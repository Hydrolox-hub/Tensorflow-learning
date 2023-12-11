#使用'F:/AI_project/Num_Test2/model.h5'路径的模型进行预测
#使用'F:/AI_project/Num_Test2/img/1.jpg'路径的图片进行预测
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time 
import tensorflow as tf

#设置predict_digit函数
def predict_digit(img_path, model):
    img = image.load_img(img_path, color_mode='grayscale', target_size=(28, 28))# 加载图像并转换为28x28像素，为什么是28x28像素呢？因为我们之前在训练的时候，我们设置了输入图片的大小为28x28像素(minst数据集的输入图片大小为28x28像素)，所以这里也要设置成28x28像素
    x = image.img_to_array(img)//255.0  # 归一化
     # 重塑数组以符合模型输入要求
    x = x.reshape(1, 28, 28, 1)
    # 使用模型进行预测
    predictions = model.predict(x)
    # 获取概率最高的类别作为预测结果
    return np.argmax(predictions)
#设置model
model = load_model('F:/AI_project/Num_Test2/model.h5')
#图片路径
img_path2 = 'F:/AI_project/Num_Test2/img/2.jpg' 
img_path4 = 'F:/AI_project/Num_Test2/img/4.jpg' 
predicted_digit = predict_digit(img_path2, model)#调用预测函数
print("Predicted digit:", predicted_digit)
predicted_digit = predict_digit(img_path4, model)#调用预测函数
print("Predicted digit:", predicted_digit)
img2 = image.load_img(img_path2, color_mode='grayscale', target_size=(28, 28))
img4 = image.load_img(img_path4, color_mode='grayscale', target_size=(28, 28))
#将img2和img4拼在一起成为一张图片
img = np.concatenate((img2, img4), axis=1)
plt.imshow(img)
plt.show()
##plt.imshow(img2)
##plt.show()
##plt.imshow(img4)
##plt.show()

