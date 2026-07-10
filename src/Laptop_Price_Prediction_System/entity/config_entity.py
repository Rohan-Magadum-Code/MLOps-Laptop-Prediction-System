from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_dir: Path
    train_data_path: str
    test_data_path: str
    preprocessor_obj_file_path: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    preprocessor_obj_file_path: str
    train_data_path: str
    model_name: str
    n_estimators: float
    max_depth: float
    min_samples_split: int
    min_samples_leaf: int
    target_column: str