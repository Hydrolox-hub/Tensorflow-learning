import tensorflow as tf
from tensorflow.keras import layers, models

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
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=8192)]
        )
    except RuntimeError as e:
        print(e)

# 定义早停的参数 
#early_stopping = tf.keras.callbacks.EarlyStopping(patience=3)
#ResNet
def build_resnet(input_shape, num_classes):
    # 输入层
    inputs = tf.keras.Input(shape=input_shape)

    # 预处理
    x = layers.Conv2D(16, kernel_size=3, padding='same', activation='relu')(inputs)

    # 残差块的堆叠
    num_layers = [9, 9, 9]
    filters = [16, 32, 64]
    strides = [1, 2, 2]

    for i in range(len(num_layers)):
        # 第一个残差块的跨层连接
        y = layers.Conv2D(filters[i], kernel_size=3, strides=strides[i], padding='same')(x)
        y = layers.BatchNormalization()(y)
        y = layers.Activation('relu')(y)

        # 残差块的堆叠
        for _ in range(num_layers[i] - 1):
            x = layers.Conv2D(filters[i], kernel_size=3, padding='same')(y)
            x = layers.BatchNormalization()(x)
            x = layers.Activation('relu')(x)
            x = layers.Conv2D(filters[i], kernel_size=3, padding='same')(x)
            x = layers.BatchNormalization()(x)
            x = layers.Add()([x, y])  # 残差连接
            x = layers.Activation('relu')(x)

            y = x  # 更新残差跳跃连接输出

    # 全局平均池化层
    x = layers.GlobalAveragePooling2D()(x)

    # 分类器（全连接层）
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    # 创建模型
    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    return model

# 设置输入形状和类别数量
input_shape = (32, 32, 3)
num_classes = 10

# 构建模型
model = build_resnet(input_shape, num_classes)

# 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 加载 CIFAR-10 数据集
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# 数据预处理
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# 训练模型
model.fit(x_train, y_train, batch_size=64, epochs=50, validation_data=(x_test, y_test))
#model.fit(x_train, y_train, batch_size=64, epochs=50, validation_data=(x_test, y_test),callbacks=[early_stopping])
# 评估模型
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
