# // Made by Cyxx
import os
import sys
import click
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from scanner import scan_directory

console = Console()

BANNER = "Readme-Architect | Powered by AI | Created by Cyxx"

def get_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/bold red] GEMINI_API_KEY environment variable not found.")
        console.print("Please set your Gemini API key in your environment variables.")
        console.print("Windows: setx GEMINI_API_KEY \"your_key_here\"")
        console.print("Linux/Mac: export GEMINI_API_KEY=\"your_key_here\"")
        sys.exit(1)
    return api_key

def generate_readme(code_files):
    """
    Sends code summaries to Gemini and generates a README.
    """
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    
    # Use a model that supports large context if possible, or standard Pro model
    model = genai.GenerativeModel('gemini-1.5-pro')

    # Prepare prompt
    prompt = "You are an expert technical writer. I will provide you with the source code of a project. " \
             "Your task is to generate a comprehensive and professional README.md file for it.\n\n" \
             "The README should include:\n" \
             "1. Project Title and Description\n" \
             "2. Key Features\n" \
             "3. Installation Instructions\n" \
             "4. Usage Guide\n" \
             "5. Project Structure (optional but good)\n" \
             "6. Technologies Used\n\n" \
             "Here are the files:\n\n"

    for file in code_files:
        prompt += f"--- FILE: {file['path']} ---\n"
        prompt += f"{file['content']}\n"
        prompt += "---\n\n"

    prompt += "\nOutput ONLY the raw markdown content for the README.md file. Do not include markdown code block ticks ```markdown or ```."

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        console.print(f"[bold red]AI Generation Error:[/bold red] {e}")
        sys.exit(1)

@click.command()
def main():
    """
    Readme-Architect: Auto-generate README.md for your project using AI.
    """
    # Display Banner
    console.print(Panel(f"[bold cyan]{BANNER}[/bold cyan]", border_style="cyan"))

    # Scan files
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task1 = progress.add_task(description="Scanning directory...", total=None)
        code_files = scan_directory(".")
        progress.remove_task(task1)
    
    if not code_files:
        console.print("[yellow]No code files found in the current directory.[/yellow]")
        return

    console.print(f"[green]Found {len(code_files)} files.[/green]")
    
    # Generate README
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task2 = progress.add_task(description="Generating README with Gemini...", total=None)
        readme_content = generate_readme(code_files)
        progress.remove_task(task2)

    # Save README
    output_file = "README.md"
    
    # If README.md exists, maybe backup or overwrite? The prompt implies generating one.
    # I'll overwrite but warn if it exists? Or just overwrite.
    # Let's write to README.md directly as requested.
    
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(readme_content)
        console.print(f"[bold green]Success![/bold green] Generated {output_file}")
    except Exception as e:
        console.print(f"[bold red]Error writing file:[/bold red] {e}")

if __name__ == "__main__":
    main()
