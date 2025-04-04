import os
from box.exceptions import BoxValueError
import yaml
from src.TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, Dict, List, Union

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    print("Reading YAML file...")
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty or not found.")
    except Exception as e:
        logger.error(f"Error reading YAML file {path_to_yaml}: {e}")
        raise BoxValueError(f"Error reading YAML file {path_to_yaml}: {e}")
    

@ensure_annotations
def create_directories(path_to_dirs: List, verbose = True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_dirs (List[Path]): List of directory paths to create.
        
    Returns:
        None
    """

    print("Creating directories...")
    for dir_path in path_to_dirs:
        try:
            os.makedirs(dir_path, exist_ok=True)
            logger.info(f"Directory {dir_path} created successfully.")
        except Exception as e:
            logger.error(f"Error creating directory {dir_path}: {e}")
            raise e
        if verbose:
            logger.info(f"createrd directory at {dir_path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file or directory in KB.
    
    Args:
        path (Union[Path, str]): Path to the file or directory.
        
    Returns:
        str: Size in KB.
    """
    if os.path.exists(path):
        size = round(os.path.getsize(path) /1024)
        return f"{size} KB"