import tensorflow as tf
from tensorflow.keras import models
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras.callbacks import TensorBoard
tensorboard_callback = TensorBoard(log_dir='./logs')#tensorboard的日志文件
gpus = tf.config.experimental.list_physical_devices('GPU')#列出所有的GPU
if gpus:
    try:
        # 设置仅在需要时进行内存增长
        for gpu in gpus:#这里虽然是循环，但我们只有一个gpu。也许别人可能有很多
            tf.config.experimental.set_memory_growth(gpu, True)#这里的True表示，在需要时进行内存增长
        # 设置仅使用第一个GPU设备
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')#只有一个gpu设备所以是零
        # 指定要使用的CUDA核心
        tf.config.experimental.set_virtual_device_configuration(
            gpus[0],
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=5120)]#5120是设置显存的大小，8G的显存，自己得留点
        )
    except RuntimeError as e:#如果设置显存失败，则会抛出异常
        print(e)

mnist = tf.keras.datasets.mnist # 加载MNIST数据集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data() # 加载训练集和测试集，分割数据集
early_stopping = tf.keras.callbacks.EarlyStopping(patience=3)# 早停(patience=3)当三轮验证集正确率不提升时停止训练
# 将像素值缩放到0到1之间(归一化)
train_images = train_images / 255.0
test_images = test_images / 255.0
# 构建模型
model = tf.keras.Sequential([#构建一个包含四个层的模型
    layers.Reshape(target_shape=(28, 28, 1), input_shape=(28, 28)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])#编译(配置)模型
'''这行代码为一个神经网络模型配置了一个优化器、一个损失函数和一些指标。

optimizer='adam' 意味着使用Adam优化器来最小化损失函数。Adam优化器是一种常用的梯度下降优化算法，它在更新权重时可以自适应地调整学习率。
loss=tf.keras.losses.SparseCategoricalCrossentropy() 意味着使用稀疏分类交叉熵作为损失函数。稀疏分类交叉熵是一种用于多分类问题的损失函数，它假设 ground truth 的标签是稀疏编码的，即只有一个标签值是1，其余都为0。
metrics=['accuracy'] 意味着计算并显示模型在每个epoch结束时的准确率。准确率是分类正确的样本数与总样本数的比例。'''
model.fit(train_images, train_labels, epochs=50,  validation_data=(test_images, test_labels), batch_size=32, callbacks=[early_stopping,tensorboard_callback])# 训练模型(callback传参到25行位置) 
test_loss, test_acc = model.evaluate(test_images, test_labels)#测试模型
print(f'Test accuracy: {test_acc}')#打印测试集准确率

#保存模型
model.save('F:/AI_project/Num_Test2/model.h5')
new_model = tf.keras.models.load_model('F:/AI_project/Num_Test2/model.h5')#加载模型
new_model.summary()#打印模型结构
for test_image, test_label in zip(test_images[:10], test_labels[:10]):#打印测试集前十个样本的预测结果
    test_image = test_image.reshape((1, 28, 28, 1))
    prediction = new_model.predict(test_image)#预测结果
    print(f'Label: {test_label}')
    print(f'Prediction: {np.argmax(prediction)}')
    print(f'Probability: {prediction[0]}')
    print()

