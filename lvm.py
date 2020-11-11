import os
def lvm():
    while True:
        os.system("clear")
        os.system("tput setaf 4")
        os.system("figlet -f slant -c LVM World") 
        os.system("tput setaf 7")
        print("""
[1]To check number of storage attached to the OS
[2] To create Physical Volume
[3] To view Physical Volume
[4] To create Volume Group
[5] To view Volume Group
[6] To create Logical Volume
[7] To view Logical Volume
[8] To format the LV
[9] go back to main menu
[10] Exit the program""")

        i = input("Enter your Choice :")
        if int(i) == 1:
            os.system("fdisk -l")
        elif int(i) == 2:
            pv1=input("Enter the name of storage 1:")
            pv2=input("Enter the name of storage 2:")
            os.system("pvcreate {}".format(pv1))
            os.system("pvcreate {}".format(pv2))
        elif int(i) == 3:
            pv=input("Enter the name of storage:")
            os.system("pvdisplay {}".format(pv))
        elif int(i) == 4:
            vg=input("Give name to the Volume Group:")
            pvn1=input("Enter the name of storage 1:")
            pvn2=input("Enter the name of Storage 2:")
            os.system("vgcreate {} {} {}".format(vg,pvn1,pvn2))
        elif int(i) == 5:
            vg1=input("Enter the name of Volume Group:")
            os.sytem("vgdisplay {}".format(vg1))
        elif int(i) == 6:
            size=input("Enter size for your Logical Volume:")
            lv=input("Give name to your Logical Volume:")
            vg2=input("Enter name of the Volume Group:")
            os.system("lvcreate --size{} --name{} {}".format(size,lv,vg2))
        elif int(i) == 7:
            os.system("lvdisplay")
        elif int(i) == 8:
            vg4=input("Enter the name of Volume Group:")
            lv2=input("Enter the name of Logical Volume:")
            os.system("mkfs.ext4  /dev{}{}".format(vg4,lv2))
        elif int(i) == 9:
            return i
        elif int(i) == 10:
            exit()
        else:
            print("This option doesn't support")
        input("\nPress Enter to try again...")
        os.system("clear")
