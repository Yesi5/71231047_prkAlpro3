print("Program Menampilkan Jumlah Hari dalam Satu Bulan Tahun 2020")

while True:
  try:
    bulan = int(input("Masukkan bulan (1-12): "))
    if bulan < 1 or bulan > 12:
      print("Bulan tidak valid!")
      continue
    
    hari31 = [1, 3, 5, 7, 8, 10, 12]
    hari30 = [4, 6, 9, 11]

    if bulan in hari31:
      print("Jumlah hari: 31")
    elif bulan in hari30:    
      print("Jumlah hari: 30")
    else:
      print("Jumlah hari: 29")
      break

  except ValueError:
    print("Input harus berupa angka bulan (1-12)!")
  
print("Program selesai.")