import logging
logging.basicConfig(
    filename="C:/Users/raju2/OneDrive/Documents/py/app.logs",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("App is started")

logging.warning("Memory is almost full")

logging.error("Disk is full")

logging.info("app stopped")