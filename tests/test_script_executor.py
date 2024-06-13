from autoscriptest.script_executor import ScriptExecutor
from autoscriptest.script_parser import ScriptParser
import pytest

def test_script_executor():
    script_file = 'test_script.txt'
    parser = ScriptParser(script_file)
    commands = parser.parse()
    script = Script(script_file, commands)
    executor = ScriptExecutor(script)
    executor.execute()
    assert True