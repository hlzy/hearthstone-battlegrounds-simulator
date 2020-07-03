import Player.Player
import random
import copy
class Battle(object):
    def __init__(self,player1,player2):
        self.player1 = copy.copy(player1)
        self.player2 = copy.copy(player2)
        self.attack_index1 = 0
        self.attack_index2 = 0


    def attack(self,i,j):

    def start_battle(self):
        attack_dir = random.random() >= 0.5
        #monsters1 = self.player1.monsters[:]
        #monsters2 = self.player2.monsters[:]
        #start battle
        while True:
            attack_dir = not attack_dir
            #1. 攻守方选择随从
            attack_index = 
            #2. 攻守方判断是触发战前效果
            #3. 进行攻击
            #4. 触发死亡效果
