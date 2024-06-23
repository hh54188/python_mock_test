import sys
import os
from unittest.mock import patch

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from main import use_rename

@patch("util.rename")
def test_use_rename(mock_rename):
    mock_rename.return_value = "name2"
    assert use_rename() == "name"