name = "blender"

variants = [
    ["platform-linux", "arch-x86_64"]
]

build_command = "python {root}/build_cmd.py {install}"
tools = [

    ]

has_plugins = True

uuid = "external.blender"

@early()
def version():
    import os
    return os.path.basename(os.path.abspath(os.getcwd()))

@early()
def version_p():
    import os
    return os.path.basename(os.path.abspath(os.getcwd())).split(".")

def commands():
    env.PATH.append("{root}/app")
    env.BLENDER_MAJOR=this.version_p[0]
    env.BLENDER_MINOR=this.version_p[1]
    env.BLENDER_PATH=this.version_p[2]
    env.BLENDER_USER_CONFIG = "~/blender/${BLENDER_MAJOR}.${BLENDER_MINOR}/config"
    env.BLENDER_USER_SCRIPTS= "~/blender/${BLENDER_MAJOR}.${BLENDER_MINOR}/scripts"
