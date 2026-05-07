"""Inject pythonpath."""
import sys
import os
import logging 

LOG = logging.getLogger("rez.blender")

# Inject the PYTHONPATH environment variable into Blender's internal path
studio_pythonpath = os.environ.get('PYTHONPATH', '')
if studio_pythonpath:
    # Reverse to maintain original search order priority
    for path in reversed(studio_pythonpath.split(os.pathsep)):
        if path and path not in sys.path:
            sys.path.insert(0, path)

LOG.debug("Studio Pipeline: Injected %s paths into sys.path",len(studio_pythonpath.split(os.pathsep)))
