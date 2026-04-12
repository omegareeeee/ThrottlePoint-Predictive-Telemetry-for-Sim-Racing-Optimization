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
    sample_start = 0
    buffer_size = 0
    brakes = []
    throttles = []

    def __init__(self, filePath: str):
        # check if it's vaild .ibt file
        #TODO: veryfiy this works
        fileType = filePath.split(".")[-1]
        if(fileType != "ibt"):
            raise ValueError("Invalid file extension: must be .ibt")
        self.ir = irsdk.IBT()
        self.ir.open(filePath)

        self._extract_header_info()
        self._parse_data()

    def _extract_header_info(self):
        session_info_len = self.ir._header.session_info_len
        self.buffer_size = self.ir._header.buf_len
        self.sample_start = SESSION_INFO_OFFSET + session_info_len 
    
    def _parse_data(self):
        data = self.ir._ibt_file.read()
        for i in range(1000):
            base = self.sample_start + (i * self.buffer_size)
        
            brake = struct.unpack_from(
                "<f",  # little-endian float
                data,
                base + VariablesOffsets.BRAKE
            )[0]

            throttle = struct.unpack_from(
                "<f",  # little-endian float
                data,
                base + VariablesOffsets.THROTTLE
            )[0]
            self.brakes.append(brake)
            self.throttles.append(throttle)

