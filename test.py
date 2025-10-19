try:
    from q1 import distance, area_from_sides, area_from_vertices
except:
    distance = lambda x: None
    area_from_sides = lambda x: None
    area_from_vertices = lambda x: None

try:
    from q2 import convert_temperature
except:
    convert_temperature = lambda x: None

try:
    from q3 import solve_quadratic
except:
    solve_quadratic = lambda x,y,z: None


def is_close(x, y):
    return abs(x - y) < 1e-6

# Q1 Tests
def test_q1_1():
    assert is_close(distance(-2, -2, -2, -2), 0)

def test_q1_2():
    assert is_close(distance(3, 5, 9, 13), 10)

def test_q1_3():
    assert is_close(distance(0, 3, 4, 0), 5)

def test_q1_4():
    assert is_close(area_from_sides(6.25, 4.25, 6.5), 12.75)

def test_q1_5():
    assert is_close(area_from_sides(20.5, 20.5, 9), 90)

def test_q1_6():
    assert is_close(area_from_sides(14.32, 18.53, 5.612), 30.027385522357424)

def test_q1_7():
    assert is_close(area_from_vertices(6.25, 4.25, 6.5), 12.75)

def test_q1_8():
    assert is_close(area_from_vertices(20.5, 20.5, 9), 90)

def test_q1_9():
    assert is_close(area_from_vertices(14.32, 18.53, 5.612), 30.027385522357424)

# Q2 Tests
def test_q2_1():
    assert is_close(convert_temperature(14, "F"), -10.0)

def test_q2_2():
    assert is_close(convert_temperature(32, "F"), 0)    

def test_q2_3():
    assert is_close(convert_temperature(10, "C"), 50.0)

def test_q2_4():
    assert is_close(convert_temperature(0, "C"), 32.0)

def test_q2_5():
    assert is_close(convert_temperature(10, "X"), None)

def test_q2_6():
    assert is_close(convert_temperature(20, "CF"), None)

# Q3 Tests
def test_q3_1():
    assert is_close(solve_quadratic(1, -5, 6), 2)

def test_q3_2():
    assert is_close(solve_quadratic(5.0, -33, 50.4), 2.4)

def test_q3_3():
    assert is_close(solve_quadratic(2, 25, 75), -7.5)


if __name__ == '__main__':
    tests_q1 = [test_q1_1, test_q1_2, test_q1_3, test_q1_4, test_q1_5, test_q1_6, test_q1_7, test_q1_8, test_q1_9]
    q1_passed = 0
    for test in tests_q1:
        try:
            test()
            q1_passed += 1
        except:
            pass
    print(f'Question 1: {q1_passed}/{len(tests_q1)} Tests Passed')

    tests_q2 = [test_q2_1, test_q2_2, test_q2_3, test_q2_4, test_q2_5, test_q2_6]
    q2_passed = 0
    for test in tests_q2:
        try:
            test()
            q2_passed += 1
        except:
            pass
    print(f'Question 2: {q2_passed}/{len(tests_q2)} Tests Passed')

    tests_q3 = [test_q3_1, test_q3_2, test_q3_3]
    q3_passed = 0
    for test in tests_q3:
        try:
            test()
            q3_passed += 1
        except:
            pass
    print(f'Question 3: {q3_passed}/{len(tests_q3)} Tests Passed')
