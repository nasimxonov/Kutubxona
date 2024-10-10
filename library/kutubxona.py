import json

from .book import Kitob, Muallif


class Kutubxona:
    def __init__(self):
        self.kitoblar: list[Kitob] = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)
        print(f"{kitob.nom} kitobi kutubxonaga qo'shildi.")

        self.save_books()

    def kitob_ochirish(self, kitob):
        if kitob in self.kitoblar:
            self.kitoblar.remove(kitob)
            print(f"{kitob.nom} kitobi kutubxonadan o'chirildi.")

            self.save_books()
        else:
            print(f"{kitob.nom} kitobi topilmadi.")

    def kitobni_qidirish(self, nom):
        for kitob in self.kitoblar:
            if kitob.nom.lower() == nom.lower():
                return kitob

        return None

    def kitoblar_royhati(self):
        if not self.kitoblar:
            print("Kutubxonada kitoblar mavjud emas.")
        else:
            print("Kutubxonadagi kitoblar:")
            for kitob in self.kitoblar:
                print(kitob)

    def load_books(self):
        with open("./db/books.json") as file:
            raw_bools = json.loads(file.read() or "[]")

            self.kitoblar = [Kitob(**{**book, "muallif": Muallif(**book["muallif"])}) for book in raw_bools]

    def save_books(self):

        data = [kitob.to_json() for kitob in self.kitoblar]

        with open("db/books.json", "w") as file:
            file.write(json.dumps(data, indent=4))
