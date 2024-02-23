# TODO: check: from functools import lru_cache
from cachetools import cached, TTLCache
import polars as pd


# Function to import the data
# TODO: change this to take data from the website's file or database. Maybe download the file into memory? 
def import_data():
    try:
        df = pd.read_csv("impc_phenodigm.csv")
        df.columns = [
            "disorder_id",
            "disorder_name",
            "human_gene_symbol",
            "mouse_model_description",
            "phenodigm_score",
            "matching_human_phenotypes",
            "matching_mouse_phenotypes",
        ]

        return df

    except:
        return "There was an error reading the file."


# Creating a cache to store the data

# Define a function to load the data
def load_data():
    df = import_data()
    rows = list(df.iter_rows(named=True))
    # return JSONResponse(content=rows)
    return rows

# Use a cached decorator from cachetools to memoize the data loading function
# TODO: might be nice to encapsulate this
# Create a cache with a maximum size of 100 and a time-to-live (TTL) of 300 seconds (5 minutes)


cache = TTLCache(maxsize=100, ttl=300)
@cached(cache)
def get_data():
    return load_data()