# -*- coding: utf-8 -*-

name = 'python'

version = '3.7.houdini'

variants = [
            #['platform-linux', 'arch-x86_64', 'os-Pop-21.10'],
            ['platform-linux', 'arch-x86_64', 'os-Pop-22.04'],
        ]

build_command = "python {root}/build_cmd.py {install}"

uuid = "external.python"

def commands():
    #env.PATH.append('{this.root}/bin')
    pass

def post_commands():
    # these are the builtin modules for this python executable. If we don't
    # include these, some python behavior can be incorrect.
    if not building:    
        env.PYTHONHOME="${HFS}/python"
        env.PATH.prepend("${HFS}/python/bin") 
