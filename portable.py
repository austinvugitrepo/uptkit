import platform
import shutil
import time

key = "e" 
while key != "q":
    os = platform.platform() #entire OS stack
    print(os)
    key = input("Welcome to Ultra Portable Toolkit (UPTKIT)! Press q to quit, otherwise press any key to continue:")
    if key == "q":
        print("exited sucessfully.")
        exit()
    else:
        system = platform.system()
        if system == "Linux":
            for i in ['apt', 'dnf', 'apk', 'pacman', 'emerge']:
                if shutil.which(i):
                    print(i)

        elif system == "OpenBSD":
            if shutil.which("pkg_add"):
                print("This system uses pkg_add")
        elif system == "Darwin":
            if shutil.which("brew"):
                print("this system uses brew")

        elif system == "Windows":
            if shutil.which("winget"):
                print("this system uses winget")
        time.sleep(0.5) #in seconds
        print("\033[2J\033[1;1H")





        

