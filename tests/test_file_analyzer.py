import unittest
from momi.file_analyzer import FileAnalyzer
from momi.exceptions import FileAnalyzerError

class TestFileAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = FileAnalyzer()

    def test_read_file_success(self):
        content = self.analyzer.read_file('test_file.txt')
        self.assertIsInstance(content, str)

    def test_read_file_not_found(self):
        with self.assertRaises(FileAnalyzerError):
            self.analyzer.read_file('non_existent_file.txt')

    def test_analyze_file_content(self):
        self.analyzer.read_file('test_file.txt')
        result = self.analyzer.analyze_content('sample content')
        self.assertIsInstance(result, dict)

    def test_analyze_empty_file(self):
        self.analyzer.read_file('empty_file.txt')
        result = self.analyzer.analyze_content('')
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()