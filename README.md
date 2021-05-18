# training-data

这里面存放了一些经过我处理过的神经网络训练数据，为了方便使用我全部保存为了 [TensorFlow Dataset Cache](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#cache) 文件格式，使用时只需要通过以下代码就可以加载使用：

```python
>>> data = tf.data.Dataset.from_generator(lambda: None, output_signature=tf.TensorSpec(shape=(对应形状,), dtype=对应类型))
>>> data = data.cache('缓存文件路径（不包含扩展名）')
>>> # 查看数据
>>> print(next(data.as_numpy_iterator()))
```

## 数据集列表

-   语音识别
    -   中文
        -   [THCHS30](./speech_recognition/chinese/THCHS30/README.md)
        -   [ST-CMDS](./speech_recognition/chinese/ST-CMDS/README.md)
        -   [AISHELL 开源版](./speech_recognition/chinese/AISHELL开源版/README.md)
        -   [Primewords-Set1](./speech_recognition/chinese/Primewords-Set1/README.md)
        -   [AIDataTang-200zh](./speech_recognition/chinese/AIDataTang-200zh/README.md)
        -   [MagicData](./speech_recognition/chinese/MagicData/README.md)
        -   [CN-Celeb](./speech_recognition/chinese/CN-Celeb/README.md)
