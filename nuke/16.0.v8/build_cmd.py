#!/usr/bin/env python
import os
import sys

def replace_last(input: str, old_char: str, new_char: str):
    last_index = input.rfind(old_char)
    if last_index == -1:
        return input 
    else:
        return f"{input[:last_index]}{new_char}{input[last_index+1:]}"
    

installing = False
if len(sys.argv) > 1 and sys.argv[1] == "install":
    installing = True

target = os.environ.get("REZ_BUILD_PATH") if not installing else os.environ["REZ_BUILD_INSTALL_PATH"]
print( "target", target)

version = os.environ["REZ_BUILD_PROJECT_VERSION"]

nuke_dir = "Nuke{}".format(replace_last(version,".", ""))

hfs_root = os.path.join("/opt",nuke_dir)
target = os.path.join(target, "app")

try: 
    os.unlink(target)
except OSError as err:
    if not "[Errno 2]" in str(err):
        raise err

if not os.path.exists(target):
    print( "symlinking",hfs_root, "to", target)
    try:
        os.symlink(hfs_root, target)
    except OSError as err:
        print(f"error {err}")
