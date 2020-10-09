import cv2

image = cv2.imread("data.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


_1 = cv2.resize(image_gray, (150, 150), interpolation = cv2.INTER_LINEAR) 
_2 = cv2.resize(image_gray, (300, 300), interpolation = cv2.INTER_LINEAR) 
_3 = cv2.resize(image_gray, (600, 600), interpolation = cv2.INTER_LINEAR) 

cv2.imshow("bi_linear_1", _1)
cv2.imshow("bi_linear_2", _2)
cv2.imshow("bi_linear_3", _3)

cv2.waitKey(0)
cv2.destroyAllWindows()