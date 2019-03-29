spisok, spisok2, spisok3 = [], [], []
while True:
	chislo = input()
	if chislo == 'end':
		break
	spisok.append(chislo.split())
if spisok != []:
	for j in spisok:
		spisok2.append([int(i) for i in j])
	lenfull, lenstr =  len(spisok2), len(spisok2[0])
	spisok3 = [[0 for kl in range(lenstr)] for km in range(lenfull)]
	for q in range(0, lenfull):
		for o in range(0, lenstr):
			spisok3[q][o] = spisok2[(q - 1) % lenfull][o] + spisok2[(q + 1) % lenfull][o] +  spisok2[q][(o - 1) % lenstr] + spisok2[q][(o + 1) % lenstr]
	for jm in range(lenfull):
		print(*spisok3[jm])
