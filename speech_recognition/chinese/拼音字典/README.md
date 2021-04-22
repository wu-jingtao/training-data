# 拼音字典

这里的拼音参考的是[《在线汉语字典》](http://xh.5156edu.com/pinyi.html)，在下面 `JSON` 文件里面除了包含的有从拼音到数字和从数字到拼音的映射之外，还包含一个特殊的属性 `count`，表示有多少种发音。

> [创建代码](./notebooks/创建拼音映射字典.ipynb)

-   [intonation_5.json](./pinyin_mapper/intonation_5.json)：包含五声声调的拼音，`1-4` 代表四种声调，`5` 代表轻声。
-   [intonation_4.json](./pinyin_mapper/intonation_4.json)：包含四声声调的拼音，`1-4` 代表四种声调。
-   [intonation_0.json](./pinyin_mapper/intonation_0.json)：无声调拼音。
-   [intonation_fuzzy.json](./pinyin_mapper/intonation_fuzzy.json)：无声调 + [模糊音](https://jingyan.baidu.com/article/636f38bb35428fd6b84610f5.html)。
