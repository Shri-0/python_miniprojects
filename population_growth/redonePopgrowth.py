currentPop = 380123456
secondsYear = 60*60*24*365

birthRate = 1/6
deathRate = 1/12
immigrationRate = 1/40

totalPop = currentPop

for i in range(3):
    birth = birthRate * secondsYear
    death = deathRate * secondsYear
    immi = immigrationRate * secondsYear

    net_change = birth - death + immi
    totalPop += net_change

print("The total population for three years is " + str(totalPop))
