from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

CID = os.getenv('cid')
SECRET = os.getenv('secret')