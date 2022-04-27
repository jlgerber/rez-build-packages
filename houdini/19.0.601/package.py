name = "houdini"

variants = [
    ["platform-linux", "arch-x86_64", "python-3.7.houdini"]
]

build_command = "python {root}/build_cmd.py {install}"
tools = [
    'houdini',
    'houdinifx',
    'mview',
    'mplay',
    'abcconvert',
    'abcecho',
    'abcinfo',
    'acombine',
    'acombine-bin',
    'aconvert',
    'aconvert-bin',
    'ainfo',
    'ainfo-bin',
    'aplay',
    'aplay-bin',
    'husk',
    'hbatch',
    'hcommand',
    'hcompile',
    'hserver',
    'hview',
    'hython',
    'mantra',
    'mplay',
    'karma',
    'mplay-bin',
    'usdcat',
    'usdchecker',
    'usddiff',
    'usddumpcrate',
    'usdedit',
    'usdrecord',
    'usdresolve',
    'usdstitch',
    'usdstichclips',
    'usdtree',
    'usdview',
    'usdzip'
]

has_plugins = True

uuid = "repository.houdini"

@early()
def version():
    import os
    return os.path.basename(os.path.abspath(os.getcwd()))

@early()
def version_p():
    import os
    return os.path.basename(os.path.abspath(os.getcwd())).split(".")

def pre_commands():
    if building:
        print("building")
        env.PYTHONHOME="/home/jgerber/packages/houdini/19.0.587/platform-linux/arch-x86_64/python-3.7.houdini/app/python"

def commands():
    env.HFS = "{root}/app"
    env.H="${HFS}"
    env.HB = "${H}/bin"
    env.HDSO = "${H}/dsolib"
    env.HH = "${H}/houdini"
    env.HHC = "${HH}/config"
    env.HHP = "${HH}/python3.7libs"
    env.HT = "${H}/toolkit"
    env.HSB = "${HH}/sbin"
    env.TEMP="/tmp"
    env.LD_PRELOAD = "/lib/x86_64-linux-gnu/libc_malloc_debug.so.0"    
    env.LD_LIBRARY_PATH.prepend("${HDSO}")
    env.PATH.prepend("${HSB}")
    env.PATH.prepend("${HB}")
    #env.PATH.prepend("{root}/app/python/bin")   
    env.HOUDINI_MAJOR_RELEASE = this.version_p[0]
    env.HOUDINI_MINOR_RELEASE = this.version_p[1]
    env.HOUDINI_BUILD_VERSION = this.version_p[2]
    env.HOUDINI_VERSION = this.version
    env.HOUDINI_BUILD_KERNEL = "3.10.0-1160.42.2.el7.x86_64"
    env.HOUDINI_BUILD_PLATFORM ="Red Hat Enterprise Linux Workstation release 7.9 (Maipo)"
    env.HOUDINI_BUILD_COMPILER="9.3.1"
    env.HOUDINI_BUILD_LIBC="glibc 2.17"
    #if building:
    #    env.PYTHONHOME="/usr/bin/python"
