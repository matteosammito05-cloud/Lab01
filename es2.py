s1 = set(input("Inserisci la prima stringa: ").lower().strip().replace(" ", ""))
s2 = set(input("Inserisci la seconda stringa: ").lower().strip().replace(" ", ""))

et=s1&s2
print("Caratteri in entrambe le stringhe:", "".join(sorted(et)))

ot1=s1^s2
ot2=s2^s1
ot=ot1+ot2
print("Caratteri presenti in una ma non nell'altra:", "".join(sorted(ot)))

abc=set("abcdefghijklmnopqrstuvwxyz")
