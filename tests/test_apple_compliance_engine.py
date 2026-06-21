import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO
from src.apple_compliance_engine import main, generate_compliant_video, Video

class TestAppleComplianceEngine(unittest.TestCase):
    def test_generate_compliant_video(self):
        video = Video("test_video.mp4", 10)
        compliant_video = generate_compliant_video(video)
        self.assertEqual(compliant_video, "black_screen_test_video.mp4")

    def test_main(self):
        with patch('sys.argv', ['script.py', '-p', 'test_video.mp4', '-d', '10']):
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                main()
                self.assertIn("Compliant video generated: black_screen_test_video.mp4", fake_stdout.getvalue())

    def test_main_no_args(self):
        with patch('sys.argv', ['script.py']):
            with patch('sys.stdout', new=StringIO()) as fake_stdout:
                main()
                self.assertIn("Please provide both path and duration.", fake_stdout.getvalue())

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    unittest.main()
