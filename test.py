import batyu


def test():
    day_index = batyu.get_day_index()
    monday_foods = batyu.get_menu(day_index)
    assert len(monday_foods) > 0

    sunday_foods = batyu.get_menu(6)
    assert len(sunday_foods) == 0


if __name__ == '__main__':
    test()
