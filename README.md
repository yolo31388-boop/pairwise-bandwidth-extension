# pairwise-bandwidth-extension

## 领域

游戏、图形与多媒体

## 主题

窄带语音带宽扩展与高频重建

## 说明

抗镜像谱搬移、高频包络平滑、块边界状态携带。

初始状态下 `av/bandwidth_ext.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
