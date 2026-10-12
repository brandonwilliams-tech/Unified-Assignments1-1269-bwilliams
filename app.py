from fastapi import FastAPI
import logging

logging.basicConfig(
    filename=r"app.log",  # r is for raw string to avoid escape characters.
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s- %(message)s",
)
# FastAPI instance: we can use this to create routes and handle requests.
app = FastAPI()


@app.get("/books")  # decorator to define route for get
def get_books():
    logging.info("Request: GET /books")
    # open the file and read it
    with open("books.txt") as file:
        # splitlines makes a list, one title per line
        books = file.read().splitlines()
    logging.info("Response: 200 OK")
    return books


@app.get("/health")
def health_check():  # health check to check if the api is running or not
    logging.info("Request: GET /health")
    logging.info("Response: 200 OK")
    return {"status": "ok"}
