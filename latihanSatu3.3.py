while True:
  try:
    a = float(input("Masukkan bilangan pertama: "))
    break
  except ValueError:
    print("Bilangan pertama harus angka. Coba lagi.")
    
while True:  
  try:
    b = float(input("Masukkan bilangan kedua: "))
    break
  except ValueError:
    print("Bilangan kedua harus angka. Coba lagi.")

while True:    
  try:
    c = float(input("Masukkan bilangan ketiga: "))
    break
  except ValueError:
    print("Bilangan ketiga harus angka. Coba lagi.")
    
if a > b and a > c:
  print("Terbesar: ", a)

elif b > a and b > c:
  print("Terbesar: ", b)
  
elif c > a and c > b:
  print("Terbesar: ", c)