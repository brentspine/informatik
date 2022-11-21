# Bubbelsort Algorithmus

# String, der als Input genommen werden kann
inp = "4, 3, 2, 6, 1"
# Der String wird in eine Liste umgewandelt --> nums = [4, 3, 2, 6, 1]
nums = inp.split(", ")

print(nums)

# Wiederhole Länge von Nummern - 1 mal
# Das heißt, so viele Schritte
for i in range(len(nums) - 1):
    # Wiederhole Länge von Nummern - 1 mal
    # Das heißt, überprüfe für jede Nummer, außer der Letzten
    for j in range(len(nums) - 1):
        # Falls Element an Stelle j größer ist als darauffolgende Stelle
        if nums[j] > nums[j + 1]:
            # Dann tausche die Stellen:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp

    # Nach jedem Schritt das Zwischenergebnis ausgeben
    print(nums)
