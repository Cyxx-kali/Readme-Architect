# // Made by Cyxx
import os
from pathlib import Path

def should_ignore(path, ignore_dirs=None, ignore_files=None):
    if ignore_dirs is None:
        ignore_dirs = {
            '.git', '__pycache__', 'venv', 'env', 'node_modules', 
            '.idea', '.vscode', 'dist', 'build', 'site-packages'
        }
    if ignore_files is None:
        ignore_files = {
            '.env', '.DS_Store', 'Thumbs.db', 'README.md', 
            'poetry.lock', 'package-lock.json', 'yarn.lock'
        }
    
    parts = path.parts
    for part in parts:
        if part in ignore_dirs:
            return True
    
    if path.name in ignore_files:
        return True
        
    return False

def scan_directory(directory="."):
    """
    Scans the directory for code files, ignoring specified directories and files.
    Returns a list of dictionaries containing file path and content.
    """
    code_files = []
    base_path = Path(directory)
    
    # Common code extensions to look for
    extensions = {
        '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.c', '.cpp', 
        '.h', '.hpp', '.cs', '.go', '.rs', '.php', '.rb', '.html', 
        '.css', '.json', '.xml', '.yaml', '.yml', '.sql', '.sh'
    }

    try:
        for file_path in base_path.rglob('*'):
            if file_path.is_file():
                # Check if we should ignore this file
                if should_ignore(file_path):
                    continue
                
                # Check extension
                if file_path.suffix.lower() not in extensions and file_path.name != 'requirements.txt':
                    continue

                try:
                    # Read content
                    content = file_path.read_text(encoding='utf-8', errors='ignore')
                    if content.strip():  # Only include non-empty files
                        # Store relative path
                        rel_path = file_path.relative_to(base_path)
                        code_files.append({
                            'path': str(rel_path),
                            'content': content
                        })
                except Exception as e:
                    print(f"Warning: Could not read file {file_path}: {e}")

    except Exception as e:
        print(f"Error scanning directory: {e}")
        
    return code_files
