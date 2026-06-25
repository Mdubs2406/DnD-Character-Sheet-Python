from file_io import readlines, writelines

class Iventory:

    def __init__(self, filename: str):
        self.is_stored_at = filename
        self.all = readlines(self.is_stored_at)
        self.items = []
        self.coins = (0,0,0,0,0)

    def manage_money(self, amount):
        cp, sp, ep, gp, pp = self.coins
        total = 0.01*cp + 0.1*sp + 0.5*ep + 1*gp + 10*pp
        


header1 = 'Copper, Sliver, Electrum, Gold, Platnum'
header2 = 'Name, (# number of), Weight, Cost'
header3 = 'Name, attunement (Y/N), descritpion'