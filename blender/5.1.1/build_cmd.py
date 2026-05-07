#!/usr/bin/env python
import os
import sys
import pathlib
import shutil

installing = False
if len(sys.argv) > 1 and sys.argv[1] == "install":
    installing = True

target = os.environ.get("REZ_BUILD_PATH") if not installing else os.environ["REZ_BUILD_INSTALL_PATH"]
print( "target", target)

version = os.environ["REZ_BUILD_PROJECT_VERSION"]

blender_dir = "blender-{}-linux-x64".format(version)

blender_root = os.path.join("/opt",blender_dir)
target = os.path.join(target, "app")


if not os.path.exists(target):
    print( "symlinking",blender_root, "to", target)
    os.symlink(blender_root, target)

# set up shim
blender_scripts = os.environ.get("BLENDER_USER_SCRIPTS")
if blender_scripts not in ["", None]:
    blender_scripts = pathlib.Path(blender_scripts)
    blender_scripts.mkdir(exist_ok=True, parents=True)
    source_path = pathlib.Path(os.environ["REZ_BUILD_SOURCE_PATH"])
    shim = source_path / "pythonpath_shim.py"
    shutil.copy2(shim, blender_scripts)
else:
    raise RuntimeError("BLENDER_USER_SCRIPTS not set")