
def menu(string):
    print(f"\033[1;32m{string}\033[0m")

def output(string):
    print(f"\033[0;34m{string}\033[0m")

def get_input(string):
    return input(f"\033[4m{string}\033[0m")

