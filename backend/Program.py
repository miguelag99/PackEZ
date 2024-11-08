import shutil
import subprocess
import time

from typing import Callable

class Program:
    def __init__(self,
                 name: str,
                 install_commands: list[str],
                 get_state_fn: Callable = None) -> None:
        self.name = name
        self.install_commands = install_commands
        self.get_state_fn = get_state_fn
        self.status = self.get_state()

    def get_state(self) -> str:
        """Check if program is installed by looking for it in system PATH"""
        if self.get_state_fn == None:
            if shutil.which(self.name):
                return "Installed"
            return "Not installed"
        else:
            # TODO: Implement get_state_command with custom command
            pass

    def install(self, status_element) -> bool:
        """Execute installation commands with progress updates"""
        try:
            for cmd in self.install_commands:
                status_element.write(f"Running: {cmd}")
                subprocess.run(cmd, shell=True, check=True)
                time.sleep(1)  # Small delay to show command
            
            self.status = self.get_state()
            return True
        except subprocess.CalledProcessError:
            return False