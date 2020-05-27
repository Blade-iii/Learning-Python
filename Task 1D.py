UserName = ""
UserAge = 0
UserColour = ""

UserName = input ("What is your name")
UserAge = input ("What is your age")
UserColour = input ("What is your favourite colour")

text1 = "Your name is {UserName} \n {UserName} is {UserAge} years old \n {UserName}`s favourite colour is {UserColour}.".format(UserName = UserName, UserAge = UserAge, UserColour = UserColour)

print(text1)