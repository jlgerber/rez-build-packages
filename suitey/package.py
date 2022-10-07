name = "suitey"

variants = []

build_command = "python {root}/build_cmd.py {install}"
tools = []

uuid = "repository.suitey"

version = "houd"

def commands():    
    env.PATH.append("/home/jgerber/suites/{version}/bin")
