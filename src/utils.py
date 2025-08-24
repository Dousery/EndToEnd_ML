import os
import sys
from pathlib import Path

# Add the project root to Python path when running this file directly
if __name__ == "__main__":
    # Get the project root directory (one level up from this file)
    project_root = Path(__file__).parent.parent
    sys.path.append(str(project_root))

import numpy as np
import pandas as pd
from src.exception import CustomException
import dill


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    


