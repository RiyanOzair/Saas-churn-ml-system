import logging
import os
from datetime import datetime


LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

log_file_name = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

log_file_path = os.path.join(LOG_DIR, log_file_name)

logging.basicConfig(
    level=logging.INFO,
    filename = log_file_path,
    format="[%(asctime)s] %(levelname)s - %(message)s",
)