# suhu = int(input("Masukkan suhu tubuh: "))
# if suhu >= 38:
#     print("Anda demam")
# else:
#     print("Anda tidak demam")

while True:
    try:
      suhu = float(input("Masukkan suhu tubuh: "))
      break

    except ValueError:
        print("Inputharus berupa angka. Coba lagi")
    
if suhu >= 38:
    print("Anda demam")
else:
    print("Anda tidak demam")

    