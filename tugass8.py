data_praktikan = [
    ("2410432029", "Cia", 100, 95, 98),
    ("2410431029", "Merry", 70, 85, 95),
    ("2410433013", "Flora", 90, 95, 85),
    ("2410431010", "Mogan", 80, 55, 70),
    ("2410432015", "Yanzu", 85, 80, 75),
    ("2410432011", "Cery", 40, 80, 60),
    ("2410431019", "Kinan", 95, 90, 88),
    ("2410433001", "Hana", 75, 70, 80),
    ("2410433029", "Evan", 65, 60, 58),
    ("2410431011", "Leaa", 88, 84, 82)]

with open("data_pratikan.txt", "w") as file:
    for data in data_praktikan:
        nim, nama, pretest, postest, tugas = data
        file.write(f"{nim},{nama},{pretest},{postest},{tugas}\n")


praktikan = {}

with open("data_pratikan.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        nim = data[0]
        nama = data[1]
        pretest = int(data[2])
        postest = int(data[3])
        tugas = int(data[4])

        praktikan[nim] = {
            "nama": nama,
            "pretest": int(pretest),
            "postest": int(postest),
            "tugas": int(tugas)}

#----NILAI AKHIR----#       
with open("data_nilai_akhir.txt", "w") as file:
    file.write(" NIM , Nama , Pretest , Postest , Tugas , Nilai Akhir\n")
    for nim, data in praktikan.items():
        nilai_akhir = (0.35 * data["pretest"] + 0.35 * data["postest"] + 0.30 * data["tugas"])
        nilai_akhir = float(f"{nilai_akhir:.2f}")
        data["nilai_akhir"] = nilai_akhir
        file.write(f"{nim},{data['nama']},{data['pretest']},{data['postest']},{data['tugas']},{nilai_akhir}\n")
nilai_akhir_list = [data["nilai_akhir"] for data in praktikan.values()]

#----MAKSIMUM DAN MINIMUM----#
praktikan_tertinggi = None
praktikan_terendah = None

for nim, data in praktikan.items():
    if praktikan_tertinggi is None:
        praktikan_tertinggi = (nim, data)
    elif data["nilai_akhir"] > praktikan_tertinggi[1]["nilai_akhir"]:
        praktikan_tertinggi = (nim, data)

    if praktikan_terendah is None:
         praktikan_terendah = (nim, data)
    elif data["nilai_akhir"] < praktikan_terendah[1]["nilai_akhir"]:
        praktikan_terendah = (nim, data)


#----RATA RATA NILAI AKHIR----#
rata_rata = sum(nilai_akhir_list) / len(nilai_akhir_list)
rata_rata = float(f"{rata_rata:.2f}")

#----BANYAK PRAKTIKAN DENGAN NILAI DIBAWAH RATA RATA----#
jumlah_bawah_rata = 0

for data in praktikan.values():
    if data["nilai_akhir"] < rata_rata:
        jumlah_bawah_rata += 1

print(f"Nilai tertinggi praktikan: {praktikan_tertinggi[1]['nama']} ({praktikan_tertinggi[0]}) = {praktikan_tertinggi[1]['nilai_akhir']}")
print(f"Nilai terendah praktikan: {praktikan_terendah[1]['nama']} ({praktikan_terendah[0]}) = {praktikan_terendah[1]['nilai_akhir']}")
print(f"Rata-rata nilai akhir praktikan: {rata_rata}")
print(f"Banyak praktikan yang mendapat nilai di bawah rata-rata: {jumlah_bawah_rata}")


