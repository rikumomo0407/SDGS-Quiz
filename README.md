# SDGS-Quiz
学校のテスト対策で作りました。以下に記載した画像の表示部分を変更すれば他のクイズにも作り変えれると思います。

```
img = cv2.imread(path[order])
cv2.imshow("Question" + str(len(finished)), img)
cv2.waitKey()
cv2.destroyAllWindows()
```