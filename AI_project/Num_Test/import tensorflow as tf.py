import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras import layers

def predict_digit(img_path,model):
    # 加载图像并转换为28x28像素
    img = image.load_img(img_path, color_mode='grayscale', target_size=(28, 28))
    #导出img图片到F:/AI_project/Num_Test/img.png
    img.save('F:/AI_project/Num_Test/img.png')
    # 将图像转换为数组并进行归一化
    img_array = image.img_to_array(img)//255.0
    # 重塑数组以符合模型输入要求
    img_array = img_array.reshape(1, 28, 28, 1)
    # 使用模型进行预测
    predictions = model.predict(img_array)
    # 获取概率最高的类别作为预测结果
    return np.argmax(predictions)

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # 设置仅在需要时进行内存增长
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        # 设置仅使用第一个GPU设备
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
        # 指定要使用的CUDA核心
        tf.config.experimental.set_virtual_device_configuration(
            gpus[0],
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=5120)]
        )
    except RuntimeError as e:
        print(e)

mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 将像素值缩放到0到1之间
train_images = train_images / 255.0
test_images = test_images / 255.0
model = tf.keras.Sequential([
    layers.Reshape(target_shape=(28, 28, 1), input_shape=(28, 28)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5, batch_size=32)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc}')
predictions = model.predict(test_images)

# 使用函数进行预测
img_path = "F:/AI_project/Num_Test/img/3.jpg"  # 替换为您的图片路径
predicted_digit = predict_digit(img_path, model)
print("Predicted digit:", predicted_digit)


#保存模型
model.save('F:/AI_project/Num_Test/model.h5')
model = tf.keras.models.load_model('F:/AI_project/Num_Test/model.h5')

#使用模型进行预测
predicted_digit = predict_digit(img_path, model)
print("Predicted digit:", predicted_digit)
img = image.load_img(img_path, color_mode='grayscale', target_size=(28, 28))
plt.imshow(img)
plt.show()
