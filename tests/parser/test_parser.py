import pytest
import src.telemetry.parser.parser as p

class TestClass:        
    def testFileType(self):
        ibt_parser = p.Parser("data.ibt")

    def testIncorrectFileType(self):
        with pytest.raises(ValueError):
            ibt_parser = p.Parser("incorrectType.py")