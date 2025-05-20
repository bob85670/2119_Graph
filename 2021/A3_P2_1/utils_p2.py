import A3_P2_1
"""Please do not edit any part of this code!"""

def score():

    score = 0
    test1 = (3, [[0,1,2], [1,2,3], [0,2,10]], 0, 2, 1)
    ans1 = 5
    
    test2 = (3, [[0,1,2], [1,2,3], [0,2,10]], 0, 2, 0)
    ans2 = 10
    

    
    tests = [(test1, ans1),(test2, ans2)]
    test_num = len(tests)
    s = A3_P2_1.Solution
    PASS = True
    # print("Before the test loop started")
    for i in range(test_num):
        n, edges, scr, dst, k = tests[i][0]
        s_a = s.theLeastPrice(A3_P2_1.Solution(), n, edges, scr, dst, k)
        # print(s_a, tests[n][1])
        if s_a == tests[i][1]:
            print("find one  equal")
            score += 100 / test_num
        else:
            print("You have passed " + str(i) + " out of " + str(test_num) + " test.")
            print("Your score is " + str(score))
            PASS = False
            break

    if PASS:
        print("You have passed " + str(test_num) + " tests")
        print("Your score is 100. Congratulation! (This is not your final score)")








