from dataclasses import dataclass
from typing import List

@dataclass
class Script:
    """Script class to hold script information"""
    name: str
    commands: List[str]

class ScriptExecutor:
    """Script Executor class to execute scripts"""
    def __init__(self, config: 'Config'):
        self.config = config

    def execute_script(self, script: Script):
        """Execute a script"""
        # TO DO: implement script execution logic
        print(f"Executing script {script.name}")
        for command in script.commands:
            print(f"Executing command {command}")