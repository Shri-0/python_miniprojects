currentPopulation = 380123456

birthRate = 1/6
deathRate = 1/12
immigrationRate = 1/40

totalSecondsInAYear = 60*60*24*365

###########################################

totalPop = currentPopulation

for i in range(3):
	birth = birthRate * totalSecondsInAYear
	death = deathRate * totalSecondsInAYear
	immigration = immigrationRate * totalSecondsInAYear

	netChangetotal = birth - death + immigration
	totalPop += netChangetotal

print("The total Population after 3 years is " + str(totalPop))
