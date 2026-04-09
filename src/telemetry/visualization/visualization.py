import matplotlib.pyplot as plt
import pandas as pd


def plotThrottleBrakevsDistance(lapData: DataFrame):
    plt.plot(lapData["LapDist"], lapData["Throttle"])
    plt.plot(lapData["LapDist"], lapData["Brake"])

    plt.xlabel("Distance")
    plt.ylabel("Throttle and Brake")

    plt.show()

    # TODO: IMPLEMENT METHOD
    # def plotTimeDeltaCumulativeTime(lapData: DataFrame):
    #     plt.xlabel("")
    #     plt.ylabel("")

    #     plt.show()

def plotSteeringAngleVsDistance(lapData: DataFrame):
    plt.plot(lapData["LapDist"], lapData["SteeringWheelAngle"])
        
    plt.xlabel("Distance")
    plt.ylabel("Steering Angle")

    plt.show()

    # TODO: IMPLEMENT METHOD
    # def plotTrackMap(lapData: DataFrame):
    #     plt.xlabel("")
    #     plt.ylabel("")

    #     plt.show()

def plotRPMVsDistance(lapData: DataFrame):
    plt.plot(lapData["LapDist"], lapData["RPM"])

    plt.xlabel("Distance")
    plt.ylabel("RPM")

    plt.show()

    # TODO: IMPLEMENT METHOD
    # def plotTireTempsWear(lapData: DataFrame):
    #     plt.plot(lapData["LapDist"], lapData[""])

    #     plt.xlabel("Distance")
    #     plt.ylabel("Tire Temps/Wear")

    #     plt.show()