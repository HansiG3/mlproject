import logging
import os
from datetime import datetime

# filename only
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# folder only
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# full file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig( ##this tells python how and where to write logs
    filename=LOG_FILE_PATH,
    format="[%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s]",
    level=logging.INFO ##which logs are recorded
)
if __name__=="__main__":
    logging.info("Logging started")
