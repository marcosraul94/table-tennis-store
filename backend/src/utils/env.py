import os
from src.utils.enum import Stage

stage = Stage(os.environ.get('STAGE', Stage.CLOUD))
