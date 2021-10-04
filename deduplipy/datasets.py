import os
import logging

import pandas as pd
from pkg_resources import resource_filename

logger = logging.getLogger()

def load_stoxx50() -> pd.DataFrame:
    file_path = resource_filename(
        "deduplipy", os.path.join("data", "stoxx50_extended_with_id.xlsx")
    )
    df = pd.read_excel(file_path, engine="openpyxl")
    logger.info("Column names: 'name'")
    return df[["name"]]


def load_voters() -> pd.DataFrame:
    file_path = resource_filename("deduplipy", os.path.join("data", "voter_names.csv"))
    df = pd.read_csv(file_path)
    logger.info("Column names: 'name', 'suburb', 'postcode'")
    return df


def load_data(kind: str = "voters") -> pd.DataFrame:
    """
    Load data for experimentation. `kind` can be 'stoxx50' or 'voters'.

    Stoxx 50 data are created by the developer of DedupliPy. Voters data is based on the North Carolina voter registry
    and this dataset is provided by Prof. Erhard Rahm ('Comparative Evaluation of Distributed Clustering Schemes for
    Multi-source Entity Resolution').

    https://dbs.uni-leipzig.de/research/projects/object_matching/benchmark_datasets_for_entity_resolution

    Args:
        kind: 'stoxx50' or 'voters'

    Returns:
        Pandas dataframe containing experimentation dataset
    """
    if kind == "stoxx50":
        return load_stoxx50()
    elif kind == "voters":
        return load_voters()
    else:
        raise ValueError(f"Unknown dataset {kind}")
