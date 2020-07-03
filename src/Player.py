#玩家结构体，对局只能有两个玩家
class Player(object):
    def __init__(self,monsters=[],star=0):
        self.star = star
        self.monsters = []
        self.index = 0
    
    #select target 
    #return index for monsters
    #1. taunt
    def select_target(self,targets):
        pass

    def select_attack(self,targets):
        return self.monsters[self.index]
