import random
import json

races = ["Human" , "Dwarf" , 'Elf']
classes = ['Warrior' , "Mage" , 'Rogue']
genders = ['Male' , 'Female']

human_male_name = ['Noah' , 'Elijah' , 'Khai' , 'Wylder' , 'Kylian']
human_female_name = ['Emma' , 'Mia' , 'Ava' , 'Isla' , 'Violet']
human_last_name = ['Cunningham' , 'Simmons' , 'Webb' , 'Griffin' , 'Sierra']

dwarf_male_name = ['Rartion ' , 'Dugriol ' , 'Dagror ' , 'Dolvion ' , 'Ruvur']
dwarf_female_name = ['Drargola' , 'Rathira' , 'Dorthna' , 'Ginila' , 'Domana']
dwarf_last_name = ['Snowhood' , 'Orcjaw' , 'Whithelm' , 'Broadsunder' , 'Hardtoe']

elf_male_name = ['Aelfdene' , 'Aktaion' , 'Albion' , 'Dearborn' , 'Ellgar']
elf_female_name = ['Elvene' , 'Elwyn' , 'Eowyn' , 'Aubrey' , 'Morwyn']
elf_last_name = ['Amaadon' , 'Amastacia' , 'Araric' , 'Celebrimbor' , 'Celeborn']


def get_random_name_char(race , gender):
    name = ''

    if race == "Human" and gender == "Male":
        name = human_male_name[random.randint(0 , len(human_male_name) - 1)] \
               + " " + human_last_name[random.randint(0 , len(human_last_name) - 1)]

    if race == "Human" and gender == "Female":
        name = human_female_name[random.randint(0 , len(human_female_name) - 1)] \
               + " " + human_last_name[random.randint(0 , len(human_last_name) - 1)]

    if race == "Dwarf" and gender == "Male":
        name = dwarf_male_name[random.randint(0 , len(dwarf_male_name) - 1)] \
               + " " + dwarf_last_name[random.randint(0 , len(dwarf_last_name))]

    if race == "Dwarf" and gender == "Female":
        name = dwarf_female_name[random.randint(0 , len(dwarf_female_name) - 1)] \
               + " " + dwarf_last_name[random.randint(0 , len(dwarf_last_name))]

    if race == "Elf" and gender == "Male":
        name = elf_male_name[random.randint(0 , len(elf_male_name) - 1)] \
               + " " + elf_last_name[random.randint(0 , len(elf_last_name) - 1)]

    if race == "" and gender == "Female":
        name = elf_female_name[random.randint(0 , len(elf_female_name) - 1)] \
               + " " + elf_last_name[random.randint(0 , len(elf_last_name) - 1)]

    return name


def get_ability_scores(CharacterClass):
    scores = []
    for x in range(6):  # Outer Loop

        score = []
        for x in range(4):  # Inner Loop
            score.append(random.randint(1 , 6))

        score = sorted(score)  # Ordering results
        score.pop(0)  # Removing the smallest value
        scores.append(sum(score))

    scores = sorted(scores)
    arranged_scores = {'STR': 0 , 'CON': 0 , 'DEX': 0 , 'INT': 0 , 'WIS': 0 , 'CHA': 0}

    if CharacterClass == 'Warrior':
        arranged_scores['STR'] = scores[5]
        arranged_scores['CON'] = scores[4]
        arranged_scores['DEX'] = scores[3]
        arranged_scores['INT'] = scores[0]
        arranged_scores['WIS'] = scores[2]
        arranged_scores['CHA'] = scores[1]

    elif CharacterClass == 'Mage':
        arranged_scores['STR'] = scores[0]
        arranged_scores['CON'] = scores[4]
        arranged_scores['DEX'] = scores[3]
        arranged_scores['INT'] = scores[5]
        arranged_scores['WIS'] = scores[2]
        arranged_scores['CHA'] = scores[1]

    elif CharacterClass == 'Rogue':
        arranged_scores['STR'] = scores[0]
        arranged_scores['CON'] = scores[4]
        arranged_scores['DEX'] = scores[5]
        arranged_scores['INT'] = scores[1]
        arranged_scores['WIS'] = scores[3]
        arranged_scores['CHA'] = scores[2]

    return arranged_scores


class Character:

    def __init__(self):
        self.race = races[random.randint(0 , len(races) - 1)]
        self.CharacterClass = classes[random.randint(0 , len(classes) - 1)]
        self.gender = genders[random.randint(0 , len(genders) - 1)]
        self.name = get_random_name_char(self.race , self.gender)
        self.abilityScores = get_ability_scores(self.CharacterClass)


newCharacter = Character()
print(json.dumps(newCharacter.__dict__))
