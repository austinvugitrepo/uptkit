import platform

key = "e" 
while key != "q":
    print("\033[2J\033[1;1H")
    os = platform.platform()
    print(os)
    key = input()


