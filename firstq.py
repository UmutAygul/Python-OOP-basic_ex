class Player:
    def __init__(self,fn,ln,age,nation):
        self.__fn=fn
        self.__ln=ln
        self.__age=age
        self.__nation=nation
        
    def setfn(self,fn):
        self.__fn=fn
    def getfn(self):
        return self.__fn
    
    def setln(self,ln):
        self.__ln=ln
    def getln(self):
        return self.__ln
    
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
    
    def setnation(self,nation):
        self.__nation=nation
    def getnation(self):
        return self.__nation
    
    
    def print_player(self):
        print("Name:",self.getfn()," ",self.getln())
        print("Age:",self.getage())
        print("Nation:",self.getnation())


    
    
class LeaguePlayer(Player):
    def __init__(self,fn,ln,age,nation,branch,game_num,win_num,lost_num,player_score):
        super().__init__(fn,ln,age,nation)
        
        self.__branch=branch
        self.__game_num=game_num
        self.__win_num=win_num
        self.__lost_num=lost_num
        self.__player_score=player_score
        
    def setbranch(self,branch):
        self.__branch=branch
    def getbranch(self):
        return self.__branch
        
    def setgame_num(self,game_num):
        self.__game_num=game_num
    def getgame_num(self):
        return self.__game_num
        
    def setwin_num(self,win_num):
        self.__win_num=win_num
    def getwin_num(self):
        return self.__win_num
        
    def setlost_num(self,lost_num):
        self.__lost_num=lost_num
    def getlost_num(self):
        return self.__lost_num
        
    def setplayer_score(self,player_score):
        self.__player_score=player_score
    def getplayer_score(self):
        return self.__player_score
        
        
    def print_player(self):
        super().print_player()
        print("Branch game:",self.getbranch())
        print("Game num",self.getgame_num())
        print("Win num",self.getwin_num())
        print("lost num",self.getlost_num())
        print("player scor: ",self.getplayer_score())
        
    def statistics(self):
        statistics=self.getplayer_score() / self.getgame_num()
        print("Statics: ",statistics)
    
    def points(self):
        points=10*self.getgame_num()+3*self.getwin_num()-2*self.getlost_num()
        return points
        
    
class NationalPlayer(LeaguePlayer):
    def __init__(self,fn,ln,age,nation,branch,game_num,win_num,lost_num,player_score,nationalgame_num,nationalPlayer_score):
        super().__init__(fn,ln,age,nation,branch,game_num,win_num,lost_num,player_score)
        self.__nationalgame_num=nationalgame_num
        self.__nationalPlayer_score=nationalPlayer_score
        
    def setnationalPlayer_score(self,nationalPlayer_score):
        self.__nationalPlayer_score=nationalPlayer_score
    def getnationalPlayer_score(self):
        return self.__nationalPlayer_score
    def setnationalgame_num(self,nationalgame_num):
        self.__nationalgame_num=nationalgame_num
    def getnationalgame_num(self):
        return self.__nationalgame_num
    
    def print_player(self):
        super().print_player()
        print("National player score:",self.getnationalPlayer_score())
        print("National game number: ",self.getnationalgame_num())
    
    def statistics(self):
        statistics=self.getnationalPlayer_score()/self.getnationalgame_num()
        print("Statics:",statistics)
    def points(self):
        points=15*self.getnationalgame_num()+10*self.getgame_num()+3*self.getwin_num()-2*self.getlost_num()
        return points
    
    
    
def main():
    my=Player("Fabian","Delph",22,"England")
    my.print_player()

    my2=LeaguePlayer("Tony", "Parker", 28, "france", "basketboll", 36, 17, 19, 22)    
    my2.print_player()
    my2.statistics()
    print("Player points:",my2.points())

    
    my3=NationalPlayer("Jordan", "Larson", 22, "Usa", "Voleyball", 21, 16, 5, 36, 8, 3)
    my3.print_player()
    my3.statistics()
    print("Player points:",my3.points())

main()
        
        
        
        
    
    