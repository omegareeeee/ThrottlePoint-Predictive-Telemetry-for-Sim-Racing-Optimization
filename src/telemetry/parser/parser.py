import pandas as pd

def parseIbt (filePath: str) -> DataFrame:
    # check if it's vaild .ibt file
    fileType = str.split(".")[-1]
    if(fileType != "ibt"):
        raise ValueError("Invalid file extension: must be .ibt") 
    

    with open(filePath, "r") as file:
        #Do something
    
    #TODO: figure out how to parse a single data point (throttle)
    # df = pd.DataFrame(columns=['Brake', 'Throttle', 'Speed', 'LapCurrentLapTime', 'Distance', 'LapDistPct'])