print("Data Awal :")
dictA = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689"
    }
for key, val in dictA.items():
    print("%s : %s" % (key, val))

print("\n")

dictA["Jane Doe"]= "+27 555 1024"

print("Data Baru : ")
dictA.update({"Anna Cooper": "+27 555 3237"})
for key, val in dictA.items():
    print("%s : %s" % (key, val))

print("\n")

print("Cetak Nomor Telepon Bob :")
print(dictA["Bob Stone"])

print("\n")

print("Cetak Semua Key Dari Dictionary :")
print(sorted(dictA.keys()))

print("\n")

print ("Cetak Semua Value Dari Dictionary :")
print(sorted(dictA.values()))
