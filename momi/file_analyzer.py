import os
import re  # Add import for regex
from momi.gemini_api import GeminiAPI
from momi.exceptions import GeminiAPIError
from colorama import Fore, Style, init  # Add colorama for formatting

# Initialize colorama for Windows terminals
init()

def analyze_file(file_path):
    """
    Analyzes a file and returns a dictionary containing the analysis results.

    Args:
        file_path (str): The path to the file to be analyzed.

    Returns:
        dict: A dictionary containing analysis results, such as line count, word count, etc.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    analysis_results = {
        'file_name': os.path.basename(file_path),
        'file_size': os.path.getsize(file_path),
        'line_count': 0,
        'word_count': 0,
        'char_count': 0,
        'gemini_analysis': None  # Add a field for Gemini's analysis
    }

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()  # Read the entire file content
            analysis_results['line_count'] = len(file_content.splitlines())
            analysis_results['word_count'] = len(file_content.split())
            analysis_results['char_count'] = len(file_content)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

    # Call Gemini API to analyze the code
    try:
        gemini_api = GeminiAPI()  # Instantiate GeminiAPI
        prompt = f"Please analyze the following code for potential errors, bugs, and improvements:\n\n{file_content}"
        gemini_response = gemini_api.ask_question(prompt)
        
        # Format the response using the same method as in gemini_api.py
        formatted_analysis = _format_text_with_code_blocks(gemini_response)
        analysis_results['gemini_analysis'] = formatted_analysis
    except GeminiAPIError as e:
        analysis_results['gemini_analysis'] = f"Error during Gemini analysis: {e}"

    return analysis_results

def _format_text_with_code_blocks(text):
    """
    Format text by preserving markdown code blocks and normal text.
    Code blocks are kept as is, and regular text is also preserved without wrapping.
    """
    # Regex to identify markdown code blocks (```language ... ```)
    code_block_pattern = r'```(?:\w*)\n(.*?)```'
    
    # Split the text into code blocks and non-code blocks
    parts = []
    last_end = 0
    
    for match in re.finditer(code_block_pattern, text, re.DOTALL):
        # Add the text before this code block
        if match.start() > last_end:
            regular_text = text[last_end:match.start()]
            parts.append(regular_text)
        
        # Add the code block with its original formatting
        code_block = match.group(0)
        parts.append(code_block)
        
        last_end = match.end()
    
    # Add any remaining text after the last code block
    if last_end < len(text):
        parts.append(text[last_end:])
    
    # Join all parts together
    return ''.join(parts)