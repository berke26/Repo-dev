x = input("Enter Your Name and Surname:")
import sys # hocam return ile çok uğraştım yazamadım bende sys modulunu 
i = 0      # import ederek bir çözüm buldum
while True:
    if(x== "Berke Ayorak"):
        print("Welcome")
        break
    else:
        print("Incorrect")
        x = input("Please Enter Your Name and Surname:")
        i += 1
        
        if (i == 3):
            print("Please Try Again!!!")
            break
a = "Berke Ayorak"
if (x == a):
    b = input("Please Enter Your Courses:").split()
    if (len(b)<3): 
        print("you failed the lesson")
        sys.exit()
    c = input ("Enter the course you want to exam:")
    sözlük = {"midterm":55,"final":38,"project":87}
    print(sözlük)
    listesözlük=list(sözlük.values())
    ortalama = listesözlük[0] * 0.3 + listesözlük[1]  * 0.5 + listesözlük[2] * 0.2
    if (ortalama >= 90):
        print("Your grade is AA")
    elif (ortalama >=70 and ortalama < 90 ):
        print("Your grade is BB")
    elif (ortalama >=50 and ortalama < 70 ):
        print("Your grade is CC")
    elif (ortalama >=30 and ortalama < 50):
        print("Your grade is DD")
    elif (ortalama < 30 ):
        print("Your grade is FF")
        print("you failed the lesson...")