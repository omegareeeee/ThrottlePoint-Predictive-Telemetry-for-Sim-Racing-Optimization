import pandas as pd
import irsdk
import struct

BUFFER_SIZE = 1064 # file dependent
SESSION_INFO_OFFSET = 39600

sample_start = 0
buffer_size = 0

class VariablesOffsets:
    SPEED = 310
    THROTTLE = 189
    BRAKE = 193 
    LAP_PCT = 221


BUFFER_SIZE = 1064 # file dependent
    # = SESSION_INFO_OFFSET + session_info_len

# TODO: implement parser
def parseIbt (filePath: str) -> DataFrame:
    # check if it's vaild .ibt file
    fileType = str.split(".")[-1]
    if(fileType != "ibt"):
        raise ValueError("Invalid file extension: must be .ibt")
    ir = irsdk.IBT()
    ir.open(filePath)
    session_info_len = ir._header.session_info_offset
    buffer_size = ir._header.buf_len
    sample_start = SESSION_INFO_OFFSET + session_info_len
