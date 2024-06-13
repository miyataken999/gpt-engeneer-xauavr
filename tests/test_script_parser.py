from autoscriptest.script_parser import ScriptParser
import pytest

def test_script_parser():
    script_file = 'test_script.txt'
    parser = ScriptParser(script_file)
    commands = parser.parse()
    assert len(commands) > 0