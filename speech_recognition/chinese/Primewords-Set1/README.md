# [Primewords-Set1](http://www.openslr.org/47/)

> 包含了大约 `100` 小时的中文语音数据，语料库由 `296` 人用智能 `手机录制`。转录准确度大于 `98％`，置信水平为 `95％`。

#### 评价

1. 有些音频有背景噪音
1. 数据的正确率比较高，随机抽查了 `60` 条数据，只有 `3` 条有点小错误。
1. [详细分析报告](./notebooks/Primewords-Set1-数据分析报告.ipynb)。

#### 错误样本

| 编号                                 | 音频                                                    | 文本                                                    | 描述           |
| ------------------------------------ | ------------------------------------------------------- | ------------------------------------------------------- | -------------- |
| 7964b953-0a5e-40e4-8b9a-cc6a5b7c02da | [音频](./demo/7964b953-0a5e-40e4-8b9a-cc6a5b7c02da.mp3) | [文本](./demo/7964b953-0a5e-40e4-8b9a-cc6a5b7c02da.txt) | 漏字           |
| cd9d0249-22a4-4045-adfa-fa69219bb9d1 | [音频](./demo/cd9d0249-22a4-4045-adfa-fa69219bb9d1.mp3) | [文本](./demo/cd9d0249-22a4-4045-adfa-fa69219bb9d1.txt) | 漏字、念错     |
| 7dc1d0a4-4601-46ab-a460-2a2fa944cf33 | [音频](./demo/7dc1d0a4-4601-46ab-a460-2a2fa944cf33.mp3) | [文本](./demo/7dc1d0a4-4601-46ab-a460-2a2fa944cf33.txt) | 漏字           |
| 8ed03269-4335-4e93-a32e-9f248ce726c9 | [音频](./demo/8ed03269-4335-4e93-a32e-9f248ce726c9.mp3) | [文本](./demo/8ed03269-4335-4e93-a32e-9f248ce726c9.txt) | 念重复了很多字 |