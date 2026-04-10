import struct
import pandas as pd
import matplotlib.pyplot as plt




BUFFER_SIZE = 1064
SPEED_OFFSET = 310
THROTTLE_OFFSET = 189
sample_start = 51236
BRAKE_OFFSET = 193
brakes = []
throtles = []
data = open("src/data/formulair04_cota gp 2025-11-06 00-16-35(1).ibt", "rb").read()


for i in range(10000):
    base = sample_start + i * BUFFER_SIZE

    brake = struct.unpack_from(
        "<f",  # little-endian float
        data,
        base + BRAKE_OFFSET
    )[0]

    throtle = struct.unpack_from(
        "<f",  # little-endian float
        data,
        base + THROTTLE_OFFSET
    )[0]
    brakes.append(brake)
    throtles.append(throtle)

df = pd.DataFrame({
    "Throttle": throtles,
    "Brake": brakes
})


def plotThrottleBrakevsDistance(lapData: DataFrame):
    x = range(len(lapData))
    plt.plot(x, lapData["Throttle"])
    plt.plot(x, lapData["Brake"])

    plt.xlabel("Time")
    plt.ylabel("Throttle and Brake")

    plt.show()

    # TODO: IMPLEMENT METHOD
    # def plotTimeDeltaCumulativeTime(lapData: DataFrame):
    #     plt.xlabel("")
    #     plt.ylabel("")

    #     plt.show()


plotThrottleBrakevsDistance(df)