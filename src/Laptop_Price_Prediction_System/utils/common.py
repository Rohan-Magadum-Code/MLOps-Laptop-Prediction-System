import os
from pathlib import Path
from box import ConfigBox
from Laptop_Price_Prediction_System import logger
import yaml

def read_yaml(filepath: Path) -> ConfigBox:
    try:
        with filepath.open("r") as file:
            content = yaml.safe_load(file)
            logger.info(f"Loaded file: {filepath}")
        return ConfigBox(content)
    except Exception as e:
        raise e

def create_directories(directories: list, verbose: bool = True) -> None:
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {directory}")

def get_size(filepath: Path) -> str:
    size_in_kb = filepath.stat().st_size / 1024
    return f"{size_in_kb:.2f} KB"