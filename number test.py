import tensorflow as tf
from tensorflow.keras import layers
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
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)]
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
