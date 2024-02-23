from typing import List
from fastapi import APIRouter, HTTPException
from data import get_data
from models import DisorderRecord


# Create a reusable modular endpoint 
router = APIRouter(tags=["search"], responses={404: {"description": "Not found"}})

@router.get("/diseases/{disorder_id}" , response_model=List[DisorderRecord])
def search_by_disorder_id(disorder_id: str):

    # get cached data
    data = get_data()

    # TODO: make a function
    # Search for the dictionary with the matching disorder_id
    matching_records = [record for record in data if record["disorder_id"] == disorder_id]

    # If no matching record is found, raise an HTTPException with status code 404
    if not matching_records:
        raise HTTPException(status_code=404, detail="Disorder ID not found")

    # Return the first matching record (assuming disorder_id is unique)
    # Make this a serialized pydantic model to make it jsony
    return [DisorderRecord(**record) for record in matching_records]


# TODO: make an endpoint to search by gene
@router.get("/genes/{gene_symbol}", response_model=List[DisorderRecord])
def search_by_gene(gene_symbol: str):
    # get cached data
    data = get_data()
    matching_records = [record for record in data if record["human_gene_symbol"] == gene_symbol]

     # If no matching record is found, raise an HTTPException with status code 404
    if not matching_records:
        raise HTTPException(status_code=404, detail="Gene symbol not found")

    # Return the first matching record (assuming disorder_id is unique)
    # Make this a serialized pydantic model to make it jsony
    return [DisorderRecord(**record) for record in matching_records]