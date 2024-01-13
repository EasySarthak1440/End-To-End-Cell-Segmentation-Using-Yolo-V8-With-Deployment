import os
import zipfile
import requests
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.config_entity import DataIngestionConfig
from cellSegmentation.entity.artifacts_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e)

    def download_data(self) -> str:
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info(f"Downloading data from {dataset_url} into file {zip_file_path}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='

            # Download the file using requests
            response = requests.get(f"{prefix}{file_id}", stream=True)
            with open(zip_file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            logging.info(f"Downloaded data from {dataset_url} into file {zip_file_path}")

            return zip_file_path

        except Exception as e:
            raise AppException(e)

    def extract_zip_file(self, zip_file_path: str) -> str:
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f"Extracting zip file: {zip_file_path} into dir: {feature_store_path}")

            return feature_store_path

        except Exception as e:
            raise AppException(e)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try:
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path,
                feature_store_path=feature_store_path
            )

            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e)

# Usage example:
# data_ingestion = DataIngestion()
# data_ingestion.initiate_data_ingestion()
