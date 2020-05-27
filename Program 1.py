MathsScore = 0
EnglishScore = 0
ComputingScore = 0
Average = 0


MathsScore = input ("Enter Maths Score")
EnglishScore = input ("Enter English Score")
ComputingScore = input ("Enter Computing Score")
Average= int(float(MathsScore)) + int(float(EnglishScore)) + int(float(ComputingScore))
Average = Average /3

print("Average is {}".format(Average))