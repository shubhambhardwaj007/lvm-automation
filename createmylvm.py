
import subprocess
def createmylv():
    print(subprocess.getoutput('lsblk'))
    device = input("Choose the devices for PV separated by space in between : ").split(" ")
    for i in device:
        pvcreate = subprocess.getstatusoutput("pvcreate {0}".format(i))
        if pvcreate[0] == 0:
            print("{0} pv created".format(i))
        else:
            print("{0} pv failed".format(i))

    vgname = input("Enter VG name: ")
    x= ' '.join(device)
    vgcreate = subprocess.getstatusoutput("vgcreate {0} {1}".format(vgname,x))
    
    lvname = input("Enter LV name: ")
    size = input("Enter Size of LV: ")
    lvcreate = subprocess.getstatusoutput("lvcreate --size {0} --name {1} {2}".format(size,lvname,vgname))
    mount = input("Enter the mountpoint: ")
    formating = subprocess.getstatusoutput("mkfs.ext4 /dev/{0}/{1}".format(vgname,lvname))
    mount_path = subprocess.getstatusoutput("mount /dev/{0}/{1} {2}".format(vgname,lvname,mount))
    if mount_path[0] == 0:
        print("Done")
    else:
        print("Can't mount")

        
createlv()
