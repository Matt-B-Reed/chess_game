board = [[x_coor,y_coor,"black"] for x_coor in ["a","b", "c","d","e","f","g","h"] for y_coor in range(1,9)] #8 by 8 board (1,1) is the top left black piece of the board.
for ele in board:
    if ele[1] %2 == 0:
        ele[2] = "White"


class pieces():
    def __init__(self, name, color, starting_position, current_position):
        self.name = name
        self.color = color
        self.starting_position = starting_position
        self.current_position = current_position

def init_game_pieces():
    white_team = []
    black_team = []
    x_range = ["a","b", "c","d","e","f","g","h"]
    x_pos = 0
    converted_x = 0
    y_pos = 0
    for color in ["Black", "White"]:
        for name in ["Rook","Knight","Bishop","King", "Queen","Bishop","Knight","Rook","Pawn1","Pawn2","Pawn3","Pawn4","Pawn5","Pawn6","Pawn7","Pawn8"]:
            if x_pos == 8:
                x_pos = 0
                if color == "White":
                    if name == "Pawn":
                        y_pos = 2
                        converted_x = x_range[x_pos]
                        piece = [name, color, (converted_x,y_pos),[converted_x,y_pos]]
                        white_team.append(piece)
                        x_pos+=1
                        print(piece)
                    else:
                        y_pos = 1
                        converted_x = x_range[x_pos]
                        piece = [name, color, (converted_x,y_pos),[converted_x,y_pos]]
                        white_team.append(piece)
                        x_pos+=1
                        print(piece)
                elif color == "Black":
                    if name == "Pawn":
                        y_pos = 7
                        converted_x = x_range[x_pos]
                        piece = [name, color, (converted_x,y_pos),[converted_x,y_pos]]
                        black_team.append(piece)
                        x_pos+=1
                        print(piece)
                    else:
                        y_pos = 8
                        converted_x = x_range[x_pos]
                        piece = [name, color, (converted_x,y_pos),[converted_x,y_pos]]
                        black_team.append(piece)
                        x_pos+=1
                        print(piece)
            else:
                if color == "White":
                    if name == "Pawn":
                        y_pos = 2
                        converted_x = x_range[x_pos]
                        piece = [name, color, (converted_x,y_pos),[converted_x,y_pos]]
                        black_team.append(piece)
                        x_pos+=1
                        print(piece)
                    else:
                        y_pos = 1
                        converted_x = x_range[x_pos]
                        piece = [name, color, (converted_x,y_pos),[converted_x,y_pos]]
                        black_team.append(piece)
                        x_pos+=1
                        print(piece)
                elif color == "Black":
                    if name == "Pawn":
                        y_pos = 7
                        converted_x = x_range[x_pos]
                        piece = [name, color, (converted_x,y_pos),[converted_x,y_pos]]
                        black_team.append(piece)
                        x_pos+=1
                        print(piece)
                    else:
                        y_pos = 8
                        converted_x = x_range[x_pos]
                        piece = [name, color, (converted_x,y_pos),[converted_x,y_pos]]
                        black_team.append(piece)
                        x_pos+=1
                        print(piece)

init_game_pieces()
