"""Pipeline Shim to register pythonpath."""

import sys
import os
import logging 

LOG = logging.getLogger("rez.blender")


bl_info = {
    "name": "Pipelne Shim",
    "category": "System",
    "blender": (
        os.environ['BLENDER_MAJOR']
        , os.environ['BLENDER_MINOR']
        , os.environ['BLENDER_PATCH']
    )
}
def register():
    # Inject the PYTHONPATH environment variable into Blender's internal path
    studio_pythonpath = os.environ.get('BLENDER_PYTHONPATH', '')
    print(f"BLENDER STUDIO_PYTHON_PATH:{studio_pythonpath}")
    if studio_pythonpath:
        # Reverse to maintain original search order priority
        for path in reversed(studio_pythonpath.split(os.pathsep)):
            if path and path not in sys.path:
                sys.path.insert(0, path)
    else:
        raise RuntimeError("pythonpath not set")

    LOG.debug("Studio Pipeline: Injected %s paths into sys.path",len(studio_pythonpath.split(os.pathsep)))

def unregister():
    pass

if __name__ == "__main__":
    register()