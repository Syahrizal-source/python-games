import random

welcome_message = "Welcome To EZAPY Games!!!"
ezapy_position = random.randint(1, 4)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input("masukkan nama mu: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4 

goa = goa_kosong.copy()
goa[ezapy_position -1] = "|0_0|"

print(f'''
Halo {nama_user}! Coba perhatikan goa dibawah ini  
{goa_kosong}
''')

pilihan_user = int(input("Menurut kamu di goa nomor berapa CUYPY berada? [1 / 2 / 3 / 4]: "))

confirm_answer = input(f"apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ")

if confirm_answer == "n":
    print("program dihentikan!")
    exit()
elif confirm_answer == "y":
    if pilihan_user == ezapy_position:
        print(f"\n{goa}\n\nSelamat Kamu Menang 🏆")
    else:
        print(f"\n{goa}\n\nUncchhh kamu kalah 🙊")
else:
    print("Silahkan ulangi programnya!")
    exit()