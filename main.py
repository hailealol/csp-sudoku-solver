def build_sudoku_board(array):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("—————————————————————")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            if array[row][col] == 0:
                print(".", end=" ")
            else:
                print(array[row][col],end=" ")
        print()

def main():
    print("Initial State:")
    puzzle = [
        [0,0,0,9,0,2,0,3,0],
        [0,0,0,0,0,0,0,4,0],
        [0,0,8,3,0,0,6,5,0],
        [0,0,0,8,2,0,1,0,0],
        [3,0,0,6,4,0,0,0,7],
        [7,6,0,5,3,1,0,0,0],
        [8,0,0,7,0,0,9,0,6],
        [0,0,0,0,0,8,0,7,0],
        [5,0,0,0,9,6,0,0,2]
    ]
    build_sudoku_board(puzzle)
    return 0

if __name__ == '__main__':
    main()