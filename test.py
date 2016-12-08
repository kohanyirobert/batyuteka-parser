import batyu


def test():
    monday_foods = batyu.get_menu(0)
    assert len(monday_foods) > 0

    sunday_foods = batyu.get_menu(6)
    assert len(sunday_foods) == 0


if __name__ == '__main__':
    test()
