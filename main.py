from tabulate import tabulate

from library import *
import os


r = Auth()

kutubxona = Kutubxona()

kutubxona.load_books()

user = Foydalanuvchi.from_json(
    {
        "fullname": "said said said o'g'li",
        "email": "saidnur@gmail.com",
        "username": "nasimxonov",
        "password": "12312saidddd",
        "rented_books": [
            {"nom": "Najot ta'lim python darslik", "muallif": {"ism": "Abdurazzoq", "familiya": "Abdusalomov"}, "janr": "O'quv qo'llanma", "narx": 50000, "sahifalar": 80},
            {"nom": "etst", "muallif": {"ism": "asd", "familiya": "ffff"}, "janr": "O'quv qo'llanma", "narx": 50000, "sahifalar": 80},
        ],
    }
)


while True:
    action = input("Login uchun 'l' yoki Ro'yxatdan o'tish uchun 'r' ni kiriting: ").lower()

    if action == "l":
        username = input("Login uchun Username: ")
        password = input("Login uchun Password: ")

        user = r.login(username, password)

        if user:
            print("Tizimga kirish muvaffaqiyatli.")

            break
        else:
            print("Login yoki parol noto'g'ri.")

    elif action == "r":

        fullname = input("Fullname: ")
        email = input("Email: ")
        username = input("Username: ")
        password = input("Password: ")

        r.register(fullname, email, username, password)

        print("Registratsiya muvaffaqiyatli bo'ldi. Qayta login qiling!")

    else:
        print("Noto'g'ri tanlov.")

def xizmatlar_royxati():
    print("\nXizmatlar ro'yxati:\n")
    print("1. Kitob qo'shish")
    print("2. Kitoblar ro'yxatini ko'rish")
    print("3. Kitob olish")
    print("4. Olingan kitoblarni ko'rish")
    print("5. Olingan kitobni qaytarish")
    print("6. Tizimdan chiqish")

while True:
    xizmatlar_royxati()

    xizmat_raqami = input("\nTanlang: Xizmat raqamini kiriting: ")

    os.system("cls" if os.name == "nt" else "clear")

    if xizmat_raqami == "1":
        yangi_kitob = Kitob(input("Kitob nomi: "), Muallif(*input("Muallif ism va familiya: ").split()), input("Janr: "), int(input("Narxi: ")), int(input("Sahifalar")))

        kutubxona.kitob_qoshish(yangi_kitob)

    elif xizmat_raqami == "2":

        kitoblar_malumotlari = [[index + 1, kitob.nom, kitob.muallif.ism + " " + kitob.muallif.familiya, kitob.narx, kitob.sahifalar] for index, kitob in enumerate(kutubxona.kitoblar)]

        print("\nKitoblar ro'yxati:\n")
        print(tabulate(kitoblar_malumotlari, headers=["№", "Nomi", "Muallif", "Narx", "Sahifalar"], tablefmt="grid"))

    elif xizmat_raqami == "3":

        kitoblar_malumotlari = [[index + 1, kitob.nom, kitob.muallif.ism + " " + kitob.muallif.familiya, kitob.narx, kitob.sahifalar] for index, kitob in enumerate(kutubxona.kitoblar)]
        print("\nKitoblar ro'yxati:\n")
        print(tabulate(kitoblar_malumotlari, headers=["№", "Nomi", "Muallif", "Narx", "Sahifalar"], tablefmt="grid"))

        kitob_raqami = int(input("Tanlang: Kitob raqamini kiriting: ")) - 1

        if 0 <= kitob_raqami < len(kutubxona.kitoblar):
            tanlangan_kitob = kutubxona.kitoblar[kitob_raqami]
            print("\nTanlangan kitob:")
            print(tanlangan_kitob)

            user.kitob_qarzga_ol(tanlangan_kitob)

            r.save_data()
        else:
            print("Noto'g'ri raqam kiritildi.")

    elif xizmat_raqami == "4":
        kitoblar_malumotlari = [[index + 1, kitob.nom, kitob.muallif.ism + " " + kitob.muallif.familiya, kitob.narx, kitob.sahifalar] for index, kitob in enumerate(user.rented_books)]
        print("\nKitoblar ro'yxati:\n")
        print(tabulate(kitoblar_malumotlari, headers=["№", "Nomi", "Muallif", "Narx", "Sahifalar"], tablefmt="grid"))


    elif xizmat_raqami == "5":
        kitoblar_malumotlari = [[index + 1, kitob.nom, kitob.muallif.ism + " " + kitob.muallif.familiya, kitob.narx, kitob.sahifalar] for index, kitob in enumerate(user.rented_books)]
        print("\nKitoblar ro'yxati:\n")
        print(tabulate(kitoblar_malumotlari, headers=["№", "Nomi", "Muallif", "Narx", "Sahifalar"], tablefmt="grid"))
        
        kitob_raqami = int(input("Tanlang: Kitob raqamini kiriting: ")) - 1
        
        if 0 <= kitob_raqami < len(kutubxona.kitoblar):
            tanlangan_kitob = kutubxona.kitoblar[kitob_raqami]
            print("\nTanlangan kitob:")
            print(tanlangan_kitob)

            user.kitob_qaytar(tanlangan_kitob)

            r.save_data()
        else:
            print("Noto'g'ri raqam kiritildi.")


    elif xizmat_raqami == "6":
        break

    else:
        print("Noto'g'ri tanlov.")

    input("\nDavom etish uchun enterni bosing ")
    os.system("cls" if os.name == "nt" else "clear")
