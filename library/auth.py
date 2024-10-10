import json
from abc import ABC, abstractmethod
from .user import Foydalanuvchi


class AbstractAuth(ABC):

    def __init__(self):
        self.users: list[Foydalanuvchi] = [Foydalanuvchi.from_json(data) for data in self.load_data()]

    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def register(self, fullname, email, username, password):
        pass

    def load_data(self):
        """Fayldan ma'lumotlarni yuklab oladi."""
        try:
            with open("db/users.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        """Faylga ma'lumotlarni saqlaydi."""

        raw_user = [user.to_json() for user in self.users]

        with open("db/users.json", "w") as f:
            json.dump(raw_user, f, indent=4)


class Auth(AbstractAuth):

    def __init__(self, fullname=None, email=None, username=None, password=None):
        super().__init__()

        if fullname and email and username and password:
            self.register(fullname, email, username, password)

    def login(self, username, password):
        """Tizimga kirish."""
        for user in self.users:

            if user.username == username and user.password == password:
                print(f"{username} tizimga kirdi.")

                return user

        print("Username yoki parol xato! Ro'yxatdan o'tishingiz kerak.")

        return None

    def register(self, fullname, email, username, password):
        """Foydalanuvchini ro'yxatdan o'tkazish."""

        if self.is_user_exists(fullname, email, username):
            raise Exception("Bu foydalanuvchi allaqachon ro'yxatga olingan!")

        self.check_name(fullname)
        self.check_email(email)
        self.check_username(username)
        self.check_password(password)

        self.users.append(Foydalanuvchi.from_json({"fullname": fullname, "email": email, "username": username, "password": password, "rented_books": []}))

        self.save_data()

        print("Ro'yxatdan o'tish muvaffaqiyatli amalga oshirildi!")

    def logout(self):
        print("Tizimdan chiqildi !!!")

    def register_auto(self, username, password):
        """Avtomatik ro'yxatdan o'tkazish."""
        fullname = input("Fullname kiriting: ")
        email = input("Email kiriting: ")
        new_password = input("Yangi parol kiriting: ")

        return self.register(fullname, email, username, new_password)

    def is_user_exists(self, fullname, email, username):
        """Foydalanuvchi allaqachon mavjudligini tekshiradi."""
        for user in self.users:
            if user.fullname == fullname or user.email == email or user.username == username:
                return True
        return False

    def check_name(self, new_name: str):
        """Ismni to'g'ri kirilganini tekshirish."""
        if len(new_name.split()) != 4:
            raise Exception("Name Error! Iltimos F.I.Sh ni to'liq kiriting!")

        if not new_name.islower():
            raise Exception("F.I.Sh kichik harf bilan boshlanishi kerak!")

        assert new_name.endswith("o'g'li") or new_name.endswith("qizi"), "F.I.Sh qizi yoki o'g'li bilan tugashi kerak"

    def check_email(self, new_email: str):
        """E-mailni to'g'riligini tekshirish."""
        assert "@" in new_email, "@ belgisi bo'lishi kerak!"
        local_part = new_email[: new_email.find("@")]
        assert len(local_part) >= 5, "E-mail uzunligi '@' gacha kamida 5 ta belgi bo'lishi kerak"
        assert new_email.endswith(".com") or new_email.endswith(".ru"), "E-mail '.ru' yoki '.com' bilan tugashi kerak"

    def check_username(self, username: str):
        """Username to'g'ri kiritilganligini tekshirish."""
        assert len(username) >= 5, "Username uzunligi kamida 5 ta bo'lishi kerak"
        assert username.isalnum(), "Username faqat raqam va harflardan iborat bo'lishi kerak"

    def check_password(self, password: str):
        """Parol qoidalarini tekshirish."""
        assert len(password) >= 8, "Parol uzunligi kamida 8 ta belgi bo'lishi kerak"
        assert any(i.isdigit() for i in password), "Parolda kamida bitta raqam bo'lishi kerak"
        assert any(i.isalpha() for i in password), "Parolda kamida bitta harf bo'lishi kerak"
        assert all(i.isalnum() for i in password), "Parol faqat raqam va harflardan iborat bo'lishi kerak"
