#!/usr/bin/env python
import os
import sys


installing = False
if len(sys.argv) > 1 and sys.argv[1] == "install":
    installing = True

target = os.environ.get("REZ_BUILD_PATH") if not installing else os.environ["REZ_BUILD_INSTALL_PATH"]
print( "target", target)

