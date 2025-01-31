from pytest import fixture
from solve import Solver
from boardGeneration import Generator

class TestSolveBoard:
    @fixture
    def solver(self):
        return Solver()

    @fixture
    def a(self):
        return [
            ['.', '.', '.',     '.', '.', '.',    '.', '1', '2'],
            ['.', '.', '.',     '.', '3', '5',    '.', '.', '.'],
            ['.', '.', '.',     '6', '.', '.',    '.', '7', '.'],

            ['7', '.', '.',     '.', '.', '.',    '3', '.', '.'],
            ['.', '.', '.',     '4', '.', '.',    '8', '.', '.'],
            ['1', '.', '.',     '.', '.', '.',    '.', '.', '.'],

            ['.', '.', '.',     '1', '2', '.',    '.', '.', '.'],
            ['.', '8', '.',     '.', '.', '.',    '.', '4', '.'],
            ['.', '5', '.',     '.', '.', '.',    '6', '.', '.']
        ]

    @fixture
    def b(self):
        return [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".",
                                                                                                                                                                                                             "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    @fixture
    def c(self):
        return [
            ['5', '1', '6',     '8', '4', '9',    '7', '3', '2'],
            ['3', '.', '7',     '6', '.', '5',    '.', '.', '.'],
            ['8', '.', '9',     '7', '.', '.',    '.', '6', '5'],

            ['1', '3', '5',     '.', '6', '.',    '9', '.', '7'],
            ['4', '7', '2',     '5', '9', '1',    '.', '.', '6'],
            ['9', '6', '8',     '3', '7', '.',    '.', '5', '.'],

            ['2', '5', '3',     '1', '8', '6',    '.', '7', '4'],
            ['6', '8', '4',     '2', '.', '7',    '5', '.', '.'],
            ['7', '9', '1',     '.', '5', '.',    '6', '.', '8']
        ]

    @fixture
    def d(self):
        return [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8",
                                                                                                                                                                                                             "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

    @fixture
    def d(self):
        return [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8",
                                                                                                                                                                                                             "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

    def test_solving(self, solver, a, b, c, d):
        assert solver.solveSudoku(a) == (True, [['6', '7', '3', '8', '9', '4', '5', '1', '2'], ['9', '1', '2', '7', '3', '5', '4', '8', '6'], ['8', '4', '5', '6', '1', '2', '9', '7', '3'], ['7', '9', '8', '2', '6', '1', '3', '5', '4'], [
            '5', '2', '6', '4', '7', '3', '8', '9', '1'], ['1', '3', '4', '5', '8', '9', '2', '6', '7'], ['4', '6', '9', '1', '2', '8', '7', '3', '5'], ['2', '8', '7', '3', '5', '6', '1', '4', '9'], ['3', '5', '1', '9', '4', '7', '6', '2', '8']])
        assert solver.solveSudoku(b) == (False, None, False)
        assert solver.solveSudoku(c) == (False, None)
        assert solver.solveSudoku(d) == (True, [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], [
            '4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']])


class TestBoardGen:
    @fixture
    def generator(self):
        return Generator()
    
    def confirm_valid(self,board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqr = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                v = board[i][j]
                if v == '.' or not (0 < int(v) < 10):
                    return False
                if v in rows[i] or v in cols[j] or v in sqr[i//3][j//3]:
                    return False
                rows[i].add(v)
                cols[j].add(v)
                sqr[i//3][j//3].add(v)
        

        return len(board) == len(board[0]) == 9 
    
    def test_board_gen_valid_cases(self, generator):
        assert self.confirm_valid(generator.base_solution(25))
        assert self.confirm_valid(generator.base_solution(11))
        assert self.confirm_valid(generator.base_solution(0))
        assert self.confirm_valid(generator.base_solution(1))
        assert self.confirm_valid(generator.base_solution(10))
        assert self.confirm_valid(generator.base_solution(24))
        assert self.confirm_valid(generator.base_solution(7))
    
    def test_board_gen_nonvalid_cases(self, generator):
        assert not self.confirm_valid(generator.base_solution(26))
        assert not self.confirm_valid(generator.base_solution(40)) 
        assert not self.confirm_valid(generator.base_solution(81))
        assert not self.confirm_valid(generator.base_solution(100))
        assert not self.confirm_valid(generator.base_solution(-1))

class TestDigging:
    pass