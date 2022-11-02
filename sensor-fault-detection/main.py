from pymongo import MongoClient
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.logger import logging

import sys


if __name__ == '__main__':

    """  mogodb_client = MongoDBClient()
    print("COllection Name:", mogodb_client.database.list_collection_names()) """


    logging.info("Main Starting")
    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()