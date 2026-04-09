import irsdk

ir = irsdk.IRSDK()

# startup (for live data OR ibt file)
ir.startup(test_file='src/data/formulair04_cota gp 2025-11-06 00-16-35(1).ibt')
