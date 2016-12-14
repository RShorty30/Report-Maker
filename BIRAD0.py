import random
from random import randint

findings = ["is a mass", "is an asymmetry", "are calcifications"]
side = ["right", "left"]
density = ["The breasts are almost entirely fatty.", "There are scattered areas of fibroglandular density.", "The breasts are heterogeneously dense.", "The breasts are extremely dense."]
clock = ["12:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00"]
depth = ["anterior", "middle", "posterior"]
views = ["CC", "MLO"]
study = "Bilateral Digital Screening Mammogram"
file = open("BIRADS0.txt", "w")
def comparison(n):
	n = randint(0,9)
	dates = []
	year = random.choice(range(2000, 2016))
	month = random.choice(range(1, 13))
	day = random.choice(range(1, 29))
	dates.append(str(month) + "/" + str(day) + "/" + str(year))
	for i in range(n-1):
		year -= 1
		month = random.choice(range(1, 13))
		day = random.choice(range(1, 29))
		dates.append(str(month) + "/" + str(day) + "/" + str(year))
	x = (', '.join(map(str, dates)))
	return x

for finding in findings:
	for s in side:
		for d in density:
			for c in clock:
				for deep in depth:
					for view in views:
						n = randint(0,9)
						y = comparison(n)
						if finding == "is an asymmetry":
							file.write(study + "\n")
							file.write("Comparison: " + y + "\n")
							file.write("Findings:\n")
							file.write(d + "\n")
							file.write("There " + finding + " seen only on the " + view + " view in the " + s + " breast at " + c + ", " + deep + " depth.\n")
							file.write("No other suspicious masses, asymmetries, or calcifications in either breast\n")
							file.write("IMPRESSION:\n BI-RADS 0. Incomplete. Additional evaluation needed\n\n")
						else:
							file.write(study + "\n")
							file.write("Comparison: " + y + "\n")
							file.write("Findings:\n")
							file.write(d + "\n")
							file.write("There " + finding +" in the " + s + " breast at " + c + ", " + deep + " depth.\n")
							file.write("No other suspicious masses, asymmetries, or calcifications in either breast\n")
							file.write("IMPRESSION:\n BI-RADS 0. Incomplete. Additional evaluation needed\n\n")
file.close
