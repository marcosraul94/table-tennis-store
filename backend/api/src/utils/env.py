import os
from src.utils.enum import ENV

env = ENV(os.environ.get("ENV", ENV.LOCAL))
