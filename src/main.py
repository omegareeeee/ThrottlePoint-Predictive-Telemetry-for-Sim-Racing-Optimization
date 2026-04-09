# add telemetry package to path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from telemetry.loader import fileLoader
from telemetry.visualization import visualization

def main():
    loader = fileLoader.openCsv("data/tele.csv")
    lapData = loader.getLapData()
    visualization.plotThrottleBrakevsDistance(lapData)


if __name__ == "__main__":
    main()



