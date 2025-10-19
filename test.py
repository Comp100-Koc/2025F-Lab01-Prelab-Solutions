try:
    from q1 import calculate_f
except:
    calculate_f = lambda x: None

try:
    from q2 import solve_quadratic
except:
    solve_quadratic = lambda x,y,z: None

try:
    from q3 import calculate_distance
except:
    calculate_distance = lambda x,y: None

try:
    from q4 import calculate_area
except:
    calculate_area = lambda x,y, z: None 

def is_close(x, y):
    return abs(x - y) < 1e-6

def test_q1_1():
    assert is_close(calculate_f(3), 1)

def test_q1_2():    
    assert is_close(calculate_f(6), 1.5)

def test_q1_3():
    assert is_close(calculate_f(15), 2)

def test_q2_1():
    assert is_close(solve_quadratic(1, -5, 6), 2)

def test_q2_2():
    assert is_close(solve_quadratic(5.0, -33, 50.4), 2.4)

def test_q2_3():
    assert is_close(solve_quadratic(2, 25, 75), -7.5)

def test_q3_1():
    assert is_close(calculate_distance(-2, -2, -2, -2), 0)

def test_q3_2():
    assert is_close(calculate_distance(3, 5, 9, 13), 10)

def test_q3_3():
    assert is_close(calculate_distance(0, 3, 4, 0), 5)

def test_q4_1():
    assert is_close(calculate_area(6.25, 4.25, 6.5), 12.75)

def test_q4_2():
    assert is_close(calculate_area(20.5, 20.5, 9), 90)

def test_q4_3():
    assert is_close(calculate_area(14.32, 18.53, 5.612), 30.027385522357424)

if __name__ == '__main__':
    tests_q1 = [test_q1_1, test_q1_2, test_q1_3]
    q1_passed = 0
    for test in tests_q1:
        try:
            test()
            q1_passed += 1
        except:
            pass
    print(f'Question 1: {q1_passed}/{len(tests_q1)} Tests Passed')

    tests_q2 = [test_q2_1, test_q2_2, test_q2_3]
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

    tests_q4 = [test_q4_1, test_q4_2, test_q4_3]
    q4_passed = 0
    for test in tests_q4:
        try:
            test()
            q4_passed += 1
        except:
            pass
    print(f'Question 4: {q4_passed}/{len(tests_q4)} Tests Passed')
