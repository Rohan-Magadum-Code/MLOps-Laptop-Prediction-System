from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] : %(levelname)s : %(message)s"
)

Project_Name = "Laptop_Price_Prediction_System"

Files = [
    ".github/workflows/.gitkeep",
    f"src/{Project_Name}/__init__.py",
    f"src/{Project_Name}/config/__init__.py",
    f"src/{Project_Name}/config/configuration.py",
    f"src/{Project_Name}/components/__init__.py",
    f"src/{Project_Name}/constants/__init__.py",
    f"src/{Project_Name}/entity/__init__.py",
    f"src/{Project_Name}/entity/config_entity.py",
    f"src/{Project_Name}/pipeline/__init__.py",
    f"src/{Project_Name}/utils/__init__.py",
    f"src/{Project_Name}/utils/common.py",
    "config/config.yaml",
    "schema.yaml",
    "params.yaml",
    "research/trails.ipynb",
    "requirements.txt",
    "setup.py",
    "main.py",
    "app.py",
    "streamlit.py"
]

def create_project_structure(files: list[str]) -> None:
    for file in files:
        filepath = Path(file)

        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            if not filepath.exists() or filepath.stat().st_size == 0:
                filepath.touch(exist_ok=True)
                logging.info(f"Created file: {filepath}")
            else:
                logging.info(f"Already exists: {filepath}")
        except Exception as e:
            raise e

def main():
    create_project_structure(Files)

if __name__ == "__main__":
    main()