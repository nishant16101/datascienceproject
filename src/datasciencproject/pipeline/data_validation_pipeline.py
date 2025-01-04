from src.datasciencproject.config.configuration import ConfigurationManager
from src.datasciencproject.components.data_validation import DataValiadtion
from src.datasciencproject import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def intitiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()
if __name__ == '__main__':
    try:
        logger.info(f">>>>>stage{STAGE_NAME} started<<<<")
        obj = DataValidationTrainingPipeline()
        obj.intitiate_data_validation()
        logger.info(f">>>stage{STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)
        raise e