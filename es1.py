word=input("Inserisci una parola: ").strip()
l=len(word)
for i in range(l):
    for f in range(i+1,l+1):
        print(word[i:f])