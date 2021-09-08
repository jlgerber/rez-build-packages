name = "renderman"

variants = [
    ["platform-linux", "arch-x86_64"]
]

build_command = "python {root}/build_cmd.py {install}"
tools = [
]

has_plugins = True

uuid = "repository.renderman"

@early()
def version():
    import os
    return os.path.basename(os.path.abspath(os.getcwd()))

@early()
def version_p():
    import os
    return os.path.basename(os.path.abspath(os.getcwd())).split(".")

def commands():
    env.RMANTREE = "/opt/pixar/RenderManProServer-23.5"
    env.RFHTREE = "/opt/pixar/RenderManForHoudini-23.5"
    env.RMAN_PROCEDURALPATH = "/opt/pixar/RenderManForHoudini-23.5/18.5.351/openvdb:&"
    env.HOUDINI_PATH = "/opt/pixar/RenderManForHoudini-23.5/18.5.351:&"

