import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Core.Support import Language


class LanguageFallbackTests(unittest.TestCase):
    def test_get_language_falls_back_when_config_is_missing(self):
        original_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp_dir:
            os.chdir(tmp_dir)
            try:
                self.assertEqual(Language.Translation.Get_Language(), "Lang/english.json")
            finally:
                os.chdir(original_cwd)


if __name__ == "__main__":
    unittest.main()
