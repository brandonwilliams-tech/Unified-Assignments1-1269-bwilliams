from fastapi import FastAPI
import logging
logging.basicConfig(filename=r"C:\Users\media\OneDrive\Documents\Fall2026-Python\Unified_Assignment1\app.log",#r is for raw string to avoid escape characters.
                    level=logging.INFO,
                    format="%(asctime)s -%(levelname)s- %(message)s")

app=FastAPI()#FastAPI instance: we can use this to create routes and handle requests.
@app.get("/books")#decorator to define route for get
def get_books():
    logging.info("Request: GET /books")
    with open("books.txt") as file:#open the file and read it
        books=file.read().splitlines()#splitlines makes a list, one title per line
    logging.info("Response: 200 OK")
    return books

@app.get("/health")
def health_check():#health check to check if the api is running or not
    logging.info("Request: GET /health")
    logging.info("Response: 200 OK")
    return{"status":"ok"}