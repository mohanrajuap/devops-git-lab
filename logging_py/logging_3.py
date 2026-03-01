import logging
logging.basicConfig(
    filename="C:/Users/raju2/OneDrive/Documents/py/app.logs",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
a=int(input("enter a value"))
try:
    if a % 2==0:
     logging.info("given got is even number")
    else:
       logging.info("give number is odd")
except ValueError:
   logging.exception("Provided value is not number")