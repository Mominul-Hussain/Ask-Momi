# AskMomi CLI Tool

## Overview
Momi is a command-line interface (CLI) tool that utilizes the Google Gemini API to answer questions and analyze local files. It is designed to work from any directory on Windows 10 and follows security best practices.

## Features
- Interacts with the Google Gemini API to provide answers to user queries.
- Analyzes local files for relevant information.
- Command-line interface for easy usage.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/momi-cli.git
   cd momi-cli
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy `.env.example` to `.env` and generate api key then replace it with 'your_api_key'.
   

## Usage

To use the tool, simply call it from the command line with the keyword `momi` followed by command then your question or the path to the file you want to analyze.

Example:
```
momi query "What is llm"
```
or
```
momi analyze "C:\path\to\your\file.txt"
```

## Error Handling
The tool includes robust error handling to manage issues such as API request failures and file reading errors. Custom exceptions are defined to provide clear feedback to the user.

## Security Best Practices
- API keys and sensitive information are stored in environment variables.
- Input validation is performed to prevent injection attacks and ensure data integrity.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.