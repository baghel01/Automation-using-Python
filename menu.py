import os
import getpass
import socket
import subprocess
import lvm as lv
import aws as a

os.system("clear")
#os.system("yum install figlet -y")
#os.system("clear")
os.system("tput setaf 4")
os.system("figlet -f slant -c MENU ProGram") 
os.system("tput setaf 1")
print("\t\t\tHey welcome to my menu program")
os.system("tput setaf 7")

print("\t\t\t==============================")

print("where you would like to perform your job (local/remote) :" , end='')
location = input()

if location == "remote":
    remoteIp = input("Enter your IP : ")
    try:
      socket.inet_aton(remoteIp)
      print("Valid IP")
      live=subprocess.getstatusoutput("ping {0} -c 2".format(remoteIp))
      if live[0] == 0:
        userName = input("Enter your remote user name : ")
        userPass = getpass.getpass("Enter your remote password : ")
      else:
        print("remote ip is not live")
    except socket.error:
      print("Invalid IP")
print("What you want to do about menu!")
while True:
    os.system("tput setaf 4")
    os.system("figlet -f slant -c MENU ProGram")
    os.system("tput setaf 7")
    print("""
    press 1: you want to configure yum or docker
    press 2: you want use docker
    press 3: you want to use hadoop
    press 4: you want to use webserver
    press 5: you want to create new user
    press 6: you want to do partion
    press 7: you want to run linux commands
    press 8: To enter AWS CLOUD
    press q: To exit
    """)

    print("Enter your choice:" , end="")
    ch=input()
    print(ch)
    if location == "local":
        if ch == "1":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c ConFigure MENU")
              os.system("tput setaf 7")
              print("[1]configure yum\n[2]configure docker\n[3]go back to main menu\n[4]exit the program")
              d = int(input("Please Enter your choice what u want to configure : "))
              if d == 1: #("yum" in d) and ("configure" in d):
                os.system("touch /etc/yum.repos.d/menuyum.repo")
                os.system(" cat yum.repo >> /etc/yum.repos.d/menuyum.repo")
                os.system("systemctl enable docker")
              elif d == 2: #("docker" in d) and ("configure" in d):
                #os.system("touch /etc/yum.repos.d/menudocker.repo")
                os.system("touch /etc/yum.repos.d/menudocker.repo")
                os.system("cat docker.repo >> /etc/yum.repos.d/menudocker.repo") 
              elif d ==3: #("go" in d) or ("back" in d) and ("menu" in d):
                break
              elif d == 4:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")  
        elif ch == "2":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c Docker MENU")
              os.system("tput setaf 7")
              print("""[1]install docker\n[2]launch new container\n[3]start docker\n[4]Show running containers\n[5]show all containers either stop or running\n[6]download docker image\n[7]show all images\n[8]go back to main menu\n[9]exit the program
              """)
              print("What you want to do in docker?", end='\n')
              d = int(input("Enter your choice: "))
              if d == 1: #("docker" in d) and ("install" in d):
                os.system("yum install docker-ce --nobest")
                os.system("systemctl enable docker")
              elif d == 2: #("run" in d) and ("docker" in d):
                dname = input("Give OS name : ")
                os.system("docker run -it --name {0} centos:latest".format(dname))
              elif d == 3: #("start" in d) and ("docker" in d):
                os.system("systemctl start docker ")
              elif d == 4: # ("status" in d) and ("running" in d):
                os.system("docker ps ")
              elif d == 5: #("status" in d) and ("all" in d):
                os.system("docker ps -a")
              elif d == 6 : #("detail" in d):
                dpull == input("Enter docker image name : ")
                os.system("docker pull {0} ".format(dpull))
              elif d == 7: #("copy" in d) and ("os" in d):
                os.system("docker images") 
              elif d == 8: #("go" in d) and ("menu" in d):
                break
              elif d == 9:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")  
        elif ch == "3":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c hadoop MENU")
              os.system("tput setaf 7")
              print("Where you want to go in hadoop?", end='\n')
              print("""[1]Go to namenode terminal\n[2]Go to datanode terminal\n[3]Go to hadoop client terminal\n[4]Go back to main menu\n[5]exit the program
              """)
              hd = int(input("Enter your choice : "))
              if hd == 1:
                while True:
                  os.system("clear")
                  os.system("tput setaf 6")
                  os.system("figlet -f slant -c Namenode")
                  os.system("tput setaf 7")
                  print("""[1] install hadoop \t[2] Namenode setup file \t[3] start  \t[4] start permanent\n[5]remove directory \t[6] report of hdfs        \t[7]stop firewall\t[8]show all files of hdfs\n[9] load files on hdfs \t[10] delete file from hdfs \t[11] read file\t[12] Fix block size on loading \n[13] safemode on \t[14] safemode off         \t[15] Go back
              """)
                  lnd = int(input("Please Enter your choice : "))
                  if lnd == 1: #("hadoop" in d) and ("install" in d):
                    lnjdkFile = input("Enter path name of jdk software whereit present in your local system : ")
                    lnjdk = subprocess.getstatusoutput("ls {0} | grep jdk".format(lnjdkFile)) 
                    os.system("rpm -ivh {0} ".format(lnjdk[1]))
                    javaVersion = input("do you want to check jdk is successfully installed or not (y/n) :")
                    if javaVersion == "y":
                      os.system("java -version")
                    lnhadoopFile = input("Enter full path name of hadoop software where it is present in your system : ")
                    lnhadoop = subprocess.getstatusoutput("ls {0} | grep hadoop".format(lnhadoopFile)) 
                    os.system("rpm -ivh {0} --force".format(lnhadoop[1]))
                    print("Are you want to check hadoop is  successfully installed or not (y/n) : ")
                    ans = input()
                    if ans == "y":
                      os.system("hadoop version")
                  elif lnd == 2 : #( "namenode" in d) or ("masternode" in d) and ("setup" in d):
                #nameIp = input("Enter ip address of namenode : ")
                    namePort = input("Enter port number on which namenode binding hdfs : ")
                    os.system("cat coren1.txt >> /etc/hadoop/core-site.xml")
                    os.system("echo '<value>hdfs://0.0.0.0:{0}</value> ' >> /etc/hadoop/core-site.xml".format(namePort))
                    os.system(" cat coren2.txt >> /etc/hadoop/hdfs-site.xml")
                ##############namenode coref-site.xml############
                    nameDir = input("Enter directory name for creating directory to be made hdfs file system in namenode : ")
                    os.system("cat hdfsn1.txt >> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<value>/{0}</value>' >> /etc/hadoop/hdfs-site.xml".format(nameDir))
                    os.system("cat coren2.txt >> /etc/hadoop/hdfs-site.xml")
             
                    formatAns = input("Do you want to format namenode : ")
                    if formatAns == "y":
                      os.system("hadoop namenode -format")
                  elif  lnd == 3: #("start" in d) and ("namenode" in d):
                    os.system("hadoop-daemon.sh start namenode")
                    jpsNameCheck = input("Do you want to see namenode start or not (y/n) : ")
                    if jpsNameCheck == "y":
                      os.system("jps")
                  elif lnd == 4:  #("start" in d) and ("namenode" in d) and ("permanent" in d):
                    os.system("echo ' ' >> /etc/rc.d/rc.local")
                    os.system("echo ' hadoop daemon.sh start namenode' >> /etc/rc.d/rc.local")
                    os.system("chmod +x /etc/rc.d/rc.local")
                  elif lnd == 5:  #("delete" in d) or ("remove" in d) and ("local" in d) and ("directory" in d):
                    localDir = input("Enter the directory name :")
                    os.system("rm -rvf {0} ")
                  elif lnd ==6: #("report" in d):
                    os.system("hadoop dfsadmin -report")
                  elif lnd == 7:  #("firewalld" in d) or ("firewall" in d) and ("stop" in d):
                    os.system("systemctl stop firewalld")
                  elif lnd == 8: #("all" in d) and ("files" in d):
                     fsDir = input("Enter directory name")
                     os.system("hadoop fs -ls /{0}".format(fsDir))
                  elif lnd == 9: #("load" in d) and ("file" in d):
                    loadFile = input("Enter file name which you want to load: ")
                    loadDir = input("Enter directory name where you want to load")
                    os.system("hadoop fs -put {0} {1}".format(loadFile,loadDir))
                  elif lnd == 10: #("remove" in d ) or ("delete" in d) and ("hdfs" in d):
                    remFile = input("Enter file name with full path name : ")
                    os.system("hadoop fs -rm {0}".format(remFile))
                  elif lnd == 11:  #("read" in d) and ("file" in d):
                    readFile = input("Enter file name with location : ")
                    os.system("hadoop fs -cat {0} ".format(readFile))
                  elif lnd == 12 : #("block" in d) and ("size" in d):
                    blockSize = int(input("Enter block size in bytes which you want to give :"))
                    blockFile = input("Enter file name which you want to upload :")
                    blockDir = input("Enter the directory name in which you want to upload : ")
                    os.system("hadoop fs -Ddfs.block.size={0} -put {1} {2} ".format(blockSize,blockFile,blockDir))
                  elif lnd == 13: #("safemode" in d) and ("on" in d):
                    os.system("hadoop dfsadmin -safemode get")
                  elif lnd == 14: #("safemode" in d) and ("off" in d):
                    os.system("hadoop dfsadmin -safemode leave")
                  elif lnd == 15: #("go" in d) ("back" in d ) and ("menu" in d):
                    break
                  else:
                    print("This option don't support")
                  input("Press Enter to try again...")
                  os.system("clear")
                print ("Good bye!") 
               ###########namenode hdfs-site.xml################ 
              elif hd == 2:
                while True:
                  os.system("clear")
                  os.system("tput setaf 6")
                  os.system("figlet -f slant -c Datanode MENU")
                  os.system("tput setaf 7")
                  print("""[1] install hadoop \t[2] Datanode setup file \t[3] start \t[4] stop \t[5] report of hdfs
[6]remove local directory \t[7]see current directry locaaly \t[8]download hdfs file \t[9]show all files of hdfs \t[10] delete hdfs directory \t[11] upload files on hdfs \t[12] delete file from hdfs \t[13] read file \t[14] Fix block size on loading\t[15] help \t[16] create a file \t[17] Go back
              """)
                  d = int(input("Please Enter your choice : "))
                  if d == 1: #("hadoop" in d) and ("install" in d):
                    ldjdkFile = input("Enter path name of jdk software whereit present in your local system : ")
                    ldjdk = subprocess.getstatusoutput("ls {0} | grep jdk".format(ldjdkFile)) 
                    os.system("rpm -ivh {0} ".format(ldjdk[1]))
                    javaVersion = input("do you want to check jdk is successfully installed or not (y/n) :")
                    if javaVersion == "y":
                      os.system("java -version")
                    ldhadoopFile = input("Enter full path name of hadoop software where it is present in your system : ")
                    ldhadoop = subprocess.getstatusoutput("ls {0} | grep hadoop".format(ldhadoopFile)) 
                    os.system("rpm -ivh {0} --force".format(ldhadoop[1]))
                    print("Are you want to check hadoop is  successfully installed or not (y/n) : ")
                    ans = input()
                    if ans == "y":
                      os.system("hadoop version")
                  elif d == 2: #( "datanode" in d) or ("slavenode" in d) and ("setup" in d):
                    nameIp = input("Enter ip address of namenode : ")
                    namePort = input("Enter port number on which namenode binding hdfs : ")
                    dataDir = input("Enter directory name for creating directory to be shared datanode : ")
                    os.system("mkdir /{0}".format(dataDir))
                    os.system("cat cored1.txt >> /etc/hadoop/core-site.xml")
                    
                    os.system("echo '<value>hdfs://{0}:{1}</value> ' >> /etc/hadoop/core-site.xml".format(nameIp,namePort))
                    os.system("cat coren2.txt >> /etc/hadoop/hdfs-site.xml")
                    
                ####datanode core-site.xml###########################
                    os.system("cat hdfsd1.txt >> /etc/hadoop/hdfs-site.xml")
                    
                    os.system("echo '<value>/{0}</value>' >> /etc/hadoop/hdfs-site.xml".format(dataDir))
                    os.system("cat coren2.txt >> /etc/hadoop/hdfs-site.xml")
                   
                ########datanode hdfs-site.xml##########################
                  elif d == 3: #("start" in d) and ("datanode" in d):
                    os.system("hadoop-daemon.sh start datanode")
                    jpsDataCheck = input("Do you want to see datanode start or not (y/n) : ")
                    if jpsDataCheck == "y":
                      os.system("jps")
                  elif d == 4: #("stop" in d) and ("datanode" in d):
                    os.system("hadoop-daemon.sh stop datanode")
                  elif d == 5: #("report" in d):
                    os.system("hadoop dfsadmin -report")
                  elif d == 6: #("delete" in d) or ("remove" in d) and ("local" in d) and ("directory" in d):
                    localDataDir = input("Enter the Directory name :")
                    os.system("rm -rvf {0} ".format(locaDataDir))
                  elif d == 7: #("current" in d) and ("directory" in d):
                    os.system("pwd")
                  elif d == 8: #("download" in d) and ("file" in d):
                    hadoopFile = input("Enter hadoop file file name : ")
                    savedLocalDir = input("Enter the name of local directory where you want to save it : ")
                    os.system("hadoop fs -get {0} {1}".format(hadoopFile,saveLocalDir))
                  elif d == 9: #("all" in d) and ("files" in d):
                    fsDir = input("Enter directory name")
                    os.system("hadoop fs -ls /{0}".format(fsDir))
                  elif d == 10: #("delete" in d) and ("hadoop" in d) and ("directory" in d):
                    hadoopDir = input("Enter the hadoop directroy to be deleted :")
                    os.system("hadoop fs -rmr {0} ".format(hadoopDir))
                  elif d == 11: #("load" in d) and ("file" in d):
                    loadFile = input("Enter file name which you want to load: ")
                    loadDir = input("Enter directory name where you want to load")
                    os.system("hadoop fs -put {0} {1}".format(loadFile,loadDir))
                  elif d == 12: #("remove" in d ) or ("delete" in d) and ("hdfs" in d):
                    remFile = input("Enter file name with full path name : ")
                    os.system("hadoop fs -rm {0}".format(remFile))
                  elif d == 13:  #("read" in d) and ("file" in d):
                    readFile = input("Enter file name with location : ")
                    os.system("hadoop fs -cat {0} ".format(readFile))
                  elif d == 14 : #("block" in d) and ("size" in d):
                    blockSize = int(input("Enter block size in bytes which you want to give :"))
                    blockFile = input("Enter file name which you want to upload :")
                    blockDir = input("Enter the directory name in which you want to upload : ")
                    os.system("hadoop fs -Ddfs.block.size={0} -put {1} {2} ".format(blockSize,blockFile,blockDir))
                #os.system("hadoop fs -touchz /filename")
                  elif d == 15: #("help" in d) or ("-h" in d):
                    help = input("Enter hadoop command : ")
                    os.system("hadoop fs -help {0}".format(help))
                  elif d == 16: # ("create" in d) or ("open" in d) and ("file" in d):
                    print("for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
                    dataFileName = input("enter file name : ")
                    os.system("vim {0}".format(dataFileName))
                  elif d == 17: #("go" in d) ("back" in d ) and ("menu" in d):
                    break
                  else:
                    print("This option don't support")
                  input("Press Enter to try again...")
                  os.system("clear")
                print ("Good bye!")
              elif hd == 3:
                while True:
                  os.system("clear")
                  os.system("tput setaf 6")
                  os.system("figlet -f slant -c hadoop Client")
                  os.system("tput setaf 7")
                  print("""
                  [1] install hadoop \t[2] hadoop client setup file\t[3] Block size fix set up in file\t[4] replication factor set up \t[5] make a local direcory \t[6] report of hdfs\t[7]remove local directory  \t [8]see current directry localy \t[9]download hdfs file \t[10]show all files of hdfs \[11] delete hdfs directory \t[12] upload files on hdfs \t[13] delete file from hdfs \t[14] read file \t[15] Fix block size on loading\t[16] help \t[17] create a file \[18] Go back
              """)
                  d = int(input("Please Enter your choice : "))
                  if d == 1: #("hadoop" in d) and ("install" in d):
                    ldjdkFile = input("Enter path name of jdk software whereit present in your local system : ")
                    ldjdk = subprocess.getstatusoutput("ls {0} | grep jdk".format(ldjdkFile)) 
                    os.system("rpm -ivh {0} ".format(ldjdk[1]))
                    javaVersion = input("do you want to check jdk is successfully installed or not (y/n) :")
                    if javaVersion == "y":
                      os.system("java -version")
                    ldhadoopFile = input("Enter full path name of hadoop software where it is present in your system : ")
                    ldhadoop = subprocess.getstatusoutput("ls {0} | grep hadoop".format(ldhadoopFile)) 
                    os.system("rpm -ivh {0} --force".format(ldhadoop[1]))
                    print("Are you want to check hadoop is  successfully installed or not (y/n) : ")
                    ans = input()
                    if ans == "y":
                      os.system("hadoop version")
                  elif d == 2: #( "datanode" in d) or ("slavenode" in d) and ("setup" in d):
                    nameIp = input("Enter ip address of namenode : ")
                    namePort = input("Enter port number on which namenode binding hdfs : ")
                    dataDir = input("Enter directory name for creating directory to be shared datanode : ")
                    os.system("mkdir /{0}".format(dataDir))
                    os.system("cat cored1.txt >> /etc/hadoop/core-site.xml")
                    
                    os.system("echo '<value>hdfs://{0}:{1}</value> ' >> /etc/hadoop/core-site.xml".format(nameIp,namePort))
                    os.system("cat coren2.txt >> /etc/hadoop/core-site.xml")
                  elif d == 3: #("current" in d) and ("directory" in d):
                    lcblockSize = int(input("Enter block size to be fixed on client : "))
                    os.system("echo '<property>'>> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<name>dfs.block.size</name>'>> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<value>{0}</value>'>> /etc/hadoop/hdfs-site.xml".format(lcblockSize))
                    os.system("echo '</property>'>> /etc/hadoop/hdfs-site.xml")
                  elif d == 4: #("current" in d) and ("directory" in d):
                    lcreplication = int(input("Enter replication factor : "))  
                    os.system("echo '<property>'>> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<name>dfs.replication</name>'>> /etc/hadoop/hdfs-site.xml")
                    os.system("echo '<value>2</value>'>> /etc/hadoop/hdfs-site.xml".format(lcreplication))
                    os.system("echo '</property>'>> /etc/hadoop/hdfs-site.xml")
                ####hadoop client core-site.xml###########################
                  elif d == 5: #("current" in d) and ("directory" in d):
                    cDir = input("Enter directory name : ")
                    os.system("mkdir {0}".format(cDir))
                  elif d == 6: #("report" in d):
                    os.system("hadoop dfsadmin -report")
                  elif d == 7: #("delete" in d) or ("remove" in d) and ("local" in d) and ("directory" in d):
                    localDataDir = input("Enter the Directory name :")
                    os.system("rm -rvf {0} ".format(locaDataDir))
                  elif d == 8: #("current" in d) and ("directory" in d):
                    os.system("pwd")
                  elif d == 9: #("download" in d) and ("file" in d):
                    hadoopFile = input("Enter hadoop file file name : ")
                    savedLocalDir = input("Enter the name of local directory where you want to save it : ")
                    os.system("hadoop fs -get {0} {1}".format(hadoopFile,saveLocalDir))
                  elif d == 10: #("all" in d) and ("files" in d):
                    fsDir = input("Enter directory name")
                    os.system("hadoop fs -ls /{0}".format(fsDir))
                  elif d == 11: #("delete" in d) and ("hadoop" in d) and ("directory" in d):
                    hadoopDir = input("Enter the hadoop directroy to be deleted :")
                    os.system("hadoop fs -rmr {0} ".format(hadoopDir))
                  elif d == 12: #("load" in d) and ("file" in d):
                    loadFile = input("Enter file name which you want to load: ")
                    loadDir = input("Enter directory name where you want to load")
                    os.system("hadoop fs -put {0} {1}".format(loadFile,loadDir))
                  elif d == 13: #("remove" in d ) or ("delete" in d) and ("hdfs" in d):
                    remFile = input("Enter file name with full path name : ")
                    os.system("hadoop fs -rm {0}".format(remFile))
                  elif d == 14:  #("read" in d) and ("file" in d):
                    readFile = input("Enter file name with location : ")
                    os.system("hadoop fs -cat {0} ".format(readFile))
                  elif d == 15 : #("block" in d) and ("size" in d):
                    blockSize = int(input("Enter block size in bytes which you want to give :"))
                    blockFile = input("Enter file name which you want to upload :")
                    blockDir = input("Enter the directory name in which you want to upload : ")
                    os.system("hadoop fs -Ddfs.block.size={0} -put {1} {2} ".format(blockSize,blockFile,blockDir))
                #os.system("hadoop fs -touchz /filename")
                  elif d == 16: #("help" in d) or ("-h" in d):
                    help = input("Enter hadoop command : ")
                    os.system("hadoop fs -help {0}".format(help))
                  elif d == 17: # ("create" in d) or ("open" in d) and ("file" in d):
                    print("for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
                    dataFileName = input("enter file name : ")
                    os.system("vim {0}".format(dataFileName))
                  elif d == 18: #("go" in d) ("back" in d ) and ("menu" in d):
                    break
                  else:
                    print("This option don't support")
                  input("Press Enter to try again...")
                  os.system("clear")
                print ("Good bye!")
              
              elif hd == 4:
                break
              elif hd == 5:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")  
        elif ch == "4":
             while True:
              os.system("clear")
              os.system("tput setaf 1")
              os.system("figlet -f slant -c Webserver MENU")
              os.system("tput setaf 7")
              print("What you want to do in webserver?", end='\n')
              print("""[1]install webserver\n[2] start webserver\n[3] check status\n[4] stop webserver\n[5] show current directory \n[6] create or open a file\n[7] copy a file on webserver\n[8] Go back \n[9] exit the program
              """)
              d = int(input("Please Enter your choice : "))
              if d == 1: #("webserver" in d) and ("install" in d):
                os.system("yum install httpd")
              elif d ==2:
                os.system("systemctl start httpd")
              elif d == 3: #("status webserver" in d):
                os.system("systemctl status httpd")
              elif d == 4: #("stop webserver" in d):
                os.system("systemctl stop httpd")
              elif d == 5: #("directory" in d):
                os.system("pwd")
                os.system("ls")
              elif d == 6: #("create" in d) or ("open" in d) and ("file" in d):
                print("for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
                webFileName = input("enter file name : ")
                os.system("vim {0}".format(webFileName))
              elif d == 7: #("copy" in d ) and ("file" in d):
                file = input("file name")
                os.system("cp {0} /var/www/html".format(webFileName))
              elif d == 8: # ("go" in d) and ("menu" in d):
                break
              elif d == 9:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
             print ("Good bye!")  
        elif ch == "5":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c User MENU")
              os.system("tput setaf 7")
              print("""[1] create user \n[2] create password for a user \n[3] Go to main menu \n[4] exit the program
              """)
              d = int(input("Enter your choice :"))
              if d == 1:
                print("please give username:" , end='')
                createUser = input()
                os.system("useradd {}".format(createUser))
              elif d == 2:
                os.system("passwd {0} ".format(creatUser))
              elif d == 3:
                break
              elif d == 4:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")
        elif ch == "6":
          while True:
            os.system("clear")
            os.system(lv.lvm())
            os.system("clear")
            break
        elif ch == "7":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c Linux MENU")
              os.system("tput setaf 7")
              print("""
[1] run linux command\t[2] help\t[3] go to main menu\t[4] exit the program
              """)
              ch =int(input("Enter your choice : "))
              if ch == 1:
                linuxCommand = input("Enter the command : ")
                os.system("{0}".format(linuxCommand))
              elif ch == 2: #("help" in d) or ("h" in d):
                os.system(" {0} --help".format(linuxCommand))
              elif ch == 3: #("go" in d) and ("menu" in d):
                break
              elif ch == 4:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")
        elif ch == "8":
          os.system("clear")
          os.system(a.menu())    
        elif ch == "q" or ch == "Q":
            exit()
        else:
            print("Option not supported")
        input("Press Enter to try again...")
        os.system("clear")
    elif location == "remote":
        if ch == "1":
            while True:
              os.system("tput setaf 6")
              os.system("figlet -f slant -c ConFigure MENU")
              os.system("tput setaf 7")
              print("""[1]configure yum\n[2]configure docker\n[3]go back to main menu\n[4]exit the program
              """)
              d = int(input("Please Enter your choice what u want to configure : "))
              if d == 1: #("yum" in d) and ("configure" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} touch /etc/yum.repos.d/menuyum.repo".format(userPass,userName,remoteIp))
                os.system("sshpass -p '{0}' ssh /cat yum.repo >> /etc/yum.repos.d/menuyum.repo".format(userPass,userName,remoteIp))
                os.system("sshpass -p '{0}' ssh {1}@{2} systemctl enable docker".format(userPass,userName,remoteIp))
              elif d == 2: #("docker" in d) and ("configure" in d):
                #os.system("touch /etc/yum.repos.d/menudocker.repo")
                os.system("sshpass -p '{0}' ssh {1}@{2} touch /etc/yum.repos.d/menudocker.repo".format(userPass,userName,remoteIp))
                os.system("shpass -p '{0}' ssh {1}@{2} cat /docker.repo >> /etc/yum.repos.d/menudocker.repo".format(userPass,userName,remoteIp)) 
              elif d ==3: #("go" in d) or ("back" in d) and ("menu" in d):
                break
              elif d == 4:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")  
            #os.system("ssh {0} systemctl enable docker ".format(remoteIp))
            #os.system("ssh {0} yum install docker-ce --nobest".format(remoteIp))
        elif ch == "2":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c Docker MENU")
              os.system("tput setaf 7")
              print("""[1] install docker\n[2] launch new container\n[3 start docker\n[4]Show running containers\n[5] show all containers either stop or running\n[6] download docker image\n[7] show all images\n[8]go back to main menu\n[9]exit the program
              """)
              print("What you want to do in docker?", end='\n')
              d = int(input("Enter your choice: "))
              if d == 1: #("docker" in d) and ("install" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} yum install docker-ce --nobest".format(userPass,userName,remoteIp))
                os.system("sshpass -p '{0}' ssh {1}@{2} systemctl enable docker".format(userPass,userName,remoteIp))
              elif d == 2: #("run" in d) and ("docker" in d):
                dname = input("Give OS name : ")
                os.system("sshpass -p '{0}' ssh {1}@{2} docker run -it --name {3} centos:latest".format(userPass,userName,remoteIp,dname))
              elif d == 3: #("start" in d) and ("docker" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} systemctl start docker ".format(userPass,userName,remoteIp))
              elif d == 4: # ("status" in d) and ("running" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} docker ps ".format(userPass,userName,remoteIp))
              elif d == 5: #("status" in d) and ("all" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} docker ps -a".format(userPass,userName,remoteIp))
              elif d == 6 : #("detail" in d):
                dpull == input("Enter docker image name : ")
                os.system("sshpass -p '{0}' ssh {1}@{2} docker pull {3} ".format(userPass,userName,remoteIp,dpull))
              elif d == 7: #("copy" in d) and ("os" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} docker images".format(userPass,userName,remoteIp)) 
              elif d == 8: #("go" in d) and ("menu" in d):
                break
              elif d == 9:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")  
            #os.system("ssh {0} cal".format(remoteIp))
        elif ch == "3":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c hadoop MENU")
              os.system("tput setaf 7")
              print("Where you want to go in hadoop?", end='\n')
              print("""[1] Go to namenode terminal\n[2] Go to datanode terminal\n[3] go to hadoop client terminal\n[4] send requirement files for hadoop file configuration for onetime setup\n[5] Go back to main menu\n[6] exit the program
              """)
              hd = int(input("Enter your choice : "))
              if hd == 1:
                while True:
                  os.system("clear")
                  os.system("tput setaf 6")
                  os.system("figlet -f slant -c Namenode MENU")
                  os.system("tput setaf 7")
                  print("""
                [1] install hadoop \t[2] Namenode setup file \t[3] start \t[4] start permanent \t [5]remove directory \t[6] report of hdfs \t [7]stop firewall \t[8]show all files of hdfs \[9] load files on hdfs \t[10] delete file from hdfs \t[11] read file \t[12] Fix block size on loading \[13] safemode on \t[14] safemode off \t [15] Go back
              """)
                  d = int(input("Please Enter your choice : "))
                  if d == 1: #("hadoop" in d) and ("install" in d):
                    rnjdkFile = input("Enter path name of jdk software whereit present in your remote system : ")
                    
                    rnjdk = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {3} | grep jdk".format(userPass,userName,remoteIp,rnjdkFile)) 
                       
                    os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} ".format(userPass,userName,remoteIp,rnjdk[1]))
                    javaVersion = input("do you want to check jdk is successfully installed or not (y/n) :")
                    if javaVersion == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} java -version".format(userPass,userName,remoteIp))
                    
                    rnhadoopFile = input("Enter full path name of hadoop software where it is present in your remote system : ")
                    rnhadoop = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {3} | grep hadoop".format(userPass,userName,remoteIp,rnhadoopFile)) 
                       
                    os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} --force".format(userPass,userName,remoteIp,rnhadoop[1]))
                    print("Are you want to check hadoop is  successfully installed or not (y/n) : ")
                    ans = input()
                    if ans == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop version".format(userPass,userName,remoteIp))
                  elif d == 2 : #( "namenode" in d) or ("masternode" in d) and ("setup" in d):
                #nameIp = input("Enter ip address of namenode : ")
                    namePort = input("Enter port number on which namenode binding hdfs : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} cat /coren1.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>hdfs://0.0.0.0:{3}</value> ' >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp,namePort))
                    os.system(" sshpass -p '{0}' ssh {1}@{2} cat /coren2.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
                ##############namenode coref-site.xml############
                    nameDir = input("Enter directory name for creating directory to be made hdfs file system in namenode : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} cat /hdfsn1.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>/{3}</value>' >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp,nameDir))
                    os.system("sshpass -p '{0}' ssh {1}@{2} cat /coren2.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
             
                    formatAns = input("Do you want to format namenode : ")
                    if formatAns == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop namenode -format".format(userPass,userName,remoteIp))
                  elif  d == 3: #("start" in d) and ("namenode" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop-daemon.sh start namenode".format(userPass,userName,remoteIp))
                    jpsNameCheck = input("Do you want to see namenode start or not (y/n) : ")
                    if jpsNameCheck == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} jps".format(userPass,userName,remoteIp))
                  elif d == 4:  #("start" in d) and ("namenode" in d) and ("permanent" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo ' ' >> /etc/rc.d/rc.local".format(userPass,userName,remoteIp))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo ' hadoop daemon.sh start namenode' >> /etc/rc.d/rc.local".format(userPass,userName,remoteIp))
                    os.system("sshpass -p '{0}' ssh {1}@{2} chmod +x /etc/rc.d/rc.local".format(userPass,userName,remoteIp))
                  elif d == 5:  #("delete" in d) or ("remove" in d) and ("local" in d) and ("directory" in d):
                    localDir = input("Enter the directory name :")
                    os.system("sshpass -p '{0}' ssh {1}@{2} rm -rvf {3} ".format(userPass,userName,remoteIp,localDir))
                  elif d ==6: #("report" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -report".format(userPass,userName,remoteIp))
                  
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop-daemon.sh stop namenode".format(userPass,userName,remoteIp))
                  elif d == 7:  #("firewalld" in d) or ("firewall" in d) and ("stop" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} systemctl stop firewalld".format(userPass,userName,remoteIp))
                  elif d == 8: #("all" in d) and ("files" in d):
                     fsDir = input("Enter directory name")
                     os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -ls /{3}".format(userPass,userName,remoteIp,fsDir))
                  elif d == 9: #("load" in d) and ("file" in d):
                    loadFile = input("Enter file name which you want to load: ")
                    loadDir = input("Enter directory name where you want to load")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -put {3} {4}".format(userPass,userName,remoteIp,loadFile,loadDir))
                  elif d == 10: #("remove" in d ) or ("delete" in d) and ("hdfs" in d):
                    remFile = input("Enter file name with full path name : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rm {3}".format(userPass,userName,remoteIp,remFile))
                  elif d == 11:  #("read" in d) and ("file" in d):
                    readFile = input("Enter file name with location : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -cat {3} ".format(userPass,userName,remoteIp,readFile))
                  elif d == 12 : #("block" in d) and ("size" in d):
                    blockSize = int(input("Enter block size in bytes which you want to give :"))
                    blockFile = input("Enter file name which you want to upload :")
                    blockDir = input("Enter the directory name in which you want to upload : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -Ddfs.block.size={3} -put {4} {5} ".format(userPass,userName,remoteIp,blockSize,blockFile,blockDir))
                  elif d == 13: #("safemode" in d) and ("on" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -safemode get".format(userPass,userName,remoteIp))
                  elif d == 14: #("safemode" in d) and ("off" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -safemode leave".format(userPass,userName,remoteIp))
                  elif d == 15: #("go" in d) ("back" in d ) and ("menu" in d):
                    break
                  else:
                    print("This option don't support")
                  input("Press Enter to try again...")
                  os.system("clear")
                print ("Good bye!") 
               ###########namenode hdfs-site.xml################ 
              elif hd == 2:
                while True:
                  os.system("clear")
                  os.system("tput setaf 6")
                  os.system("figlet -f slant -c Datanode MENU")
                  os.system("tput setaf 7")
                  print("""
[1] install hadoop \t[2] Datanode setup file \t[3] start \t[4] stop \t[5] report of hdfs\t[6]remove local directory  \t[7] see current directry locaaly \t[8]download hdfs file \t[9]show all files of hdfs \t[10] delete hdfs directory \t[11] upload files on hdfs \t[12] delete file from hdfs \t[13] read file \t[14] Fix block size on loading\t[15] help \t[16] create a file \t[17] Go back
              """)
                  d = int(input("Please Enter your choice : "))
                  if d == 1: #("hadoop" in d) and ("install" in d):
                 
                    rdjdkFile = input("Enter path name of jdk software whereit present in your remote system : ")
                    
                    rdjdk = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {3} | grep jdk".format(userPass,userName,remoteIp,rdjdkFile)) 
                       
                    os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} ".format(userPass,userName,remoteIp,rjddk[1]))   
                    
                    javaVersion = input("do you want to check jdk is successfully installed or not (y/n) :")
                    if javaVersion == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} java -version".format(userPass,userName,remoteIp))
                    rdhadoopFile = input("Enter full path name of hadoop software where it is present in your remote system : ")
                    rnhadoop = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {3} | grep hadoop".format(userPass,userName,remoteIp,rdhadoopFile))   
                    os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} --force".format(userPass,userName,remoteIp,rdhadoop[1]))   
                    print("Are you want to check hadoop is  successfully installed or not (y/n) : ")
                    ans = input()
                    if ans == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop version".format(userPass,userName,remoteIp))
                  elif d == 2: #( "datanode" in d) or ("slavenode" in d) and ("setup" in d):
                    nameIp = input("Enter ip address of namenode : ")
                    namePort = input("Enter port number on which namenode binding hdfs : ")
                    dataDir = input("Enter directory name for creating directory to be shared datanode : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} mkdir /{3}".format(userPass,userName,remoteIp,dataDir))
                    os.system("sshpass -p '{0}' ssh {1}@{2} cat /cored1.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
                    
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>hdfs://{3}:{4}</value> ' >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp,nameIp,namePort))
                    os.system("sshpass -p '{0}' ssh {1}@{2} cat /coren2.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                    
                ####datanode core-site.xml###########################
                    os.system("sshpass -p '{0}' ssh {1}@{2} cat /hdfsd1.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                    
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>/{3}</value>' >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp,dataDir))
                    os.system("sshpass -p '{0}' ssh {1}@{2} cat /coren2.txt >> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                    
                ########datanode hdfs-site.xml##########################
                  elif d == 3: #("start" in d) and ("datanode" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop-daemon.sh start datanode".format(userPass,userName,remoteIp,remoteIp))
                    jpsDataCheck = input("Do you want to see datanode start or not (y/n) : ")
                    if jpsDataCheck == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} jps".format(userPass,userName,remoteIp))
                  elif d == 4: #("stop" in d) and ("datanode" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop-daemon.sh stop datanode".format(userPass,userName,remoteIp))
                  elif d == 5: #("report" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -report".format(userPass,userName,remoteIp,remoteIp))
                  elif d == 6: #("delete" in d) or ("remove" in d) and ("local" in d) and ("directory" in d):
                    localDataDir = input("Enter the Directory name :")
                    os.system("sshpass -p '{0}' ssh {1}@{2} rm -rvf {3} ".format(userPass,userName,remoteIp,remoteIp,locaDataDir))
                  elif d == 7: #("current" in d) and ("directory" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} pwd".format(userPass,userName,remoteIp))
                  elif d == 8: #("download" in d) and ("file" in d):
                    hadoopFile = input("Enter hadoop file file name : ")
                    savedLocalDir = input("Enter the name of local directory where you want to save it : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -get {3} {4}".format(userPass,userName,remoteIp,hadoopFile,saveLocalDir))
                  elif d == 9: #("all" in d) and ("files" in d):
                    fsDir = input("Enter directory name")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -ls /{3}".format(userPass,userName,remoteIp,fsDir))
                  elif d == 10: #("delete" in d) and ("hadoop" in d) and ("directory" in d):
                    hadoopDir = input("Enter the hadoop directroy to be deleted :")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rmr {3} ".format(userPass,userName,remoteIp,hadoopDir))
                  elif d == 11: #("load" in d) and ("file" in d):
                    loadFile = input("Enter file name which you want to load: ")
                    loadDir = input("Enter directory name where you want to load")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -put {1} {2}".format(userPass,userName,remoteIp,loadFile,loadDir))
                  elif d == 12: #("remove" in d ) or ("delete" in d) and ("hdfs" in d):
                    remFile = input("Enter file name with full path name : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rm {3}".format(userPass,userName,remoteIp,remFile))
                  elif d == 13:  #("read" in d) and ("file" in d):
                    readFile = input("Enter file name with location : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -cat {3} ".format(userPass,userName,remoteIp,readFile))
                  elif d == 14 : #("block" in d) and ("size" in d):
                    blockSize = int(input("Enter block size in bytes which you want to give :"))
                    blockFile = input("Enter file name which you want to upload :")
                    blockDir = input("Enter the directory name in which you want to upload : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -Ddfs.block.size={1} -put {3} {4} ".format(userPass,userName,remoteIp,blockSize,blockFile,blockDir))
                #os.system("hadoop fs -touchz /filename")
                  elif d == 15: #("help" in d) or ("-h" in d):
                    help = input("Enter hadoop command : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -help {3}".format(userPass,userName,remoteIp,help))
                  elif d == 16: # ("create" in d) or ("open" in d) and ("file" in d):
                    print("for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
                    dataFileName = input("enter file name : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} vim {3}".format(userPass,userName,remoteIp,dataFileName))
                  elif d == 17: #("go" in d) ("back" in d ) and ("menu" in d):
                    break
                  else:
                    print("This option don't support")
                  input("Press Enter to try again...")
                  os.system("clear")
                print ("Good bye")
              elif hd == 3:
                while True:
                  os.system("clear")
                  os.system("tput setaf 6")
                  os.system("figlet -f slant -c hadoop Client")
                  os.system("tput setaf 7")
                  print("""
                  [1] install hadoop \t[2] hadoop client setup file\t[3] Block size fix set up in file\t[4] replication factor set up \t[5] make a remote direcory \t[6] report of hdfs\t[7]remove remote directory  \t [8]see current directry locally \t[9]download hdfs file \t[10]show all files of hdfs \[11] delete hdfs directory \t[12] upload files on hdfs \t[13] delete file from hdfs \t[14] read file \t[15] Fix block size on loading\t[16] help \t[17] create a file \[18] Go back
              """)
                  d = int(input("Please Enter your choice : "))
                  if d == 1: #("hadoop" in d) and ("install" in d):
                    ldjdkFile = input("Enter path name of jdk software whereit present in your local system : ")
                    ldjdk = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {0} | grep jdk".format(userPass,userName,remoteIp,ldjdkFile)) 
                    os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} ".format(userPass,userName,remoteIp,ldjdk[1]))
                    javaVersion = input("do you want to check jdk is successfully installed or not (y/n) :")
                    if javaVersion == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} java -version".format(userPass,userName,remoteIp))
                    ldhadoopFile = input("Enter full path name of hadoop software where it is present in your system : ")
                    ldhadoop = subprocess.getstatusoutput("sshpass -p '{0}' ssh {1}@{2} ls {4} | grep hadoop".format(userPass,userName,remoteIp,ldhadoopFile)) 
                    os.system("sshpass -p '{0}' ssh {1}@{2} rpm -ivh {3} --force".format(userPass,userName,remoteIp,ldhadoop[1]))
                    print("Are you want to check hadoop is  successfully installed or not (y/n) : ")
                    ans = input()
                    if ans == "y":
                      os.system("sshpass -p '{0}' ssh {1}@{2} hadoop version".format(userPass,userName,remoteIp))
                  elif d == 2: #( "datanode" in d) or ("slavenode" in d) and ("setup" in d):
                    nameIp = input("Enter ip address of namenode : ")
                    namePort = input("Enter port number on which namenode binding hdfs : ")
                    dataDir = input("Enter directory name for creating directory to be shared datanode : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} mkdir /{0}".format(userPass,userName,remoteIp,dataDir))
                    os.system("sshpass -p '{0}' ssh {1}@{2} /cat cored1.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
                    
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>hdfs://{3}:{4}</value> ' >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp,nameIp,namePort))
                    os.system("sshpass -p '{0}' ssh {1}@{2} /cat coren2.txt >> /etc/hadoop/core-site.xml".format(userPass,userName,remoteIp))
                  elif d == 3: #("current" in d) and ("directory" in d):
                    lcblockSize = int(input("Enter block size to be fixed on client : "))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<property>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<name>dfs.block.size</name>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>{3}</value>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp,lcblockSize))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '</property>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                  elif d == 4: #("current" in d) and ("directory" in d):
                    lcreplication = int(input("Enter replication factor : "))  
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<property>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                    os.system("sshpass -p '{0}' ssh {1}@{2} sshpass -p '{0}' ssh {1}@{2} echo '<name>dfs.replication</name>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '<value>{3}</value>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp,lcreplication))
                    os.system("sshpass -p '{0}' ssh {1}@{2} echo '</property>'>> /etc/hadoop/hdfs-site.xml".format(userPass,userName,remoteIp))
                ####hadoop client core-site.xml###########################
                  elif d == 5: #("current" in d) and ("directory" in d):
                    cDir = input("Enter directory name : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} mkdir {3}".format(userPass,userName,remoteIp,cDir))
                  elif d == 6: #("report" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop dfsadmin -report".format(userPass,userName,remoteIp))
                  elif d == 7: #("delete" in d) or ("remove" in d) and ("local" in d) and ("directory" in d):
                    localDataDir = input("Enter the Directory name :")
                    os.system("sshpass -p '{0}' ssh {1}@{2} rm -rvf {3} ".format(userPass,userName,remoteIp,locaDataDir))
                  elif d == 8: #("current" in d) and ("directory" in d):
                    os.system("sshpass -p '{0}' ssh {1}@{2} pwd".format(userPass,userName,remoteIp))
                  elif d == 9: #("download" in d) and ("file" in d):
                    hadoopFile = input("Enter hadoop file file name : ")
                    savedLocalDir = input("Enter the name of local directory where you want to save it : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -get {3} {4}".format(userPass,userName,remoteIp,hadoopFile,saveLocalDir))
                  elif d == 10: #("all" in d) and ("files" in d):
                    fsDir = input("Enter directory name")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -ls /{4}".format(userPass,userName,remoteIp,fsDir))
                  elif d == 11: #("delete" in d) and ("hadoop" in d) and ("directory" in d):
                    hadoopDir = input("Enter the hadoop directroy to be deleted :")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rmr {3} ".format(userPass,userName,remoteIp,hadoopDir))
                  elif d == 12: #("load" in d) and ("file" in d):
                    loadFile = input("Enter file name which you want to load: ")
                    loadDir = input("Enter directory name where you want to load")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -put {3} {4}".format(userPass,userName,remoteIp,loadFile,loadDir))
                  elif d == 13: #("remove" in d ) or ("delete" in d) and ("hdfs" in d):
                    remFile = input("Enter file name with full path name : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -rm {4}".format(userPass,userName,remoteIp,remFile))
                  elif d == 14:  #("read" in d) and ("file" in d):
                    readFile = input("Enter file name with location : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -cat {4} ".format(userPass,userName,remoteIp,readFile))
                  elif d == 15 : #("block" in d) and ("size" in d):
                    blockSize = int(input("Enter block size in bytes which you want to give :"))
                    blockFile = input("Enter file name which you want to upload :")
                    blockDir = input("Enter the directory name in which you want to upload : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -Ddfs.block.size={3} -put {4} {5} ".format(userPass,userName,remoteIp,blockSize,blockFile,blockDir))
                #os.system("hadoop fs -touchz /filename")
                  elif d == 16: #("help" in d) or ("-h" in d):
                    help = input("Enter hadoop command : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} hadoop fs -help {3}".format(userPass,userName,remoteIp,help))
                  elif d == 17: # ("create" in d) or ("open" in d) and ("file" in d):
                    print("for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
                    dataFileName = input("enter file name : ")
                    os.system("sshpass -p '{0}' ssh {1}@{2} vim {3}".format(userPass,userName,remoteIp,dataFileName))
                  elif d == 18: #("go" in d) ("back" in d ) and ("menu" in d):
                    break
                  else:
                    print("This option don't support")
                  input("Press Enter to try again...")
                  os.system("clear")
                print ("Good bye!")
              elif hd == 4:
                os.system("sshpass -p '{0}' scp  coren1.txt coren2.txt cored1.txt hdfsn1.txt hdfsd1.txt {1}@{2}:/ ".format(userPass,userName,remoteIp))
              elif hd == 5:
                break
              elif hd == 6:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")  
            #os.system("ssh {0} yum install httpd".format(remoteIp))
        elif ch == "4":
            while True:
              os.system("clear")
              os.system("tput setaf 1")
              os.system("figlet -f slant -c Webserver MENU")
              os.system("tput setaf 7")
              print("What you want to do in webserver?", end='\n')
              print("""[1] install webserver\n[2] stop webserver\n[3] show current directory \n[4] create or open a file\n[5] copy a file on webserver\n[6] Go back \n[7] exit the program
              """)
              d = int(input("Please Enter your choice : "))
              if d == 1: #("webserver" in d) and ("install" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} yum install httpd".format(userPass,userName,remoteIp))
              elif d == 2: #("stop webserver" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} systemctl stop httpd".format(userPass,userName,remoteIp))
              elif d == 3: #("directory" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} pwd".format(userPass,userName,remoteIp))
                os.system("sshpass -p '{0}' ssh {1}@{2} ls".format(userPass,userName,remoteIp))
              elif d == 4: #("create" in d) or ("open" in d) and ("file" in d):
                print("for writting anything in file press i  and for saving press esc key and :wq and only close file press esc key and :q")
                webFileName = input("enter file name : ")
                os.system("sshpass -p '{0}' ssh {1}@{2} vim {0}".format(userPass,userName,remoteIp,webFileName))
              elif d == 5: #("copy" in d ) and ("file" in d):
                file = input("file name")
                os.system("sshpass -p '{0}' ssh {1}@{2} cp {0} /var/www/html".format(userPass,userName,remoteIp,webFileName))
              elif d == 6: # ("go" in d) and ("menu" in d):
                break
              elif d == 7:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!") 
            #print("please give username:" , end='')
            #createUser = input()
            #os.system("ssh {0} useradd {1}".format(remoteIip,createUser))
        elif ch == "5":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c User MENU")
              os.system("tput setaf 7")
              print("""
              [1] create user \t[2] create password for a user \t[3] Go to main menu \t[4] exit the program
              """)
              d = int(input("Enter your choice :"))
              if d == 1:
                print("please give username:" , end='')
                createUser = input()
                os.system("sshpass -p '{0}' ssh {1}@{2} useradd {3}".format(userPass,userName,remoteIp,createUser))
              elif d == 2:
                os.system("sshpass -p '{0}' ssh {1}@{2} passwd {3} ".format(userPass,userName,remoteIp,creatUser))
              elif d == 3:
                break
              elif d == 4:
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")
             #os.system("ssh {0} touch abhi.txt".format(remoteIp))
        elif ch == "6":
            #os.system("ssh {0} date".format(remoteIp))
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c Partition MENU")
              os.system("tput setaf 7")
              print("What you want to do in partition?", end='\n')
              print("""[1] create a directory \n[2] create a partition \n[3] format partition \n[4] mount partion \n[5] permamnent mount \n[6] show hardisk \n[7] show partition \n[8] go to main menu \n[9] exit the program
              """)
              d = input("Please type here something to it : ")
              if int(d) == 1: #("create" in d) and ("directory" in d):
                partDir = input("Enter the direcory name which you want to create :")
                os.system("sshpass -p '{0}' ssh {1}@{2} mkdir {3}".format(userPass,userName,remoteIp,partDir))
              elif dint(d)== 2: #("create" in d) and ("partition" in d):
                partitionName = input("Give hardisk name : ")
                os.system("sshpass -p '{0}' ssh {1}@{2} fdisk {3} ".format(userPass,userName,remoteIp,partitionName)) #for creating partition
                os.system("sshpass -p '{0}' ssh {1}@{2} udevadm sttle".format(userPass,userName,remoteIp)) # for loading driver if any new partition created
              elif int(d) == 3: #("format" in d) and ("partion" in d):
                partName = input("Enter the partion name : ")
                os.system("sshpass -p '{0}' ssh {1}@{2} mkfs.ext4 {3}".format(userPass,userName,remoteIp,partName))
              elif int(d) == 4: #("mount" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} echo 'mount {3} {4}' >> /etc/rc.d/rc.local".format(userPass,userName,remoteIp,partName,partDir))
              elif int(d) == 5: #("mount" in d) and ("permanent" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} mount {3} {4}".format(userPass,userName,remoteIp,partName,partDir))
              elif int(d) == 6: #("show" in d) and ("hardisk" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} fdisk -l".format(userPass,userName,remoteIp))
              elif int(d) == 7: #("see" in d )or ("show" in d) and ("partition" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} lsblk".format(userPass,userName,remoteIp)) # show all block devices
              elif d == "b" or d == "B": #("go" in d) and ("menu" in d):
                break
              elif d == "q" or d == "Q":
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!") 
        elif ch == "7":
            while True:
              os.system("clear")
              os.system("tput setaf 6")
              os.system("figlet -f slant -c Linux MENU")
              os.system("tput setaf 7")
              print("""\n
[1] run linux command\t[2] help\t[3] go back to main menu\t[q] exit the program
              """)
              rcmd = input("Enter your choice : ")
              if int(rcmd) == 1:
                linuxCommand = input("Enter the command : ")
                os.system("sshpass -p '{0}' ssh {1}@{2} {3}".format(userPass,userName,remoteIp,linuxCommand))
              elif int(rcmd) == 2: #("help" in d) or ("h" in d):
                os.system("sshpass -p '{0}' ssh {1}@{2} {3} --help ".format(userPass,userName,remoteIp,linuxCommand))
              elif rcmd == "b" or rcmd == "B": #("go" in d) and ("menu" in d):
                break
              elif rcmd == "q" or rcmd == "Q":
                exit()
              else:
                print("This option don't support")
              input("Press Enter to try again...")
              os.system("clear")
            print ("Good bye!")
        
        elif ch == "q" or ch == "Q":
            exit()
        else:
            print("Option not supported")
        input("Press Enter to try again...")
        os.system("clear")
    else:
        print("location doesn't support")



