# --------------------------Multi-level Inheritance-------------------------


class Dad:
    football = 2

    def is_foot(self):
        return f'This guy can play football {self.football} out of 10'


class Son(Dad):
    singing = 5

    def is_sing(self):
        return f'This guy can sing {self.singing} out of 10'


class Grandson(Son):
    bkchodi = 9

    def is_bkchod(self):
        return f'this guy is bkchod {self.bkchodi} out of 10'


ks = Dad()
ds = Son()
hs = Grandson()

print(hs.is_bkchod())
print(ds.is_foot())
print(ks.is_foot())
