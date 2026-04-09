import pandas as pd
from pandas import DataFrame
            
def openCsv (filepath: str) -> DataFrame:
    df = pd.read_csv(filepath)
    return df

# TODO: implement Ibt
# def openIbt (filepath: String) -> DataFrame:

# def cleanFile()