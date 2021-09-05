import mysql.connector as mysqlconnector
import sys
print("Enter the choise(only for 2018 scheme):\n1.SGPA\n2.CGPA\n3.Exit")
n=input("\nYour choise:")
if (n==1):
    #calculate sgpa
    print("Enter your semester:")
    sem=int(input())
    if(sem>9|sem==0):
        print("Plese check your semester")
    else:
        connextion={"host":"localhost"
                                      "user":"root"
                                      "password":"iloveyoumom"
                                      "database":"courier"}
        con=mysql.connector.connect(**connextion)
        cursor=con.cursor()
        sql="""select * from courier"""
        cursor.execute(sql)

        
        for sem in range(1,8):
            print(sem)
elif(n==2):
    #calculate cgpa
    print("Enter Your semester:")
    add=0
    sem=int(input())
    if(sem>9|sem==0):
        print("Plese check your semester")
    else:
        for sem in range(1,8):
            print("Enter the "+sem+" semester SGPA: ")
            add +=add
        print(add)
elif(n==3):
    sys.close()
else:
    print("Check your choise.")
