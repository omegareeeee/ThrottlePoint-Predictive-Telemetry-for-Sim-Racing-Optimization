import pandas as pd
import irsdk
import struct

SESSION_INFO_OFFSET = 39600

OFFSETS = {
    "speed": 310,
    "throttle": 189,
    "brake": 193,
    "steering_angle": 185,
    "engine_rpm": 205,

    "lap_pct": 221,
    "lap_number": 209,
    "lap_completed": 213,

    "lap_time": 245,
    "last_lap_time": 241,
    "best_lap_time": 237,

    "lap_delta": 265,
    "lap_delta_ok": 273,

    "session_id": 20,
    "session_length": 44
}
    


class Parser:
    sample_start = 0
    buffer_size = 0
    brakes = []
    throttles = []
    speeds = []
    lapPcts = []
    steeringWheelAngles =[]
    engineRpms = []

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

    def read_float(data, base, key):
        return struct.unpack_from("<f", data, base + OFFSETS[key])[0]

    def read_int(data, base, key):
        return struct.unpack_from("<d", data, base + OFFSETS[key])[0]
    
    def _parse_data(self):
        data = self.ir._ibt_file.read()
        for i in range(20000):
            base = self.sample_start + (i * self.buffer_size)

            brake = read_float(data, base, "brake")
            throttle = read_float(data, base, "throttle")
            speed = read_float(data, base, "speed")
            lapPct = read_float(data, base, "lap_pct")
            steeringWheelAngle = read_float(data, base, "steering_angle")
            engineRpm = read_float(data, base, "engine_rpm")
            
            self.brakes.append(brake)
            self.throttles.append(throttle)
            self.speeds.append(speed)
            self.lapPcts.append(lapPct)
            self.steeringWheelAngles.append(steeringWheelAngle)
            self.engineRpms.append(engineRpm)

