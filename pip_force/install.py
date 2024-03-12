import sys
import subprocess

def install_requirements(file_path):
    if file_path is None: file_path = "requirements.txt"
    with open(file_path, 'r') as f:
        for line in f:
            requirement = line.strip()
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', requirement])
            except subprocess.CalledProcessError:
                print(f"Failed to install {requirement}")

if __name__ == "__main__":
    install_requirements(sys.argv[1])