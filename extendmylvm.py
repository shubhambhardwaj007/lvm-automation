import subprocess
def extendmylvm():
    dev = input("Enter the device path : ")
    size = input("Enter the size to be extended (8G) : ")
    lvextend = subprocess.getstatusoutput("lvextend --size +{0} {1}".format(size,dev))
    if lvextend[0] == 0:
        resize2fs_errorcode = subprocess.getstatusoutput("resize2fs {0}".format(dev))
        if resize2fs_errorcode[0] == 0:
            print("Done")
        else:
            print("resize2fs unsuccessful")
    else:
        print("lvextend unsuccessful")

extendlvm()
