import subprocess

from types import SimpleNamespace
from .Program import Program


arch = subprocess.run("dpkg --print-architecture", shell=True,
                      capture_output=True, text=True).stdout.strip()
version_codename = subprocess.run("cat /etc/os-release | grep VERSION_CODENAME",
                                  shell=True, capture_output=True,
                                  text=True).stdout.strip().split('=')[-1]

docker_cfg = {
    "name": "docker",
    "install_commands": [
        "sudo apt-get update",
        "sudo apt-get install -y ca-certificates curl",
        "sudo install -m 0755 -d /etc/apt/keyrings",
        "sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc",
        "sudo chmod a+r /etc/apt/keyrings/docker.asc",       
        f"echo 'deb [arch={arch} signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu {version_codename} stable'" + \
            " | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
        "sudo apt-get update",
        "sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin",
        "sudo groupadd docker",
        "sudo usermod -aG docker $USER",
    ],
}

docker_handler = Program(**docker_cfg)

