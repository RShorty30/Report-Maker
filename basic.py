findings = ["is a mass", "is an asymmetry", "are calcifications"]
side = ["right", "left"]
density = ["The breasts are almost entirely fatty.", "There are scattered areas of fibroglandular density.", "The breasts are heterogeneously dense.", "The breasts are extremely dense."]
clock = ["12:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00"]
depth = ["anterior", "middle", "posterior"]
views = ["CC", "MLO"]
study = "Bilateral Digital Screening Mammogram"
file = open("BIRADS0.txt", "w")

for finding in findings:
		for s in side:
			for d in density:
				for c in clock:
					for deep in depth:
						for view in views:
							if finding == "is an asymmetry":
								file.write(study + "\n")
								file.write("Findings:\n")
								file.write(d + "\n")
								file.write("There " + finding + " seen only on the " + view + " view in the " + s + " breast at " + c + ", " + deep + " depth.\n")
								file.write("No other suspicious masses, asymmetries, or calcifications in either breast\n")
								file.write("IMPRESSION:\n BI-RADS 0. Incomplete. Additional evaluation needed\n\n")
							else:
								file.write(study + "\n")
								file.write("Findings:\n")
								file.write(d + "\n")
								file.write("There " + finding +" in the " + s + " breast at " + c + ", " + deep + " depth.\n")
								file.write("No other suspicious masses, asymmetries, or calcifications in either breast\n")
								file.write("IMPRESSION:\n BI-RADS 0. Incomplete. Additional evaluation needed\n\n")
file.close
