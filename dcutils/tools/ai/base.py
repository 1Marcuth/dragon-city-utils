from urllib.request import urlretrieve, build_opener, install_opener
from pydantic import validate_call
from zipfile import ZipFile
import tensorflow as tf
import numpy as np
import pathutil
import logging
import os

@validate_call
def load_labels(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        lables = [ line.strip() for line in file.readlines() ]
        
    return lables

class BaseAIConfig:
    def __init__(
        self,
        model_zip_url: str,
        model_out_dir: str,
        model_zip_filename: str,
        model_filename: str,
        labels_filename: str
    ) -> None:
        self.model_zip_url = model_zip_url
        self.model_out_dir = model_out_dir
        self.model_zip_filename = model_zip_filename
        self.model_filename = model_filename
        self.labels_filename = labels_filename

    @property
    def model_zip_file_path(self) -> str:
        return os.path.join(self.model_out_dir, self.model_zip_filename)

    @property
    def model_file_path(self) -> str:
        return os.path.join(self.model_out_dir, self.model_filename)

    @property
    def labels_file_path(self) -> str:
        return os.path.join(self.model_out_dir, self.labels_filename)

class BaseAI:
    @validate_call(config=dict(arbitrary_types_allowed=True))
    def __init__(self, config: BaseAIConfig) -> None:
        self.config = config

        if not os.path.exists(config.model_file_path) or not os.path.exists(config.labels_file_path):
            self.__download_model_zip()
            self.__unzip_model_zip()
            self.__delete_model_zip()

        self.__load_model()

    def __load_model(self):
        logging.info(f"Loading '{self.__class__.__name__}' ai model")

        np.set_printoptions(suppress=True)

        self.model = tf.keras.models.load_model(self.config.model_file_path)
        self.model.labels = load_labels(self.config.labels_file_path)

        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    def __download_model_zip(self) -> None:
        logging.info(f"Downloading model AI from: {self.config.model_zip_url}")

        if not os.path.exists(self.config.model_out_dir):
            pathutil.mktree(self.config.model_out_dir)

        opener = build_opener()
        opener.addheaders = [("User-Agent", "Mozilla/5.0")]
        install_opener(opener)

        urlretrieve(self.config.model_zip_url, self.config.model_zip_file_path)

    def __unzip_model_zip(self) -> None:
        logging.info(f"Extracting model from: {self.config.model_zip_file_path}")

        with ZipFile(self.config.model_zip_file_path, "r") as file:
            file.extractall(self.config.model_out_dir)

    def __delete_model_zip(self) -> None:
        logging.info(f"Deleting model zip from: {self.config.model_zip_file_path}")
        os.remove(self.config.model_zip_file_path)

    def __delete_model_file(self) -> None:
        logging.info(f"Deleting model from: {self.config.model_file_path}")
        os.remove(self.config.model_file_path)

    def __delete_labels_file(self) -> None:
        logging.info(f"Deleting labels from: {self.config.labels_file_path}")
        os.remove(self.config.labels_file_path)

    def update(self) -> None:
        logging.info(f"Updating the model: {self.__class__.__name__}")
        
        self.__delete_model_file()
        self.__delete_labels_file()
        self.__download_model_zip()
        self.__unzip_model_zip()
        self.__delete_model_zip()
        self.__load_model()

__all__ = [ "BaseAI", "BaseAIConfig" ]