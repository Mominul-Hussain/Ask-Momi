import unittest
from momi.cli import main

class TestCLI(unittest.TestCase):
    def test_help_command(self):
        result = main(['momi', '--help'])
        self.assertIn('usage:', result)

    def test_version_command(self):
        result = main(['momi', '--version'])
        self.assertIn('Version:', result)

    def test_invalid_command(self):
        with self.assertRaises(SystemExit) as cm:
            main(['momi', 'invalid_command'])
        self.assertEqual(cm.exception.code, 1)

    def test_analyze_file_command(self):
        result = main(['momi', 'analyze', 'test_file.txt'])
        self.assertIn('File analysis complete', result)

if __name__ == '__main__':
    unittest.main()