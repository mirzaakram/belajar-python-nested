#nested
max = int(input("jumlah bintang: "))
for i in range(max):
    for s in range(i):
        print(" ", end=" ")
    for j in range(max - i):
        print("*", end=" ")
    print()

#belajar berhitung
a = int(input("masukkan angka pertama: "))
b = int(input("masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

match operator:
    case "+":
        hasil = a + b
        print(f"Hasil dari {a} + {b} = {hasil}")
    case "-":
        hasil = a - b
        print(f"Hasil dari {a} - {b} = {hasil}")
    case "*":
        hasil = a * b
        print(f"Hasil dari {a} * {b} = {hasil}")
    case "/":
        if b != 0:
            hasil = a / b
            print(f"Hasil dari {a} / {b} = {hasil}")
        else:
            print("error: pembagian dengan nol tidak bisa")
    case _:
        print("Operator tidak dikenal!")