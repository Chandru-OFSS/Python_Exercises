class MyFirstClass():
#Odd or Even
    def OddorEven():
        num1=int(input("Enter the Number: "))
        if num1%2==1:
            message="Odd"
        else:
            message="Even"
            print(message)
        return message

#Body Mass Index
    def BMI():
        BMI=int(input("Enter the BMI Index:"))
        if(BMI<=18):
        	print("Underweight")
        elif(BMI<=24):
        	print("Healthy")
        elif(BMI<=29):
        	print("Overweight")
        elif(BMI<=39):
        	print("Obese")
        else:
        	print("Extremely Obese")

#Marriage eligibility
    def CheckMarriageEligiblity():
        age=int(input("Enter the Age: "))
        gendr=input("Enter the Gender (M/F): ")
        print("Your Gender is: ", gendr.upper())
        print("Your Age is   : ", age)
        if ((gendr)=="F" and (age>18)):
            print("Eligible")
            message="Eligible"
        elif ((gendr) =="M" and (age>25)):
            print("Eligible")
            message="Eligible"
        elif gendr!="M" and gendr!="F": 
            message="Invalid Gender"
        else:
            message="Not Eligible"
        print(message)

#print area and perimeter of a triangle
    def GetAreaAndPerim():
        h1=int(input("Enter the height1: "))
        h2=int(input("Enter the height2: "))
        b=int(input("Enter the breadth: "))
        area=(h1*b)/2
        perim=(h1+h2+b)
        print("Height: ",h1)
        print("Breadth: ",b)
        print("Area of the Triangle is: ", area)
        print("Height1: ",h1)
        print("Height2: ",h2)
        print("Breadth: ",b)
        print("Perimeter of the Triangle is: ", perim)

    def subject():
        sub1=int(input("Enter marks for Subject1 = "))
        sub2=int(input("Enter marks for Subject2 = "))
        sub3=int(input("Enter marks for Subject3 = "))
        sub4=int(input("Enter marks for Subject4 = "))
        sub5=int(input("Enter marks for Subject5 = "))
        tot = sub1+sub2+sub3+sub4+sub5
        print ("Total = ",tot)
        print ("Percentage = ",tot/500*100)