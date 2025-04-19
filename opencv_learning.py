import  cv2

'''
#读取图片
img = cv2.imread('train/twitter_19_31_0_0.jpg')

#显示图片，窗口名为第一个参数
cv2.imshow("img",img)

#等待用户按键，参数表示等待时间，0表示无限等待
cv2.waitKey(0)

#关闭所有opencv的窗口
cv2.destroyAllWindows()
#打印出来是一个三维矩阵
print(img.shape)

#打印出来是一个二维矩阵，此时的img是一个灰度图像
img = cv2.imread("train/twitter_19_31_0_0.jpg",cv2.IMREAD_GRAYSCALE)
print(img.shape)


vc = cv2.VideoCapture("487fe23d70c213074f435fb0b4c30749.mp4")
#读取视频
if vc.isOpened():
    open,frame = vc.read()
else:
    open = False

#展示视频，当视频播放完或键盘按下q就退出
while open:
    ret,frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #将视频变为灰度
        cv2.imshow('result',gray)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
vc.release()
cv2.destroyAllWindows()
'''
img2 = cv2.imread("train/twitter_19_31_0_3.jpg")
cat = img2[0:300,0:500]# 按照二维数组的形式对图片进行截取
cv2.imshow('cat', cat)
cv2.waitKey(0)
cv2.destroyAllWindows()

#对图片进行颜色通道提取
b,g,r = cv2.split(img2)

#与上面相反，对图片颜色通道合并
img2 = cv2.merge((b,g,r))

top_size,bottoom_size,left_size,right_size = (50,50,50,50)
