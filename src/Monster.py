import pandas as pd
#Time 20200702

Monsters_file = pd.read_excel("../data/monster.xlsx")
#种族索引
index_to_race = dict()
race_to_index = dict()
race = Monsters_file["race"].unique().tolist()
for i,each_race in enumerate(race):
    #global race_to_index
    #global index_to_race
    race_to_index[each_race] = i
    index_to_race[i] = each_race

#怪物名称索引
index_to_name = dict()
name_to_index = dict()
names = Monsters_file["name"].unique().tolist()
for i,each_name in enumerate(names):
    #global index_to_name
    #global name_to_index
    name_to_index[each_name] = i
    index_to_name[i] = each_name

special_list = set()
for each in Monsters_file["special"].tolist():
    for each_special in each.split(","):
        special_list.add(each_special.replace(chr(0xa0),""))


##随从
class Monster(object):
    def __init__(self,name):
       self.name = name
       self.star =  int(Monsters_file[Monsters_file["name"] == name]["star"].tolist()[0])
       self.attack =int(Monsters_file[Monsters_file["name"] == name]["attack"].tolist()[0])
       self.health =int(Monsters_file[Monsters_file["name"] == name]["health"].tolist()[0])
       self.race =  str(Monsters_file[Monsters_file["name"] == name]["race"].tolist()[0])
       self.gold = False
       self.special = dict()
       for each in special_list:
           self.special[each] = False
       for each_special in str(Monsters_file[Monsters_file["name"] == name]["special"].tolist()[0]).replace(chr(0xa0),"").split(","):
           self.special[each_special] = True

    #触发亡语特效,特效的种类有几种
    #1. 增益类,给队友带来特效
    #2. 召唤类,召唤一个特定类型的随从
    #3. 伤害类,如 食尸鬼 
    def triger_death(self,name):
        pass 

    #1. 召唤类
    def triger_battlecry(self,name):
        if name="雄斑虎":
            return  1,Monster()

    def show(self):
        print("""name:{}
                star:{}
                attack:{}
                health:{}
                race:{}
                gold:{}
                special_list:{}
                """.format(self.name,
                    self.star,
                    self.attack,
                    self.health,
                    self.race,
                    self.gold,
                    str(self.special.items())
                    ))

if __name__ == "__main__":
    a = Monster("毒鳍鱼人")
    a.show()
