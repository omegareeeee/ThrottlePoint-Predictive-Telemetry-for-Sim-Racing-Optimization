import pandas as pd
import irsdk
import struct

SESSION_INFO_OFFSET = 39600

class VariablesOffsets:
    SPEED = 310
    THROTTLE = 189
    BRAKE = 193 
    LAP_PCT = 221

class Parser:
    self.sample_start = 0
    self.buffer_size = 0
    self.ir
    def __init__(self, filePath: str):
        # check if it's vaild .ibt file
        #TODO: veryfiy this works
        fileType = str.split(".")[-1]
        if(fileType != "ibt"):
            raise ValueError("Invalid file extension: must be .ibt")
        self.ir = irsdk.IBT()
        ir.open(filePath)

    def extractHeaderInfo(ir: IBT):
        session_info_len = ir._header.session_info_offset
        buffer_size = ir._header.buf_len
        sample_start = SESSION_INFO_OFFSET + session_info_len
