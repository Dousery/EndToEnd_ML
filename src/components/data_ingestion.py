import os
import sys
from pathlib import Path

# Add the project root to Python path when running this file directly
if __name__ == "__main__":
    # Get the project root directory (two levels up from this file)
    project_root = Path(__file__).parent.parent.parent
    sys.path.append(str(project_root))

from src.exception import CustomException
from src.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Create artifacts directory if it doesn't exist
            artifacts_dir = 'artifacts'
            os.makedirs(artifacts_dir, exist_ok=True)
            logging.info(f"Created artifacts directory: {artifacts_dir}")
            
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved to: {self.ingestion_config.raw_data_path}")

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test data
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info(f"Train data saved to: {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved to: {self.ingestion_config.test_data_path}")

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    print(f"Data ingestion completed successfully!")
    print(f"Train data: {train_data}")
    print(f"Test data: {test_data}")

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)



