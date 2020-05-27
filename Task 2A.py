#Setup Variables
Area = 0
Length = 0
Breadth = 0
Height = 0 


Length = input ("Enter the Length")
Breadth = input ("Enter the Breadth")
Height = input ("Enter the Height")

Area = int(float(Length)) * int(float(Breadth)) * int(float(Height)) 

print("Area is {}".format(Area))