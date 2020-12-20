import os 
import subprocess

global instance_name , count , sg_name , sg_description , key_name , ebs_name , ebs_size
name="Name"


def menu():
    print("\t\t\tWelcome TO AWS...")

    new=input("Do you want to enter AWS Cloud (yes/no) ? ").lower()

    if new == "yes":
        check()
        while True:
            os.system("clear")
            print("\t\t\tWelcome TO AWS...")    
            print("1. To create key pair for EC2 instance.")
            print("2. To create security Group for EC2 instance.")
            print("3. To launch instance on AWS with Amazon Linux.")
            print("4. To describe EC2 instances on AWS.")
            print("5. To stop/terminate an EC2 instance.")
            print("6. To create Volume to create EBS volume.(limit 10GB).")
            print("7. To attach the EBS volume to EC2 instance.")
            print("8. TO enter into S3 section.")
            print("9. To exit.")
    
        
            x = int(input("Enter your choice: "))
            
            if x==1:
                key_name = input("Enter Key Name: ")
                os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
                print("Success security key created : {} ".format(key_name ))
                input("press Enter to continue...")
            

            elif x==2:
                sg_name=input("Enter your security group name: ")
                sg_description=input("Enter your security group description: ")
                os.system("aws ec2 create-security-group --group-name {} --description {} --vpc-id vpc-e11afa8a ".format(sg_name,sg_description))
                print("Success security group created: {} , description: {}".format(sg_name , sg_description))
                input("press Enter to continue...")
            
            elif x==3:
                #name = 0
                #score = input("Enter your Instance Name")
                #instance_name = {}
                #instance_name[name] = score
                instance_name=input("Enter instance name:")
                count=int(input("Enter instance count: "))
                key_name = input("Enter Key Name: ")
                sg_name=input("Enter your security group name: ")
                print(instance_name[0])
                os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name {0} --security-groups {1} --count {2} ".format(key_name,sg_name,count,))
                instance_id=input("Enter Instance id : ")
                os.system("aws ec2 create-tags --resources {} --tags  Key=Name,Value={}".format(instance_id,instance_name))
                #os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --key-name p --security-groups p --count 1 --tag-specifications ResourceType=instance,Tags=[{{Key=Name,Value={}}}]".format(instance_name[0]))


            

            elif x==4:
                print("1.To describe all instance: \n2.To enter instance name: ")
                o=int(input())
                
                if o==1:
                    os.system("aws ec2 describe-instances")
                    input("press Enter to continue...")
                
                else:
                    name=input("Enter instance name: ")
                    os.system("aws ec2 describe-instances --filters Name=tag:Name,Values={}".format(name))
                    input("press Enter to continue...")

            elif x==5:
                print("1.To stop an instance : \n2.To terminate an instance: ")
                o=int(input())

                if o==1:
                    Iid=input("Enter the instance id of EC2 instance you want to stop: ")
                    os.system("aws ec2 stop-instances --instance-ids {}".format(Iid))
                    input("press Enter to continue...")
                else:
                    Iid=input("Enter the instance id of EC2 instance you want to terminate: ")
                    os.system("aws ec2 stop-terminates --instance-ids {}".format(Iid))
                    input("press Enter to continue...")

            elif x==6:
                ebs_name=input("Enter your EBS name: ")
                ebs_size=int(input("Enter your EBS size in GB: "))
                os.system("aws ec2 create-volume --availability-zone ap-south-1a --size {}".format(ebs_size))
                ebs_id=input("Enter EBS volume id: ")
                os.system("aws ec2 create-tags --resources {} --tags  Key=Name,Value={}".format(ebs_id,ebs_name))
                input("press Enter to continue...")
                    
            elif x==7:
                Iid=input("Enter the instance id of EC2 instance: ")
                volid=input("Enter the EBS volume id: ")
                os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(volid,Iid))
                input("press Enter to continue...")
                        
            elif x==8:
                    o=int(input("1.To create S3 bucket\n2. To delete S3 bucket\n3. To list all S3 bucket.\n4. To copy a file to S3 bucket"))
                    if o==1:
                        bkName=input("Enter unique bucket name: ")
                        os.system("aws s3 mb s3://{}".format(bkName))
                        input("press Enter to continue...")
                    elif o==2:
                        bkName=input("Enter unique bucket name: ")
                        os.system("aws s3 rb --force s3://{}".format(bkName))
                        input("press Enter to continue...")
                    elif o==3:
                        os.system("aws s3 ls: ")
                        input("press Enter to continue...")
                    elif o==4:   
                        bkName=input("Enter unique bucket name: ")
                        fname=input("Enter file name: ")
                        os.system("aws s3 cp {} s3://{}",fname,bkName)
                        input("press Enter to continue...")


            else:
                break
        
    else:
        print("Exiting...")
        
        


def check():
        
        print("Checking for AWS CLI tools")
        x = subprocess.getstatusoutput("aws --version")
        if x[0] != 0 :
            x =input("AWS CLI is not installed! do you want to install (yes/no)?").lower
            if x =="yes":
                os.system(" curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip")
                os.system("unzip awscliv2.zip")
                os.system("sudo ./aws/install")
                check()
            else:
                print("AWS can't run")
                os.system("exit()")
        else:
            print("Configure AWS CLI ! ")
            os.system("aws configure")



menu()

                    
                    
                    
                    #  elif x==:
                    #os.system("aws ec2 authorize-security-group-ingress  --group-name  --protocol tcp --port 22  --cidr ")
