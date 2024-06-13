from typing import List

class ScriptParser:
    """Script Parser class to parse scripts"""
    def __init__(self, config: 'Config'):
        self.config = config

    def parse_script(self, script_file: str) -> 'Script':
        """Parse a script file and return a Script object"""
        # TO DO: implement script parsing logic
        with open(script_file, 'r') as f:
            lines = f.readlines()
        script_name = lines[0].strip()
        commands = [line.strip() for line in lines[1:]]
        return Script(script_name, commands)