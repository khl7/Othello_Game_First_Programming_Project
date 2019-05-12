from stone import Stone

SIZE = 16
LEN = 8


def test_constructor():
    width = 600
    stone = Stone(width)

    assert len(stone.first_row) == LEN
    assert len(stone.second_row) == LEN
    assert len(stone.third_row) == LEN
    assert len(stone.fourth_row) == LEN
    assert len(stone.fifth_row) == LEN
    assert len(stone.sixth_row) == LEN
    assert len(stone.seventh_row) == LEN
    assert len(stone.eighth_row) == LEN
    assert len(stone.total_row) == LEN

    i = 1

    for l in range(len(stone.first_row)):
        assert stone.first_row[l].x == stone.SPACING * i
        i += 2
        assert stone.first_row[l].y == width/SIZE

    i = 1

    for l in range(len(stone.second_row)):
        assert stone.second_row[l].x == stone.SPACING * i
        i += 2
        assert stone.second_row[l].y == width/SIZE + (width/(SIZE/2)) * 1

    i = 1

    for l in range(len(stone.third_row)):
        assert stone.third_row[l].x == stone.SPACING * i
        i += 2
        assert stone.third_row[l].y == width/SIZE + (width/(SIZE/2)) * 2

    i = 1

    for l in range(len(stone.fourth_row)):
        assert stone.fourth_row[l].x == stone.SPACING * i
        i += 2
        assert stone.fourth_row[l].y == width/SIZE + (width/(SIZE/2)) * 3

    i = 1

    for l in range(len(stone.fifth_row)):
        assert stone.fifth_row[l].x == stone.SPACING * i
        i += 2
        assert stone.fifth_row[l].y == width/SIZE + (width/(SIZE/2)) * 4

    i = 1

    for l in range(len(stone.sixth_row)):
        assert stone.sixth_row[l].x == stone.SPACING * i
        i += 2
        assert stone.sixth_row[l].y == width/SIZE + (width/(SIZE/2)) * 5

    i = 1

    for l in range(len(stone.seventh_row)):
        assert stone.seventh_row[l].x == stone.SPACING * i
        i += 2
        assert stone.seventh_row[l].y == width/SIZE + (width/(SIZE/2)) * 6

    i = 1

    for l in range(len(stone.eighth_row)):
        assert stone.eighth_row[l].x == stone.SPACING * i
        i += 2
        assert stone.eighth_row[l].y == width/SIZE + (width/(SIZE/2)) * 7
