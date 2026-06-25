class Species:

    def __init__(self):
        self.name = 'race'
        self.darkvision = True
        self.speed = 30
        self.size = 'medium'
        self.proficiencies = []
        self.level = 1
        self.hp_bonus = 0
        self.features = []

    def display_features(self):
        for feature in self.features:
            title, description = feature
            print("--------------------------")
            print(f"{title}")
            print("--------------------------")
            print(f"{description}")
            print()

    def level_up(self):
        pass