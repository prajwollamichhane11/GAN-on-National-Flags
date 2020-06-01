import cv2
import os


rootPath = './Flags_2/'
listFile = os.listdir(rootPath)

# print(listFile)

for image in listFile:
    print(image)
    path = str(os.path.join(rootPath, image))

    img = cv2.imread(path,cv2.IMREAD_UNCHANGED)
    print('Original Dimensions : ',img.shape)

    dim = (64, 64)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)


    if resized.shape == (64, 64, 3):
        cv2.imwrite(f'./Resized/{image}',resized)

# cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()