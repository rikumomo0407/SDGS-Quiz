"""
-----------------------------------------------
(解答)
-----------------------------------------------
1.貧困をなくそう
2.飢餓をゼロに
3.すべての人に健康と福祉を
4.質の高い教育をみんなに
5.ジェンダー平等を実現しよう
6.安全な水とトイレを世界中に
7.エネルギーをみんなにそしてクリーンに
8.働きがいも経済成長も
9.産業と技術革新の基盤をつくろう
10.人や国の不平等をなくそう
11.住み続けられるまちづくりを
12.つくる責任つかう責任
13.気候変動に具体的な対策を
14.海の豊かさを守ろう
15.陸の豊かさもまもろう
16.平和と公正をすべての人に
17.パートナーシップで目標を達成しよう
-----------------------------------------------
"""

#program

import cv2
import random
import time

# path = [
#     "img_quiz\icon_1.png",
#     "img_quiz\icon_2.png",
#     "img_quiz\icon_3.png",
#     "img_quiz\icon_4.png",
#     "img_quiz\icon_5.png",
#     "img_quiz\icon_6.png",
#     "img_quiz\icon_7.png",
#     "img_quiz\icon_8.png",
#     "img_quiz\icon_9.png",
#     "img_quiz\icon_10.png",
#     "img_quiz\icon_11.png",
#     "img_quiz\icon_12.png",
#     "img_quiz\icon_13.png",
#     "img_quiz\icon_14.png",
#     "img_quiz\icon_15.png",
#     "img_quiz\icon_16.png",
#     "img_quiz\icon_17.png"
# ]

finished = []
correct = 0
for i in range(17):
    print("\r//////////問題" + str(len(finished) + 1) + "//////////")
    while(True):
        order = random.randrange(17)
        if (order in finished) == 0:
            finished.append(order)
            break
    img = cv2.imread("img_quiz\icon_" + str(order + 1) + ".png")
    #img = cv2.imread(path[order])
    cv2.imshow("Question" + str(len(finished)), img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    while(True):
        print("答えを入力 >>> " ,end="")
        ans = input()
        if ans.isdecimal() == False:
            print("***1~17数字を入力してください***")
        elif int(ans) < 0 or 18 < int(ans):
            print("***1~17の範囲で入力してください***")
        else:
            break
    if int(ans) - 1 == order:
        print("正解!!")
        correct += 1
    else:
        print("不正解 (答え: " + str(order + 1) + ")")
    if i < 16:
        for i in reversed(range(4)):
            time.sleep(1)
            print("\r次の問題まで: " + str(i),end="")
print("//////////結果//////////")
print("正解率:" + str(correct) +"/17")
