"""SIMPLE CALCUlATOR PYTHON"""
__author__ = "morvn"

# Atur semua nilai menjadi 0
output = 0
num1 = ""
operasi = ""
num2 = ""

# Tanyakan angka berapa yang akan digunakan
num1 = input("Masukan Angka Pertama.....\n")
operasi = input("Masukan Operasi.....(+, -, *, /)\n")
num2 = input("Masukan Angka Kedua.....\n")

# Atur angka pertanyaan menjadi float,
# Dengan begitu itu akan memberikan jawaban yang benar
angka1 = float(num1)
angka2 = float(num2)

# Jika operasi telah dipilih maka lakukan

if operasi == '+':
    output = angka1 + angka2
if operasi == '-':
    output = angka1 - angka2
if operasi == '/':
    output = angka1 / angka2
if operasi == '*':
    output = angka1 * angka2
if operasi == '+' or operasi == '-' or operasi == '*' or operasi == '/':
    print('Hasil:' + str(output))
else:
    print('Operasi kamu tidak valid, coba lagi')