spisok, spisok2 = [], []
while True:
	chislo = input()
	if chislo == 'end':
		break
	spisok.append(chislo.split())
for j in spisok:
	spisok2.append([int(i) for i in j])
lenfull, lenstr =  len(spisok2), len(spisok2[0])
