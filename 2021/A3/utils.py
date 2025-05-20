import A3
"""Please do not edit any part of this code!"""

def score():

    score = 0
    test1 = ([[5,0], [6,0], [7,1,0], [8,1,0], [9,1]], 5, 9)
    ans1 = 3

    test2 = ([[5, 0], [6, 0], [7, 0], [8, 0]], 5, 0)
    ans2 = 1

    test3 = ([[5, 3, 1, 0], [6, 2, 1, 0], [7, 3, 2, 1], [8, 3, 2, 0]], 5, 7)
    ans3 = 2

    test4 = ([[5, 0], [6, 1, 0], [7, 2, 1], [8, 2]], 5, 8)
    ans4 = 4

    test5 = ([[5, 0], [6, 1], [7, 1], [8, 1]], 7, 5)
    ans5 = -1

    
    tests = [(test1, ans1),(test2, ans2),(test3, ans3),(test4, ans4),(test5, ans5)]
    test_num = len(tests)
    s = A3.Solution
    PASS = True
    # print("Before the test loop started")
    for n in range(test_num):
        routes, source, target = tests[n][0]
        s_a = s.leastNumBus(s.leastNumBus, routes, source, target)
        # print(s_a, tests[n][1])
        if s_a == tests[n][1]:
            print("find one  equal")
            score += 100 / test_num
        else:
            print("You have passed " + str(n) + " out of " + str(test_num) + " test.")
            print("Your current score is " + str(score))
            PASS = False
            break

    if PASS:
        print("You have passed " + str(test_num) + " tests")
        print("Your score is 100. Congratulation! (This is not your final score) ")






