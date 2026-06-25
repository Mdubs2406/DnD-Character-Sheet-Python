from dice import Dice


class DnD_Class:

    def __init__(self):
        self.name = 'hero'
        self.saving_throws = []
        self.prof_options = []
        self.proficiencies = self.select_profs(0)
        self.expertise = self.select_expert(0)
        self.hit_dice = Dice(0)
        self.level = 1
        self.training = []
        self.tools =[]
        self.full_caster = True
        self.half_caster = False
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

    def select_profs(self,k):
        print(f"Level 1: You gain proficiency in {k} skills from the following:")
        skill_lst = []
        lst = self.prof_options.copy()
        i = 1
        t = 1
        while t <= k: 
            for item in lst:
                print(f"{i}) {item}")
                i += 1
            i = 1
            chosen_num = int(input(f"Input the number of one skill you would like. You can choose {k-t} more after this one: "))
            skill_lst.append(lst[chosen_num-1])
            print("You have chosen proficiency in the following skills:")
            for item in skill_lst:
                print(f"*{item}*")
            lst.remove(lst[chosen_num-1])
            print()
            t += 1
        return  skill_lst

    def select_expert(self,k):
        print(f"Level 1: You gain Expertise in {k} of your skill proficiencies of your choice.")
        expert_lst = []
        lst = self.proficiencies.copy()
        i=1
        t=1
        while t <= k: 
            for item in lst:
                print(f"{i}) {item}")
                i += 1
            i = 1
            chosen_num = int(input(f"Input the number of one skill you would like. You can choose {k-t} more after this one."))
            expert_lst.append(lst[chosen_num-1])
            print("You have chosen expertise in the following skills:")
            for item in expert_lst:
                print(f"*{item}*")
            lst.remove(lst[chosen_num-1])
            print()
            t += 1
        return expert_lst

class Rouge(DnD_Class):
    
    def __init__(self):
        self.name = 'Rogue'
        self.saving_throws = ['dex', 'int']
        self.prof_options = ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Persuasion', 'Sleight of Hand', 'Stealth']
        self.hit_dice = Dice(8)
        self.training = ['Simple Weapons','Martial weapons with the Finesse or Light property','']
        self.tools =["Theives' Tools"]
        self.proficiencies = self.select_profs(4)
        self.expertise = self.select_expert(2)
        self.features = []
        self.full_caster = False
        self.half_caster = False
        self.features = []