import os

from dotenv import load_dotenv

load_dotenv()
class EnvReader:
    @staticmethod
    def get_env_variable_value(variable_name):
        env_variable_value = os.getenv(variable_name)
        if env_variable_value is None:
            raise Exception(f"Для переменной {variable_name} не определено значения")
        return env_variable_value