UserPercent = input ("What is your percentage in your exam")

UserPercent = int(UserPercent)

if UserPercent >= 90:
    print("You got an A grade")
elif UserPercent >=70:
    print("You got an B grade")
elif UserPercent >=50:
    print("You got an C grade")
elif UserPercent >= 40:
    print("You got a D grade")
elif UserPercent <40:
    print("You got no award")
