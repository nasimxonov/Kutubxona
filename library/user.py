import json

from .book import Kitob


class Foydalanuvchi:
    def __init__(self, fullname, username, email, password, rented_books=[]):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password

        self.rented_books: list[Kitob] = rented_books

        super().__init__()

    def __repr__(self):
        return f"Foydalanuvchi(ism='{self.ism}', familiya='{self.familiya}')"

    def kitob_qarzga_ol(self, kitob: Kitob):
        self.rented_books.append(kitob)
        print(f"{kitob.nom} kitobi qarzga olindi.")

    def kitob_qaytar(self, kitob):
        if kitob in self.rented_books:
           
            self.rented_books.remove(kitob)
            print(f"{kitob.nom} kitobini qaytardi.")
        else:
            print(f"{kitob.nom} kitobi qarzga olinmagan.")

    @staticmethod
    def from_json(data: dict):

        kitoblar: list[Kitob] = [Kitob.from_json(book) for book in data.pop("rented_books")]

        return Foydalanuvchi(rented_books = kitoblar, **data)

    def to_json(self):
        return {
            "fullname": self.fullname,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "rented_books": [book.to_json() for book in self.rented_books],
        }
