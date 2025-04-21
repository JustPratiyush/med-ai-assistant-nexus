import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Run the main file directly
if __name__ == "__main__":
    import subprocess
    subprocess.run(["streamlit", "run", "app/main.py"])