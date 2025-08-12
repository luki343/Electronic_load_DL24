import sys
import logging
import runpy
from pathlib import Path

BASE_DIR = Path(__file__).parent
LOG_FILE = BASE_DIR / "app.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

def excepthook(exc_type, exc_value, exc_traceback):
    logging.error("error", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = excepthook

class LoggerWriter:
    def __init__(self, level):
        self.level = level
    def write(self, message):
        message = message.strip()
        if message:
            self.level(message)
    def flush(self):
        pass

sys.stdout = LoggerWriter(logging.info)
sys.stderr = LoggerWriter(logging.error)

logging.info("===== START APP =====")

try:
    runpy.run_path(str(BASE_DIR / "main.py"), run_name="__main__")
except Exception:
    logging.exception("CRITICAL Error")
finally:
    logging.info("===== END =====")
