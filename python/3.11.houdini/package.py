# -*- coding: utf-8 -*-

name = 'python'

@early()
def version():
    import os
    return os.path.basename(os.path.abspath(os.getcwd()))

variants = [
            ['platform-linux', 'arch-x86_64', 'os-Pop-22.04'],
        ]

build_command = "python {root}/build_cmd.py {install}"

uuid = "external.python"

def commands():
    pass

def post_commands():
    # these are the builtin modules for this python executable. If we don't
    # include these, some python behavior can be incorrect.
    if not building:    
        env.PYTHONHOME="${HFS}/python"
        env.PATH.prepend("${HFS}/python/bin") 
