# import util
from util import rename

def use_rename():
    # after_rename = util.rename("name")
    after_rename = rename("name")
    return after_rename

print(use_rename())