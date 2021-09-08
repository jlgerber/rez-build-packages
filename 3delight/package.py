name = "3delight"

version="2.3.7"

description="3delight runtime"

requires = [ "katana"
        ]

tools = ["i-display", "licutils", "oslc", "tdlmake"]

build_command = "{root}/build.sh {install}"

def pre_build_commands():
    env.BASE_PATH="/opt/3delight/3delight-{this.version}/Linux-x86_64"

def commands():
    env.DELIGHT = "{root}"
    env.KATANA_RESOURCES.append("${DELIGHT}/3DelightForKatana")
    env.PATH.append("${DELIGHT}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
