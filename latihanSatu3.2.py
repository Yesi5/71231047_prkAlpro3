while True:
  try:
    bilangan = float(input("Masukkan suatu bilangan: "))
    break
  except ValueError:
    print("Input harus berupa angka. Silakan coba lagi.")

if bilangan > 0:
  print("Positif")
elif bilangan < 0:
  print("Negatif")  
elif bilangan == 0:
  print("Nol")