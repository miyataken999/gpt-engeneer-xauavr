from unittest import TestCase
from autoscriptest.test_executor import TestExecutor
from autoscriptest.script_executor import Script

class TestScriptExecutor(TestCase):
    """Test Script Executor class"""
    def test_execute_script(self):
        config = MagicMock()
        test_executor = TestExecutor(config)
        script = Script("test_script", ["command1", "command2"])
        test_executor.test_execute_script(script)