import platform
import shutil

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
        if system == "Linux":
            for i in ['apt', 'dnf', 'apk', 'pacman', 'emerge']:
                if shutil.which(i):
                    print(i)

        elif system == "OpenBSD":
            print("this is OpenBSD system")
        elif system == "Darwin":
            print("this is macOS system")
        elif system == "Windows":
            print("this is Windows system")




        

