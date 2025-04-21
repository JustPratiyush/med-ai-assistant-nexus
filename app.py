import sys
import os

# Add project root directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Run the main file using streamlit
if __name__ == "__main__":
    import subprocess
    subprocess.run(["streamlit", "run", "app/main.py"])