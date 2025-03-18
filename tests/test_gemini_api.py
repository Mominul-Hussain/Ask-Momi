import unittest
from momi.gemini_api import query_gemini_api
from momi.exceptions import GeminiAPIError

class TestGeminiAPI(unittest.TestCase):

    def test_successful_query(self):
        response = query_gemini_api("What is the capital of France?")
        self.assertIn("Paris", response)

    def test_query_with_invalid_input(self):
        with self.assertRaises(GeminiAPIError):
            query_gemini_api("")

    def test_api_response_format(self):
        response = query_gemini_api("Tell me about Python.")
        self.assertIsInstance(response, dict)
        self.assertIn("answer", response)

if __name__ == '__main__':
    unittest.main()