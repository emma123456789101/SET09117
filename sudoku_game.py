# Emma Davidson
# sudoku game
# 31/03/2021




def get_difficulty(clues):
    if clues >= 30:
        return "easy"
    elif clues >= 20:
        return "medium"
    else:
        return "hard"


clues = int(input("what number would you like to have of clues"))

difficulty = get_difficulty(clues)

print("This Sudoku puzzle is" ,{difficulty}," difficulty.")
base = 3
side = base*base
# to get the users input on what level they would like to play



# asking the user which level they would like to play

if difficulty=="easy":
    # Ask the user which cell they want to update
    row = int(input("Enter the row number (0-8): "))
    col = int(input("Enter the column number (0-8): "))
    # Ask the user for the new value
    new_value = int(input("Enter the new value (1-9): "))


    # this is for the easier version
    base = 3
    side = base*base

#the baords pattern
    def pattern(r, c):return (base * (r % base) + r // base + c) % side


    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample

#shuffling numbers for the board when it prints
    def shuffle(s):
        return sample(s, len(s))


    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # producing the board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side
    empties = squares * 3 // 8
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0

    numSize = len(str(side))


    def expandLine(line):
        return line[0] + line[5:9].join([line[1:5] * (base - 1)] * base) + line[9:13]


    line0 = expandLine("╔═══╤═══╦═══╗")
    line1 = expandLine("║ . │ . ║ . ║")
    line2 = expandLine("╟───┼───╫───╢")
    line3 = expandLine("╠═══╪═══╬═══╣")
    line4 = expandLine("╚═══╧═══╩═══╝")
    print("0   1   2   3   4   5  6    7   8   9")
    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [[""] + [symbol[n] for n in row] for row in board]
    letters = [[""] + [symbol[n] for n in column] for column in board]
    print(line0)
    for r in range(1, side + 1):
       print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
       print([line2, line3, line4][(r % side == 0) + (r % base == 0)])
elif difficulty == "medium ":
    # Ask the user which cell they want to update
    row = int(input("Enter the row number (0-8): "))
    col = int(input("Enter the column number (0-8): "))
    # Ask the user for the new value
    new_value = int(input("Enter the new value (1-9): "))

    # this is for the medium version
    base = 3
    side = base * base
    from email.mime import base


    # pattern for a baseline valid solution
    def pattern(r, c):

        return (base * (r % base) + r // base + c) % side


    # randomize rows,columns and numbers (of valid base pattern)
    from random import sample


    def shuffle(s):
        return sample(s, len(s))


    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    squares = side * side

    empties = squares * 3 // 5
    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0

    numSize = len(str(side))


    def expandLine(line):
        return line[0] + line[5:9].join([line[1:5] * (base - 1)] * base) + line[9:13]


    line0 = expandLine("╔═══╤═══╦═══╗")
    line1 = expandLine("║ . │ . ║ . ║")
    line2 = expandLine("╟───┼───╫───╢")
    line3 = expandLine("╠═══╪═══╬═══╣")
    line4 = expandLine("╚═══╧═══╩═══╝")
    print("0   1   2   3   4   5  6    7   8   9")
    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [[""] + [symbol[n] for n in row] for row in board]
    letters = [[""] + [symbol[n] for n in column] for column in board]
    print(line0)
    for r in range(1, side + 1):
        print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
        print([line2, line3, line4][(r % side == 0) + (r % base == 0)])


else:  # Ask the user which cell they want to update
        row = int(input("Enter the row number (0-8): "))
        col = int(input("Enter the column number (0-8): "))
        # Ask the user for the new value
        new_value = int(input("Enter the new value (1-9): "))
        # this is for the easier version
        base = 3
        side = base * base


        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side


        # randomize rows, columns and numbers (of valid base pattern)
        from random import sample


        def shuffle(s):
            return sample(s, len(s))


        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))

        # producing the board using randomized baseline pattern
        board = [[nums[pattern(r, c)] for c in cols] for r in rows]

        squares = side * side
        empties = squares * 3 // 4
        for p in sample(range(squares), empties):
            board[p // side][p % side] = 0

        numSize = len(str(side))


        def print_board(baord):
            def expandLine(line):
                return line[0] + line[5:9].join([line[1:5] * (base - 1)] * base) + line[9:13]

            line0 = expandLine("╔═══╤═══╦═══╗")
            line1 = expandLine("║ . │ . ║ . ║")
            line2 = expandLine("╟───┼───╫───╢")
            line3 = expandLine("╠═══╪═══╬═══╣")
            line4 = expandLine("╚═══╧═══╩═══╝")
            print("0   1   2   3   4   5  6    7   8   9")
            symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            nums = [[""] + [symbol[n] for n in row] for row in board]
            letters = [[""] + [symbol[n] for n in column] for column in board]
            print(line0)
            for r in range(1, side + 1):
                print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
                print([line2, line3, line4][(r % side == 0) + (r % base == 0)])
                # Replacing the "." character with the user's new value
                line1 = line1.replace(".", str(new_value))
                # Replacing the "." character with the user's new value
                line1 = line1.replace(".", str(new_value))


def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def check_isVaild():
    num = input("Enter a number between 1 and 9: ")
    if check_isVaild(num):
        print("Valid input!")
    else:
        print("Invalid input. Please enter a number between 1 and 9.")
def main():
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = int(input("Enter value for row " + str(i + 1) + ", column " + str(j + 1) + ": "))


    print_sudoku(board)

if __name__ == "__main__":
    main()
