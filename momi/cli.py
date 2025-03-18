import argparse
import os
from momi.gemini_api import GeminiAPI
from momi.file_analyzer import analyze_file
from builtins import FileNotFoundError  # Import FileNotFoundError from builtins
from momi.exceptions import GeminiAPIError

def main():
    parser = argparse.ArgumentParser(description="welcome to Momi CLI")
    parser.add_argument('command', choices=['query', 'analyze'], help='Command to execute')
    parser.add_argument('input', help='Input for the command (query string or file path)')

    args = parser.parse_args()

    try:
        if args.command == 'query':
            gemini = GeminiAPI()
            response = gemini.ask_question(args.input)
            print("momi >>>", response)
        elif args.command == 'analyze':
            if not os.path.isfile(args.input):
                raise FileNotFoundError(f"The file {args.input} does not exist.")
            analysis_result = analyze_file(args.input)
            print("File Analysis Result:", analysis_result)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except GeminiAPIError as e:
        print(f"Error interacting with Gemini API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()