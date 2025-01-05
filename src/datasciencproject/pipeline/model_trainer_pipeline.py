from src.datasciencproject.config.configuration import ConfigurationManager
from src.datasciencproject.components.model_trainer import ModelTrainer
from src.datasciencproject import logger

STAGE_NAME = "Model Tranier Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def intitiate_model_trainig(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()
