from types import SimpleNamespace
from .Program import Program

git_cfg = {
    "name": "git",
    "install_commands": ["sudo apt-get update", "sudo apt-get install -y git"],
}

git_handler = Program(**git_cfg)
