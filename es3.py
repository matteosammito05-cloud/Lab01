with open("input.txt", "r", encoding = "utf-8") as testo:
    ls=testo.readlines()

for l in ls:
    print(l, end="")

ls_inv=ls[::-1]
with open("output.txt", "w", encoding="utf-8") as testo_inv:
    testo_inv.writelines(ls_inv)

testo.close()
testo_inv.close()