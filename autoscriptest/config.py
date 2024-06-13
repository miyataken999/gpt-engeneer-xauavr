class Config:
    """Configuration class for autoscriptest"""
    def __init__(self, script_dir: str, output_dir: str):
        self.script_dir = script_dir
        self.output_dir = output_dir