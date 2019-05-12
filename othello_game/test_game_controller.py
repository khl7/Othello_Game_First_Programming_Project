from game_controller import GameController
from stone import Stone


def test_constructor():
    stone = Stone(600)
    gc = GameController(600, stone)
    assert gc.width == 600


def test_start_game():
    pass  # Not testable because there is a graphical line of code in here


def test_can_go():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)
    gc.counter = 2
    gc.stone.total_row[3][3].color = 0  # 4 starting stones
    gc.stone.total_row[4][4].color = 0
    gc.stone.total_row[3][4].color = 1
    gc.stone.total_row[4][3].color = 1
    gc.can_go()
    assert len(gc.moves_list) == 4  # First move: 4 valids moves for player


def test_is_edge():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)
    assert gc.is_edge(0, 8) is True
    assert gc.is_edge(3, 0) is True
    assert gc.is_edge(4, 7) is True
    assert gc.is_edge(7, 4) is True
    assert gc.is_edge(1, 8) is None
    assert gc.is_edge(3, 4) is None
    assert gc.is_edge(2, 6) is None
    assert gc.is_edge(5, 5) is None


def test_is_corner():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)
    assert gc.is_corner(0, 0) is True
    assert gc.is_corner(7, 7) is True
    assert gc.is_corner(0, 7) is True
    assert gc.is_corner(7, 0) is True
    assert gc.is_corner(1, 8) is None
    assert gc.is_corner(3, 4) is None
    assert gc.is_corner(2, 6) is None
    assert gc.is_corner(5, 5) is None


def test_is_third_away():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)
    assert gc.is_third_away(2, 2) is True
    assert gc.is_third_away(5, 1) is True
    assert gc.is_third_away(1, 2) is True
    assert gc.is_third_away(2, 5) is True
    assert gc.is_third_away(1, 8) is None
    assert gc.is_third_away(6, 4) is None
    assert gc.is_third_away(3, 3) is None
    assert gc.is_third_away(4, 4) is None


def test_ai_make_move():
    pass  # Not testable because there is a graphical line of code in here


def test_check_valid_move():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)
    gc.counter = 2

    gc.stone.total_row[3][3].color = 0
    gc.stone.total_row[4][4].color = 0
    gc.stone.total_row[3][4].color = 1
    gc.stone.total_row[4][3].color = 1
    assert gc.check_valid_move(4, 2) is True
    assert gc.check_valid_move(5, 3) is True
    assert gc.check_valid_move(2, 4) is True
    assert gc.check_valid_move(3, 5) is True
    assert gc.check_valid_move(3, 4) is False
    assert gc.check_valid_move(2, 2) is False
    assert gc.check_valid_move(0, 0) is False
    assert gc.check_valid_move(7, 7) is False

    gc.counter = 1
    gc.stone.total_row[3][3].color = 0
    gc.stone.total_row[4][4].color = 0
    gc.stone.total_row[3][4].color = 1
    gc.stone.total_row[4][3].color = 1
    assert gc.check_valid_move(3, 2) is True
    assert gc.check_valid_move(4, 5) is True
    assert gc.check_valid_move(5, 4) is True
    assert gc.check_valid_move(2, 3) is True
    assert gc.check_valid_move(3, 4) is False
    assert gc.check_valid_move(2, 2) is False
    assert gc.check_valid_move(0, 0) is False
    assert gc.check_valid_move(7, 7) is False


def test_flip_stone():
    pass  # Not testable


def test_current_color():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)
    gc.counter = 2
    assert gc.current_color() == 0


def test_other_color():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)
    gc.counter = 2
    assert gc.other_color() == 1


def test_end_game():
    pass  # Not testable


def test_save_to_txt():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)

    gc.score_list = []  # Test case of empty list
    gc.player_score = 20
    gc.save_to_txt('Khai')
    test_list = []
    with open('scores.txt') as f:
        for line in f:
            new_line = line.split(' ')
            test_list.append([new_line[0], new_line[1]])
            assert test_list == [['Khai', '20\n']]

    gc.score_list = [['Khai', '22\n']]
    # Test case of existing list with higher score
    gc.player_score = 20
    gc.save_to_txt('Khai2')
    test_list = []
    with open('scores.txt') as f:
        for line in f:
            if line != '\n':
                new_line = line.split(' ')
                test_list.append([new_line[0], new_line[1]])
        assert test_list == [['Khai', '22\n'], ['Khai2', '20\n']]

    gc.score_list = [['Khai3', '20\n']]
    # Test case of existing list with lower score
    gc.player_score = 22
    gc.save_to_txt('Khai4')
    test_list = []
    with open('scores.txt') as f:
        for line in f:
            if line != '\n':
                new_line = line.split(' ')
                test_list.append([new_line[0], new_line[1]])
        assert test_list == [['Khai4', '22\n'], ['Khai3', '20\n']]


def test_read_file():
    WIDTH = 600
    stone = Stone(WIDTH)
    gc = GameController(WIDTH, stone)

    assert gc.score_list == []
    # The default when scores.txt is blank

    gc.read_file('test_scores.txt')
    assert gc.score_list == [['Khai4', 22], ['Khai3', 20]]
    # Tested from a test file
