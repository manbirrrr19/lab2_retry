import Lab2

def test_find_min_max():
    result = []
    input_arr = [5, 67, 32]
    test = (5, 67)

    result = Lab2.find_min_max(input_arr)

    assert (result == test)



def test_calc_average():
    result = []
    input_arr = [5, 67, 32]
    test = 34.666666666666664

    result = Lab2.calc_average(input_arr)

    assert (result == test)


def test_calc_median_temperature():
    result = []
    input_arr = [5, 67, 32]
    test = 32

    result = Lab2.calc_median_temperature(input_arr)

    assert (result == test)