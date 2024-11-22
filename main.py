from src.TextSummarizer.logging import logger
from src.TextSummarizer.pipeline.stage_1_dataingestion_pipeline import DataIngestionTrainingPipiline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipiline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e