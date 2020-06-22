#!/usr/bin/env python
import os
import sys


installing = False
if len(sys.argv) > 1 and sys.argv[1] == "install":
    installing = True

target = os.environ.get("REZ_BUILD_PATH") if not installing else os.environ["REZ_BUILD_INSTALL_PATH"]
print "target", target

version = os.environ["REZ_BUILD_PROJECT_VERSION"]


source = os.path.join("/opt","gcc",version)
target = os.path.join(target, "app")


if not os.path.exists(target):
    print "symlinking", source, "to", target
    os.symlink(source, target)

