import platform

def get_os_info():
    return {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
    }

os_info = get_os_info()
print(f"Operating System: {os_info['system']}")
print(f"Release: {os_info['release']}")
print(f"Version: {os_info['version']}")
