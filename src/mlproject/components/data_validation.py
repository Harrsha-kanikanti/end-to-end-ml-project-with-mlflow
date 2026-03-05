from mlproject.entity.config_entity import DataValidationConfig
import pandas as pd
from mlproject import logger

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            validation_status = all(
                col in self.config.all_schema.keys() for col in data.columns
            )
            with open(self.config.STATUS_FILE,"w") as f:
                f.write(f"validation_status: {validation_status}")
            logger.info(f"validation_status: {validation_status}")
        except Exception as e:
            logger.exception(e)
            raise e