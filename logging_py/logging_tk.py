import logging

logging.basicConfig(
    filename="C:/Users/raju2/OneDrive/Documents/py/app.txt",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

n = 7
logging.info(f"Program started with input: {n}")

if n % 2 == 0:
    logging.info("Number is even")
else:
    logging.info("Number is odd")

logging.info("Program finished successfully")
logging.error("ERROR BHAI")
