name = "nuke"

description="nuke runtime"

requires = [
        ]

tools = ["Nuke16.0"]

build_command = "python {root}/build_cmd.py {install}"


@early()
def version():
    import os
    return os.path.basename(os.path.abspath(os.getcwd()))

@early()
def version_p():
    import os
    return os.path.basename(os.path.abspath(os.getcwd())).split(".")

def pre_build_commands():
    env.BASE_PATH="/opt/Nuke{this.version}"

def commands():
    env.PATH.append("{root}/app")
    alias("nuke", "Nuke16.0")