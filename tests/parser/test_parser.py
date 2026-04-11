import pytest
from src.telemetry.parser import parser

class TestClass:
    def testIncorrectFileType(self):
        with pytest.raises(ValueError("Invalid file extension: must be .ibt")):
            ibt_parser = parser.Parser("data.py")