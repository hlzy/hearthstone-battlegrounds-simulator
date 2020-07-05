#对局玩家
class Player(object):
    def __init__(self,star=0):
        self.star = star
        self.monsters = []
        self.index = 0
        self.turns = 1
        self.hands = []  #用户当前的手牌
   

    #回合选择相关功能
    def pickMonster(self,name):
        pick_monster = Monster(name)
        

    #战斗相关功能
    #select target 
    #return index for monsters
    #1. taunt
    #2. normal
    #3. stealth can't be selected
    #return: -2 没怪 -1 有怪但无目标 else 目标索引
    def select_target(self):
        taunt = []
        stealth = []
        normal = []
        for i in range(len(self.monsters)):
            if self.monsters[i].special["嘲讽"]:
                taunt.append(i)
            elif self.monsters[i].special["潜行"]:
                stealth.append(i)
            else:
                normal.append(i)
        if len(taunt) > 0:
            return taunt[random.randint(0,len(taunt)-1)]
            #return self.monsters[taunt[random.randint(0,len(taunt)-1)]]
        elif len(normal) > 0:
            return normal[random.randint(0,len(normal)-1)]
            #return self.monsters[normal[random.randint(0,len(normal)-1)]]
        elif len(stealth) > 0:
            return -1

    #选取攻击方
    #从左向右选取第一个攻击大于0
    #return:索引号 找不到的情况返回-1
    #TODO:还要考虑大炮这种无法攻击的随从
    #return: -2 没怪 -1 有怪但无目标 else 目标索引
    def select_attack(self):
        if len(self.monsters) == 0:
            return -2
        trys = 0
        while trys<len(self.monsters):
            trys += 1
            if self.monsters[self.index].attack > 0:
                return self.monsters[self.index]
            self.index = (self.index + 1) % len(self.monsters)
        return -1
    
    #攻击前的一些效果
    #如海盗有了 亡灵舰长伊丽扎,撕心狼队长 在攻击前会触发增加攻击率
    def before_attack(self):
        pass
    
    #攻击后产生的效果 
    #如 巨大的金刚鹦鹉 会在攻击后触发随机的亡语
    #如 超杀带来的特效
    def after_attack(self):
        pass

if __name__ == "__main__":
    player1 = Player()
