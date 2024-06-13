from unittest import TestCase
from autoscriptest.script_parser import ScriptParser
from autoscriptest.script_executor import Script

class TestScriptParser(TestCase):
    """Test Script Parser class"""
    def test_parse_script(self):
        config = MagicMock()
        script_parser = ScriptParser(config)
        script_file = "test_script.txt"
        script = script_parser.parse_script(script_file)
        self.assertIsInstance(script, Script)