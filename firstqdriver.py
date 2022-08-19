from firstq import Player
from firstq import LeaguePlayer
from firstq import NationalPlayer



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