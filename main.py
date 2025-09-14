from Chicken_disease_classification import logger
from Chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chicken_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from Chicken_disease_classification.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME_01 = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME_01} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME_01} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_02 = "Prepare Base Model"
try:
    logger.info(f">>>>> stage {STAGE_NAME_02} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME_02} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME_03 = "Training Stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME_03} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME_03} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
