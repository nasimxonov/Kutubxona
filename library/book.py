class Muallif:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def __repr__(self):
        return f"Muallif(ism='{self.ism}', familiya='{self.familiya}')"

    def to_json(self):
        return {"ism": self.ism, "familiya": self.familiya}


class Kitob:
    def __init__(self, nom, muallif, janr, narx, sahifalar):
        self.nom = nom
        self.muallif: Muallif = muallif
        self.janr = janr
        self.__narx = None
        self.sahifalar = sahifalar
        self.qarzga_olindi = False
        self.narx = narx

    @property
    def narx(self):
        return self.__narx

    @narx.setter
    def narx(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__narx = value
        else:
            raise ValueError("Narx musbat son bo'lishi kerak!")

    def __repr__(self):
        return f"Kitob(nom='{self.nom}', muallif={self.muallif}, " f"janr='{self.janr}', narx={self.narx}, sahifalar={self.sahifalar})"

    def to_json(self):
        return {"nom": self.nom, "muallif": self.muallif.to_json(), "janr": "O'quv qo'llanma", "narx": 50000, "sahifalar": 80}

    @staticmethod
    def from_json(data: dict):

        muallif: Muallif = Muallif(**data.pop("muallif"))

        return Kitob(muallif=muallif, **data)

    def __eq__(self, value: object) -> bool:
        return isinstance(value,Kitob) and self.nom == value.nom
