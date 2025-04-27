def vypocitaj_obsah():
    return a * a


def vypocitaj_obvod():
    return 4 * a


a = abs(float(input("Zadaj stranu stvorca: ")))

print(f"Obsah tvojho stvorca je:  {vypocitaj_obsah()}")
print(f"Obvod tvojho stvorca je:  {vypocitaj_obvod()}")

input("Pre pokracovanie stlac ENTER")
