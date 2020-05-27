PupilName = ""
PupilAge = 0

PupilName = input ("What is your name")
PupilAge = input ("What is your age")

PupilAge = int(PupilAge)

if PupilAge >=4 and PupilAge <=11:
    print("You should be in primary school "+ PupilName)

if PupilAge >=12 and PupilAge <=17:
    print("You should be in High School " + PupilName)