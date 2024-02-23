
from typing import List
# embeded in fastapi and recommended for creating complex classes, for json serializaton and data validation compared to dataclasses 
from pydantic import BaseModel, Field


# Create a class to store each row
# FIX: This is not being used
class DataRow(BaseModel):
    """ Model to store diseases from each row in the IMPC phenodigm dataset

    Args:
        BaseModel (_type_): _description_
    """
    disorder_id: List[str] = Field(..., title="Disorder ID", description="The unique identifier for the disorder")
    disorder_name: List[str] = Field(..., title="Disorder Name", description="The name of the disorder")
    human_gene_symbol: List[str]  = Field(..., title="Human Gene Symbol)", description="The gene symbol as per HGNC")
    mouse_model_description: List[str] = Field(..., title="Mouse Model Description", description="The description of the mouse model")
    phenodigm_score: List[float] = Field(..., title="Phenodigm Score", description="The phenodigm score")
    matching_human_phenotypes: List[str] = Field(..., title="Matching Human Phenotypes", description="List of matching HP terms")
    matching_mouse_phenotypes: List[str] =  Field(..., title="Matching Mouse Phenotypes", description="List of matching MP terms")


class DisorderRecord(BaseModel):
    """ Model to store disorder data """
    disorder_id: str = Field(..., title="Disorder ID", description="The unique identifier for the disorder")
    disorder_name: str = Field(..., title="Disorder Name", description="The name of the disorder")
    human_gene_symbol: str = Field(..., title="Human Gene Symbol", description="The gene symbol as per HGNC")
    mouse_model_description: str = Field(..., title="Mouse Model Description", description="The description of the mouse model")
    phenodigm_score: float = Field(..., title="Phenodigm Score", description="The phenodigm score")
    matching_human_phenotypes: str = Field(..., title="Matching Human Phenotypes", description="List of matching HP terms")
    matching_mouse_phenotypes: str = Field(..., title="Matching Mouse Phenotypes", description="List of matching MP terms")