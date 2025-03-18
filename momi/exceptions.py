class GeminiAPIError(Exception):
    """Exception raised for errors in the interaction with the Google Gemini API."""
    pass

class FileAnalysisError(Exception):
    """Exception raised for errors during file analysis."""
    pass

class InvalidInputError(Exception):
    """Exception raised for invalid input provided by the user."""
    pass

class ConfigurationError(Exception):
    """Exception raised for errors in configuration settings."""
    pass