import sys
import os
from unittest.mock import patch
from main import use_rename

@patch("main.util")
def test_use_rename(mock_util):
    mock_util.rename.return_value = "name"
    assert use_rename() == "name"