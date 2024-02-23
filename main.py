
from typing import List
from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import RedirectResponse
# from fastapi.responses import JSONResponse
from search import router as search_router
from data import get_data

# Create an instance of FastApi

# Add a startup event to load the data
async def lifespan(app: FastAPI):
    print("Starting up...")
    get_data()
    yield
    print("Shutting down...")
          
app = FastAPI(lifespan=lifespan)








####
    # Visit URL/docs# to see swagger api menu
####

# Define path to visit
# Decorator - HTTP method - route

# Redirects user to the docs (swagger) page
@app.get("/")
async def _root():
    return RedirectResponse(url="/docs#")
    return "Hello there... Phenodigm API is up and running!"



# TODO: make an endpoint to search by HP or MP?
# TODO: make an endpoint to search in a range of scores


# Add router to the app
app.include_router(search_router, prefix="/serach")
