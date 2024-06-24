import sys
import os
from unittest.mock import patch
import main
from main import use_rename

# @patch("main.rename")
# def test_use_rename(mocked_rename):
#     mocked_rename.return_value = "name"
#     assert use_rename() == "name"

def fake_rename(name: str) -> str:
    return 'Hello World'

def test_use_rename():
    main.rename = fake_rename
    assert use_rename() == "name"