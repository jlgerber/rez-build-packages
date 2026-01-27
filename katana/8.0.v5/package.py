name = "katana"

description="Katana runtime"

requires = [
        ]

tools = ["katanaBin"]

#build_command = "{root}/build.sh {install}"
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
    env.BASE_PATH="/opt/Katana{this.version}"

def commands():
    env.PATH.append("{root}/app")
    #alias("katana", "katanaBin")
