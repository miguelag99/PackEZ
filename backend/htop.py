from types import SimpleNamespace
from .Program import Program

htop_cfg = {
    "name": "htop",
    "install_commands": ["sudo apt-get update", "sudo apt-get install -y htop"],
}

htop_handler = Program(**htop_cfg)
