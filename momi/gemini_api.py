import requests
import os
import re
from dotenv import load_dotenv
from momi.exceptions import GeminiAPIError
import textwrap  # For line wrapping
from colorama import Fore, Back, Style, init

# Initialize colorama for Windows terminals
init()

load_dotenv()

class GeminiAPI:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    def ask_question(self, question):
        if not self.api_key:
            raise GeminiAPIError("API key is missing. Please set API_KEY in your environment variables.")
        
        url = f"{self.base_url}?key={self.api_key}"
        headers = {'Content-Type': 'application/json'}
        data = {
            "contents": [{"parts": [{"text": question}]}]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            response_json = response.json()

            # Extract the text from the response
            if response_json and 'candidates' in response_json and len(response_json['candidates']) > 0:
                candidate = response_json['candidates'][0]
                text = candidate['content']['parts'][0]['text']

                # Process the text to format code blocks
                formatted_text = self._format_text_with_code_blocks(text)
                return formatted_text
            return "No response text found."
        except requests.exceptions.RequestException as e:
            raise GeminiAPIError(f"Error interacting with Gemini API: {e}")
    
    def _format_text_with_code_blocks(self, text):
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