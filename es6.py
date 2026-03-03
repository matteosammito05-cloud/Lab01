n = int(input("Inserisci il lato della matrice: "))
col = [0]*n
row = []
for i in range(n):
    row.append(col.copy())

matrice=row

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            matrice[i][j] = 1
        elif i==0:
            matrice[i][j] = matrice[i][j-1]
        elif j==0:
            matrice[i][j] = matrice[i-1][j]
        else:
            matrice[i][j] = matrice[i-1][j] + matrice[i][j-1]
for r in matrice:
    print(r)