def main():
    stone = 20
    print(f"There are {stone} stones left.")
    
    while stone >= 0:
            print(f"\nThere are {stone} stones left")
            stone = players_turn(stone, 1)
            if stone == 0:
                print("Player 1 wins!")
                break
            print(f"\nThere are {stone} stones left")
            stone = players_turn(stone, 2)
            if stone == 0:
                print("Player 2 wins!")
                break
            
                
            
        


def players_turn(stone, player):
    while True:
        
        move = int(input(f"Player {player} would you like to take 1 or 2 stones? "))
        if move == 1 or move == 2:
            if stone - move >= 0:
                stone = stone - move 
                break
        
        else:
            print(int(input(f"Please enter 1 or 2: ")))
        
    return stone


if __name__ == '__main__':
    main()
