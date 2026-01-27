name = "katana"

version="4.0v5"

description="Katana runtime"

requires = [
        ]

tools = ["katanaBin"]

build_command = "{root}/build.sh {install}"

def pre_build_commands():
    env.BASE_PATH="/opt/Katana{this.version}"

def commands():
    env.PATH.append("{root}/bin")
    alias("katana", "katanaBin")
