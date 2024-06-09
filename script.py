def tic_tac_toe():
    
    
    data = {}

    def move(data, pos):
        pos = data.get(pos, pos)
        if pos == 1:
            return chr(215)
        elif pos == 0:
            return chr(9711)
        else:
            return pos

    def show_board():
        print(f' {move(data, "1")} | {move(data, "2")} | {move(data, "3")} ')
        print("-" * 11)
        print(f' {move(data, "4")} | {move(data, "5")} | {move(data, "6")} ')
        print("-" * 11)
        print(f' {move(data, "7")} | {move(data, "8")} | {move(data, "9")} ')
        print("\n")

    def winner_checker():
        win_pos = ["123", "456", "789", "147", "258", "369", "159", "357"]
        win_checkers = [[data.get(i) for i in j] for j in win_pos]
        check = True in [(set(i) == {1}) | (set(i) == {0}) for i in win_checkers]
        return check

    while True:
        
        show_board()
        
        player1 = input(f"Select a position (player {chr(215)}): ")
        print("\n")
        
        data[player1] = 1

        if winner_checker():
          print(f"Player {chr(215)} Won!\n")
          show_board()
          break
        
        show_board()
        
        player2 = input(f"Select a position (player {chr(9711)}): ")
        print("\n")
        
        data[player2] = 0

        if winner_checker():
          print(f"Player {chr(9711)} Won!\n")
          show_board()
          break