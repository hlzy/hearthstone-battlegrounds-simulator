import pandas as pd
#Time 20200702

Monsters_file = pd.read_excel("../data/monster.xlsx")
#种族索引
index_to_race = dict()
race_to_index = dict()
race = Monsters_file["race"].unique().tolist()
for i,each_race in enumerate(race):
    global race_to_inde
    global index_to_race
    race_to_index[each_race] = i
    index_to_race[i] = each_race

#怪物名称索引
index_to_name = dict()
name_to_index = dict()
names = Monsters_file["name"].unique().tolist()
for i,each_name in enumerate(names):
    global index_to_name
    global name_to_index
    name_to_index[each_name] = i
    index_to_name[i] = each_name


#随从
class Monster(object):
    def __init__(self,name):
       self.name = name
       self.star = Monsters_file[Monsters_file["name"] = name]["star"]
       self.attack = Monsters_file[Monsters_file["name"] = name]["attack"]
       self.health = Monsters_file[Monsters_file["name"] = name]["health"]
       self.race = Monsters_file[Monsters_file["name"] = name]["race"]
       self.special = Monsters_file[Monsters_file["name"] = name]["special"].split(",")
