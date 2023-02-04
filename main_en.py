"""
-----------------------------------------------
(Answers)
-----------------------------------------------
1.No Poverty
2.Zero Hunger
3.Good Health and Well-Being
4.Quality Education
5.Gender Equality
6.Clean Water and Sanitation
7.Affordable and Clean Energy
8.Decent Work and Economic Growth
9.Industry, Innovation and Infrastructure
10.Reduced Inequalities
11.Sustainable Cities and Communities
12.Responsible Consumption and Production
13.Climate Action
14.Life Below Water
15.Life On Land
16.Peace, Justice and Strong Institutions
17.Partnerships for the Goals
-----------------------------------------------
"""

#program

import cv2
import random
import time

path = [
    "img_quiz\icon_1.png",
    "img_quiz\icon_2.png",
    "img_quiz\icon_3.png",
    "img_quiz\icon_4.png",
    "img_quiz\icon_5.png",
    "img_quiz\icon_6.png",
    "img_quiz\icon_7.png",
    "img_quiz\icon_8.png",
    "img_quiz\icon_9.png",
    "img_quiz\icon_10.png",
    "img_quiz\icon_11.png",
    "img_quiz\icon_12.png",
    "img_quiz\icon_13.png",
    "img_quiz\icon_14.png",
    "img_quiz\icon_15.png",
    "img_quiz\icon_16.png",
    "img_quiz\icon_17.png"
]

finished = []
correct = 0
for i in range(len(path)):
    print("\r//////////Question" + str(len(finished) + 1) + "//////////")
    while(True):
        order = random.randrange(len(path))
        if (order in finished) == 0:
            finished.append(order)
            break
    img = cv2.imread(path[order])
    cv2.imshow("Question" + str(len(finished)), img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    while(True):
        print("Input correct number >>> " ,end="")
        ans = input()
        if ans.isdecimal() == False:
            print("***Enter a number in the range 1~" + str(len(path)) + "***")
        elif int(ans) < 0 or 18 < int(ans):
            print("***Enter a number in the range 1~" + str(len(path)) + "***")
        else:
            break
    if int(ans) - 1 == order:
        print("Correct!!")
        correct += 1
    else:
        print("Wrong (Answer: " + str(order + 1) + ")")
    if i < 16:
        for i in reversed(range(4)):
            time.sleep(1)
            print("\rNext question: " + str(i),end="")
print("//////////Result//////////")
print("Accuracy rate:" + str(correct) + "/" + str(len(path)))
