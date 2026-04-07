import pandas as pd
from pandas import DataFrame

class fileLoader:
    def __init__(self, filetype: str, filepath: str) -> DataFrame:
        if(filetype == "csv"):
            self.lapData = self.openCsv(filepath)
        # TODO: implement Ibt
        # elif(filetype == "ibt"):
        #     openIbt(filepath)
        else:
            raise ValueError(f"Unsupported file type: {filetype}")

            
    def openCsv (self, filepath: str) -> DataFrame:
        df = pd.read_csv(filepath)
        return df
    
    def getLapData(self) -> DataFrame:
        return self.lapData

    # TODO: implement Ibt
    # def openIbt (filepath: String) -> DataFrame: