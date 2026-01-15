import platform

key = "e" 
while key != "q":
    os = platform.platform()
    print(os)
    key = input("Welcome to Ultra Portable Toolkit (UPTKIT)! Press q to quit, otherwise press any key to continue:")
    if key == "q":
        print("exited sucessfully.")
        exit()
    else:
        system = platform.system()
        print(system)



        

