def read_file(file_path):
    """Read the contents of a file and return it as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")

def validate_file_path(file_path):
    """Validate the provided file path."""
    if not isinstance(file_path, str) or not file_path:
        raise ValueError("Invalid file path provided.")
    return True

def get_file_extension(file_path):
    """Return the file extension of the given file path."""
    return file_path.split('.')[-1] if '.' in file_path else ''