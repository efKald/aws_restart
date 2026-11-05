data = """ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//"""

secuencia = data.replace("ORIGIN", "").replace("//", "")


# caracter.isalpha() looks if sequence has a leter of the alphabet
secuencia_limpia = "".join(caracter for caracter in secuencia if caracter.isalpha())

secuencia_final = secuencia_limpia.upper() #upper to go uppercase.

print(secuencia_final)

# Separando usando Slicing (corte exacto de aminoácidos)
linsulin  = secuencia_final[0:24]   # Aminoácidos 1 al 24
binsulin  = secuencia_final[24:54]  # Aminoácidos 25 al 30
cinsulin  = secuencia_final[54:89]  # Aminoácidos 55 al 89
ainsulin  = secuencia_final[89:110] # Aminoácidos 90 al 110

# Imprimimos los resultados bien ordenados
print(f"L-insulin (Líder):  {linsulin}\n")
print(f"B-insulin (Chain B): {binsulin}\n")
print(f"C-insulin (Peptide C): {cinsulin}\n")
print(f"A-insulin (Chain A): {ainsulin}\n")

# Comprobación de longitud total: 24 + 30 + 35 + 21 = 110
print(f"Longitud total comprobada: {len(linsulin) + len(binsulin) + len(cinsulin) + len(ainsulin)} aminoácidos")