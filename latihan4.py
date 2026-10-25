# Program Hitung Harga
# masukan harga : 
# 100000
# masukan persentase pajak (%) :
# 20
# Total harga =  120000


print("masukkan harga :")
p = int(input())
print("masukkan persentase pajak (%)")
pajak = int(input())
total = p + (p * pajak /100)
print(f"Total harga = {total:.2f}")
