import sys
import os
import logging
from datetime import datetime

# Set the log file name with a timestamp to avoid overwriting old logs
log_file = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path,log_file)

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Log file name
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    level=logging.INFO  # Log level (INFO)
)

# Example usage
logging.info("Logging has been configured successfully.")
