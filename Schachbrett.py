nx = 1
ny = 1
nx = int(input("Gib die Anzahl der Zeilen ein: "))
ny = int(input("Gib die Anzahl der Spalten ein: "))
for x in range(1, nx + 1):
    for y in range(1, ny + 1):
        if (y + x) % 2 == 0:
            print("O", end=" ")
        else:
            print("X", end=" ")
    print("")