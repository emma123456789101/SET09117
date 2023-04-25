# Emma Davidson
# sudoku game
# 31/03/2021

difficulty = "debug"
base = 3
side = base*base
# to get the users input on what level they would like to play



# asking the user which level they would like to play
def board():
    input("which level would you like to play easy, medium or hard")
    if difficulty=="easy":

        # this is for the easier version
        base = 3
        side = base*base





        def pattern(r, c):return (base * (r % base) + r // base + c) % side


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
           #printing the time it took the user
            print("--finished calculating--")
            # this function is to play the sudoku
        def playSudoku(board):
            board = [[-n for n in row] for row in board]
            while not sudokuDone(board):
                printSudoku(board)
                command = input("Enter Row,Column=Number: ")
                try:
                    r, c, n = map(int, command.replace("=", ",").split(","))
                except:
                    print("Invalid input")
                    continue
                if n not in range(0, 10): print("Number must be 0...9");continue
                if r not in range(1, 10): print("Row must be 1...9");continue
                if c not in range(1, 10): print("col must be 1...9");continue
                if board[r - 1][c - 1] < 0: print("Cannot change initial numbers");continue
                board[r - 1][c - 1] = n
                printSudoku(board)
                print("well done the game is over!!")

                def shortSudokuSolve(board):
                    size = len(board)
                    block = int(size ** 0.5)
                    board = [n for row in board for n in row]
                    span = {(n, p): {(g, n) for g in (n > 0) * [p // size, size + p % size,
                                                                2 * size + p % size // block + p // size // block * block]}
                            for p in range(size * size) for n in range(size + 1)}
                    empties = [i for i, n in enumerate(board) if n == 0]
                    used = set().union(*(span[n, p] for p, n in enumerate(board) if n))
                    empty = 0
                    while empty >= 0 and empty < len(empties):
                        pos = empties[empty]
                        used -= span[board[pos], pos]
                        board[pos] = next((n for n in range(board[pos] + 1, size + 1) if not span[n, pos] & used), 0)
                        used |= span[board[pos], pos]
                        empty += 1 if board[pos] else -1
                        if empty == len(empties):
                            solution = [board[r:r + size] for r in range(0, size * size, size)]
                            yield solution
                            empty -= 1
                solution = [[9, 5, 3, 1, 6, 7, 4, 2, 8],
                            [4, 2, 8, 3, 5, 9, 7, 6, 1],
                            [7, 6, 1, 8, 2, 4, 9, 5, 3],
                            [5, 8, 4, 9, 3, 6, 2, 1, 7],
                            [6, 3, 9, 7, 1, 2, 5, 8, 4],
                            [2, 1, 7, 4, 8, 5, 6, 3, 9],
                            [3, 4, 5, 6, 9, 1, 8, 7, 2],
                            [8, 7, 2, 5, 4, 3, 1, 9, 6],
                            [1, 9, 6, 2, 7, 8, 3, 4, 5]]
                board = [[0, 0, 0, 0, 0, 0, 0, 0, 8],
                         [0, 2, 0, 0, 5, 0, 7, 6, 0],
                         [0, 6, 0, 0, 0, 0, 0, 0, 3],
                         [5, 0, 0, 0, 0, 0, 2, 0, 7],
                         [0, 3, 0, 0, 1, 0, 0, 0, 0],
                         [2, 0, 0, 4, 0, 0, 0, 3, 0],
                         [0, 0, 0, 6, 0, 0, 0, 0, 0],
                         [8, 0, 0, 0, 0, 0, 0, 0, 0],
                         [1, 0, 0, 2, 7, 0, 0, 4, 0]]

                import random
                from itertools import islice
                while True:
                    solved = [*islice(shortSudokuSolve(board), 2)]
                    if len(solved) == 1: break
                    diffPos = [(r, c) for r in range(9) for c in range(9)
                               if solved[0][r][c] != solved[1][r][c]]
                    r, c = random.choice(diffPos)
                    board[r][c] = solution[r][c]
# this is for the medium version

    elif difficulty=="medium":
                from email.mime import base

                base = 3
                side = base * base


                # pattern for a baseline valid solution
                def pattern(r, c):

                    return (base * (r % base) + r // base + c) % side


                # randomize rows,columns and numbers (of valid base pattern)
                from random import sample


                def shuffle(s): return sample(s, len(s))


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

                print(line0)
                for r in range(1, side + 1):
                     print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
                     print([line2, line3, line4][(r % side == 0) + (r % base == 0)])


                # this function is to play the sudoku
                def playSudoku(board):
                    board = [[-n for n in row] for row in board]
                    while not sudokuDone(board):
                        printSudoku(board)
                        command = input("Enter Row,Column=Number: ")
                        try:
                            r, c, n = map(int, command.replace("=", ",").split(","))
                        except:
                            print("Invalid input")
                            continue
                        if n not in range(0, 10): print("Number must be 0...9");continue
                        if r not in range(1, 10): print("Row must be 1...9");continue
                        if c not in range(1, 10): print("col must be 1...9");continue
                        if board[r - 1][c - 1] < 0: print("Cannot change initial numbers");continue
                        board[r - 1][c - 1] = n
                        printSudoku(board)
                        print("well done the game is over!!")

                        def shortSudokuSolve(board):
                            size = len(board)
                            block = int(size ** 0.5)
                            board = [n for row in board for n in row]
                            span = {(n, p): {(g, n) for g in (n > 0) * [p // size, size + p % size,
                                                                        2 * size + p % size // block + p // size // block * block]}
                                    for p in range(size * size) for n in range(size + 1)}
                            empties = [i for i, n in enumerate(board) if n == 0]
                            used = set().union(*(span[n, p] for p, n in enumerate(board) if n))
                            empty = 0
                            while empty >= 0 and empty < len(empties):
                                pos = empties[empty]
                                used -= span[board[pos], pos]
                                board[pos] = next((n for n in range(board[pos] + 1, size + 1) if not span[n, pos] & used),
                                                  0)
                                used |= span[board[pos], pos]
                                empty += 1 if board[pos] else -1
                                if empty == len(empties):
                                    solution = [board[r:r + size] for r in range(0, size * size, size)]
                                    yield solution
                                    empty -= 1
                        solution = [[9, 5, 3, 1, 6, 7, 4, 2, 8],
                                    [4, 2, 8, 3, 5, 9, 7, 6, 1],
                                    [7, 6, 1, 8, 2, 4, 9, 5, 3],
                                    [5, 8, 4, 9, 3, 6, 2, 1, 7],
                                    [6, 3, 9, 7, 1, 2, 5, 8, 4],
                                    [2, 1, 7, 4, 8, 5, 6, 3, 9],
                                    [3, 4, 5, 6, 9, 1, 8, 7, 2],
                                    [8, 7, 2, 5, 4, 3, 1, 9, 6],
                                    [1, 9, 6, 2, 7, 8, 3, 4, 5]]
                        board = [[0, 0, 0, 0, 0, 0, 0, 0, 8],
                                 [0, 2, 0, 0, 5, 0, 7, 6, 0],
                                 [0, 6, 0, 0, 0, 0, 0, 0, 3],
                                 [5, 0, 0, 0, 0, 0, 2, 0, 7],
                                 [0, 3, 0, 0, 1, 0, 0, 0, 0],
                                 [2, 0, 0, 4, 0, 0, 0, 3, 0],
                                 [0, 0, 0, 6, 0, 0, 0, 0, 0],
                                 [8, 0, 0, 0, 0, 0, 0, 0, 0],
                                 [1, 0, 0, 2, 7, 0, 0, 4, 0]]

                        import random
                        from itertools import islice
                        while True:
                            solved = [*islice(shortSudokuSolve(board), 2)]
                            if len(solved) == 1: break
                            diffPos = [(r, c) for r in range(9) for c in range(9)
                                       if solved[0][r][c] != solved[1][r][c]]
                            r, c = random.choice(diffPos)
                            board[r][c] = solution[r][c]

    # this is for the hard level
    else:

            def pattern(r, c): return (base * (r % base) + r // base + c) % side



            # randomize rows, columns and numbers (of valid base pattern)
            from random import sample


            def shuffle(s): return sample(s, len(s))


            rBase = range(base)
            rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
            cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
            nums = shuffle(range(1, base * base + 1))

            # produce board using randomized baseline pattern
            board = [[nums[pattern(r, c)] for c in cols] for r in rows]

            squares = side * side
            empties = squares * 3 // 4
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
            print(line0)
            for r in range(1, side + 1):
               print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
               print([line2, line3, line4][(r % side == 0) + (r % base == 0)])


            # this function is to play the sudoku
            def playSudoku(board):
                board = [[-n for n in row] for row in board]
                while not sudokuDone(board):
                    printSudoku(board)
                    command = input("Enter Row,Column=Number: ")
                    try:
                        r, c, n = map(int, command.replace("=", ",").split(","))
                    except:
                        print("Invalid input")
                        continue
                    if n not in range(0, 10): print("Number must be 0...9");continue
                    if r not in range(1, 10): print("Row must be 1...9");continue
                    if c not in range(1, 10): print("col must be 1...9");continue
                    if board[r - 1][c - 1] < 0: print("Cannot change initial numbers");continue
                    board[r - 1][c - 1] = n
                    printSudoku(board)
                    print("well done the game is over!!")


            def shortSudokuSolve(board):
                size = len(board)
                block = int(size ** 0.5)
                board = [n for row in board for n in row]
                span = {(n, p): {(g, n) for g in (n > 0) * [p // size, size + p % size,
                                                            2 * size + p % size // block + p // size // block * block]}
                        for p in range(size * size) for n in range(size + 1)}
                empties = [i for i, n in enumerate(board) if n == 0]
                used = set().union(*(span[n, p] for p, n in enumerate(board) if n))
                empty = 0
                while empty >= 0 and empty < len(empties):
                    pos = empties[empty]
                    used -= span[board[pos], pos]
                    board[pos] = next((n for n in range(board[pos] + 1, size + 1) if not span[n, pos] & used), 0)
                    used |= span[board[pos], pos]
                    empty += 1 if board[pos] else -1
                    if empty == len(empties):
                        solution = [board[r:r + size] for r in range(0, size * size, size)]
                        yield solution
                        empty -= 1
            solution = [[9, 5, 3, 1, 6, 7, 4, 2, 8],
                        [4, 2, 8, 3, 5, 9, 7, 6, 1],
                        [7, 6, 1, 8, 2, 4, 9, 5, 3],
                        [5, 8, 4, 9, 3, 6, 2, 1, 7],
                        [6, 3, 9, 7, 1, 2, 5, 8, 4],
                        [2, 1, 7, 4, 8, 5, 6, 3, 9],
                        [3, 4, 5, 6, 9, 1, 8, 7, 2],
                        [8, 7, 2, 5, 4, 3, 1, 9, 6],
                        [1, 9, 6, 2, 7, 8, 3, 4, 5]]
            board = [[0, 0, 0, 0, 0, 0, 0, 0, 8],
                     [0, 2, 0, 0, 5, 0, 7, 6, 0],
                     [0, 6, 0, 0, 0, 0, 0, 0, 3],
                     [5, 0, 0, 0, 0, 0, 2, 0, 7],
                     [0, 3, 0, 0, 1, 0, 0, 0, 0],
                     [2, 0, 0, 4, 0, 0, 0, 3, 0],
                     [0, 0, 0, 6, 0, 0, 0, 0, 0],
                     [8, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 2, 7, 0, 0, 4, 0]]

            import random
            from itertools import islice

            while True:
                solved = [*islice(shortSudokuSolve(board), 2)]
                if len(solved) == 1: break
                diffPos = [(r, c) for r in range(9) for c in range(9)
                           if solved[0][r][c] != solved[1][r][c]]
                r, c = random.choice(diffPos)
                board[r][c] = solution[r][c]



