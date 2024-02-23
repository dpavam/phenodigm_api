# Phenodigm API

This is a project to explore building APIs using `FastAPI` and `uvicorn`. 
This includes using `pydantic` classes and dependency management with `poetry`.




## Data
The data presented here belong to the (Disease Models website)[https://diseasemodels.research.its.qmul.ac.uk].

The data are currently imported via manual download of a `impc_phenodigm.csv`. Future implementations will fectch data automatically from the website.



## Use
To use this API you need to have (`poetry`)[https://python-poetry.org] installed.
This will create a virtual environment and handle dependecies.
1. Navigate to the root dir where `pyproject.toml` is and run `poetry install`
2. Start the virutal environemnt using `poetry shell` 
3. Run `uvicorn main:app --reload` and open the URL provided by the console to see the swagger API docs


