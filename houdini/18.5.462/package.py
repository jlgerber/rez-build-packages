name = "houdini"

variants = [
    ["platform-linux", "arch-x86_64"]
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

def commands():
    env.HFS = "{root}/app"
    env.H="${HFS}"
    env.HB = "${H}/bin"
    env.HDSO = "${H}/dsolib"
    env.HH = "${H}/houdini"
    env.HHC = "${HH}/config"
    env.HHP = "${HH}/python2.7libs"
    env.HT = "${H}/toolkit"
    env.HSB = "${HH}/sbin"
    env.TEMP="/tmp"
    
    env.LD_LIBRARY_PATH.prepend("${HDSO}")
    env.PATH.prepend("${HSB}")
    env.PATH.prepend("${HB}")
    
    env.HOUDINI_MAJOR_RELEASE = this.version_p[0]
    env.HOUDINI_MINOR_RELEASE = this.version_p[1]
    env.HOUDINI_BUILD_VERSION = this.version_p[2]
    env.HOUDINI_VERSION = this.version
    env.HOUDINI_BUILD_KERNEL = "3.10.0-1062.4.1.el7.x86_64"
    env.HOUDINI_BUILD_PLATFORM ="Red Hat Enterprise Linux Workstation release 7.7 (Maipo)"
    env.HOUDINI_BUILD_COMPILER="6.3.1"
    env.HOUDINI_BUILD_LIBC="glibc 2.17"
    env.PXR_PLUGINPATH_NAME = "/opt/redshift/redshift4solaris/18.5.462"

