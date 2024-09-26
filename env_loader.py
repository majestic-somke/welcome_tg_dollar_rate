import os
from dotenv import load_dotenv


class EnvLoader:
    def __init__(self):
        self.env_file = os.path.join(os.path.dirname(__file__), '.env.dev')
        self.load_env()

    def load_env(self):
        load_dotenv(self.env_file)

    def get_var(self, var_name):
        return os.getenv(var_name)


eloader = EnvLoader()
