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
        pass

    #检测当前是否可以继续战斗
    #如果不能战斗,判断当前的结果
    # 0 继续
    # 1 player1 win
    # 2 player2 win
    # 3 tie
    def check_status(self):
        player1_index = self.player1.select_attack()
        player2_index = self.player2.select_attack()
        if player1_index == -2 and player2_index == -2:
            return 3
        if player1_index == -1 and player2_index == -1:
            return 3
        if player2_index == -2:
            return 1 
        if player1_index == -2:
            return 2 
        return 0

    def start_battle(self):
        attack_dir = random.random() >= 0.5
        #monsters1 = self.player1.monsters[:]
        #monsters2 = self.player2.monsters[:]
        #start battle
        while self.check_status() == 0:
            attack_dir = not attack_dir
            attack,target = self.player1,self.player2 if attack_dir else self.player2,self.player1
            #1. 攻守方选择随从,如果没有可以攻击的随从切换对手
            attack_index = attack.select_attack()
            target_index = target.select_target()
            if attack_index == -1:
                continue
            #2. 攻守方判断是触发战前效果
            attack.before_attack()
            #3. 进行攻击
            attack_attack,attack_health = attack.monsters[attack_index].attack,attack.monsters[attack_index].health
            target_attack,target_health = target.monsters[target_index].attack,target.monsters[target_index].health
            attack_health -= target_attack
            target_health -= attack_attack
            attack.monsters.triger()
            #4. 触发死亡效果
