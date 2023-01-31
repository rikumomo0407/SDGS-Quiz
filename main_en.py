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
    "img_quiz\sdg_icon_01_ja_2.png",
    "img_quiz\sdg_icon_02_ja_2.png",
    "img_quiz\sdg_icon_03_ja_2.png",
    "img_quiz\sdg_icon_04_ja_2.png",
    "img_quiz\sdg_icon_05_ja_2.png",
    "img_quiz\sdg_icon_06_ja_2.png",
    "img_quiz\sdg_icon_07_ja_2.png",
    "img_quiz\sdg_icon_08_ja_2.png",
    "img_quiz\sdg_icon_09_ja_2.png",
    "img_quiz\sdg_icon_10_ja_3.png",
    "img_quiz\sdg_icon_11_ja_2.png",
    "img_quiz\sdg_icon_12_ja_2.png",
    "img_quiz\sdg_icon_13_ja_2.png",
    "img_quiz\sdg_icon_14_ja_2.png",
    "img_quiz\sdg_icon_15_ja_2.png",
    "img_quiz\sdg_icon_16_ja_2.png",
    "img_quiz\sdg_icon_17_ja_2.png"
]

finished = []
correct = 0
for i in range(17):
    print("\r//////////Question" + str(len(finished) + 1) + "//////////")
    while(True):
        order = random.randrange(17)
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
            print("***Input number range 1~17***")
        elif int(ans) < 0 or 18 < int(ans):
            print("***Input number range 1~17***")
        else:
            break
    if int(ans) - 1 == order:
        print("Correct!!")
        correct += 1
    else:
        print("Incorrect (Answer: " + str(order + 1) + ")")
    if i < 16:
        for i in reversed(range(4)):
            time.sleep(1)
            print("\rNext question: " + str(i),end="")
print("//////////Result//////////")
print("Accuracy rate:" + str(correct) +"/17")
