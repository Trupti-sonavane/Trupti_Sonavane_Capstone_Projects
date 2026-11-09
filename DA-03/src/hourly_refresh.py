from pathlib import Path
import subprocess
import sys

PROJECT_DIR = Path(__file__).resolve().parent.parent

scripts = [
    PROJECT_DIR / "generate_data.py",
    PROJECT_DIR / "src" / "import_to_postgres.py",
]

for script in scripts:
    print(f"Running: {script.name}")
    subprocess.run([sys.executable, str(script)], check=True)

print("Hourly refresh completed successfully.")