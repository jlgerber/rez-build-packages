name = "gcc"

variants = [
    ["platform-linux", "arch-x86_64"]
]

build_command = "python {root}/build_cmd.py {install}"
tools = [
    "c++",
    "cpp",
    "g++",
    "gcc",
    "gcc-ar",
    "gcc-nm",
    "gcc-ranlib",
    "gcov",
    "gcov-dump",
    "gcov-tool",
    "gfortran",
    "x86_64-pc-linux-gnu-c++",
    "x86_64-pc-linux-gnu-g++",
    "x86_64-pc-linux-gnu-gcc",
    "x86_64-pc-linux-gnu-gcc-6.4.0",
    "x86_64-pc-linux-gnu-gcc-ar",
    "x86_64-pc-linux-gnu-gcc-nm",
    "x86_64-pc-linux-gnu-gcc-ranlib",
    "x86_64-pc-linux-gnu-gfortran"
        ]

#has_plugins = True

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
    env.GCC_INCLUDE_PATH = "{root}/app/include"
    env.GCC_LIBRARY_PATH = "{root}/app/lib64" 
    env.LD_LIBRARY_PATH.append("${GCC_LIBRARY_PATH}")
    env.MANPATH.append("{root}/app/share/info")
    env.INFOPATH.append("{root}/app/share/info")
    env.PATH.prepend("{root}/app/bin")
