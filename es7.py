with open("promessi_sposi.txt", "r", encoding="utf-8") as testo:
    parole = testo.read()
    testo.close()

punt = '.,;:!?…–—"\''
for ch in punt:
    parole = parole.replace(ch, "")

parole = parole.lower().split()

word = input("Inserisci una parola: ").lower().strip()
volte = parole.count(word)
print(f"La parola '{word}' compare {volte} volte nel testo.")

frequenze = {}

for p in parole:
    if p in frequenze:
        frequenze[p] += 1
    else:
        frequenze[p] = 1

top = sorted(frequenze.items(), key=lambda x: x[1], reverse=True)

for parola, conteggio in top[:100]:
    print(parola, conteggio)