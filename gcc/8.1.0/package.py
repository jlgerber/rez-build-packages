name = "gcc"

variants = [
    ["platform-linux", "arch-x86_64"]
]

build_command = "python {root}/build_cmd.py {install}"
tools = [
]

has_plugins = True

uuid = "repository.gcc"

@early()
def version():
    import os
    return os.path.basename(os.path.abspath(os.getcwd()))

@early()
def version_p():
    import os
    return os.path.basename(os.path.abspath(os.getcwd())).split(".")

def commands():
    env.LD_LIBRARY_PATH.prepend("${HDSO}")
    env.PATH.prepend("${HSB}")

