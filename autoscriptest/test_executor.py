from unittest.mock import MagicMock
from autoscriptest.script_executor import ScriptExecutor

class TestExecutor:
    """Test Executor class to test script execution"""
    def __init__(self, config: 'Config'):
        self.config = config
        self.executor = ScriptExecutor(config)

    def test_execute_script(self, script: 'Script'):
        """Test executing a script"""
        self.executor.execute_script(script)