# Readme-Architect by Cyxx

Auto-documents your entire project in seconds using AI.

## Description

Readme-Architect is a CLI tool that scans your project folder, analyzes the code using Google's Gemini AI, and automatically generates a professional `README.md` file. It's designed to save developers time and ensure documentation is always up-to-date.

## Features

- **Automated Scanning**: Recursively scans your directory for code files while ignoring build artifacts and non-code files.
- **AI-Powered**: Uses Google Gemini Pro to understand your code logic and structure.
- **Professional Output**: Generates a structured README with sections for installation, usage, features, and more.
- **CLI Interface**: Simple command-line usage with rich visual feedback.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Cyxx-kali/Readme-Architect.git
   cd Readme-Architect
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration: Getting a Gemini API Key

To use Readme-Architect, you need a Google Gemini API key.

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Click on **Create API key**.
3. Select a project (or create a new one) and copy your API key.

### Setting the Environment Variable

You need to set the `GEMINI_API_KEY` environment variable.

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```
Or to set it permanently:
```powershell
setx GEMINI_API_KEY "your_api_key_here"
```

**Linux / macOS:**
```bash
export GEMINI_API_KEY="your_api_key_here"
```

## Usage

Run the tool from the root of the project you want to document:

```bash
python architect.py
```

The tool will scan the current directory and generate a `README.md` file (or overwrite the existing one).

## License

Created by Cyxx.
