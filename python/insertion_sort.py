# Insertionsort Algorithmus

# String, der als Input genommen werden kann
inp = "4, 3, 2, 6, 1"
# Der String wird in eine Liste umgewandelt --> nums = [4, 3, 2, 6, 1]
nums = inp.split(", ")

# Das ist die Liste, mit den richtig sortierten Zahlen
# Am Anfang wird schon die letzte Zahla aus der `nums` Liste hinzugefügt
# Damit die weiteren Zahlen richtig einsortiert werden können
r = [nums[len(nums) - 1]]

print(nums)

for i in range(len(nums)):

    # Gebe den momentanen Zustand der Liste aus --> Zwischenergebnis
    print(r)

    # Die Zahl, die in die sortierte Liste hinzugefügt wird
    c = nums[i]

    # Prüfe ob die Zahl größer ist, als das letzte Element der sortierten Liste
    # Falls true, füge als letztes Element ein
    # Da es die größte Zahl momentan sein muss
    # continue; springt zum nächsten Element in der for Schleife
    if c > r[len(r) - 1]:
        r.append(c)
        continue

    # Wiederhole Länge von r mal
    for j in range(len(r)):
        # Falls die zu prüfende Zahl größer ist als das momentane Element der sortierten Liste, dann prüfe das nächste
        if c > r[j]:
            continue
        # Richtige Stelle in der sortierten Liste wurde gefunden
        # Füge die geprüfte Zahl `c` an Stelle `j` zur sortierten Liste hinzu und stoppe den Loop
        r.insert(j, c)
        break
