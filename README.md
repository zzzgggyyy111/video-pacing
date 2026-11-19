# 视频帧调度：帧时、截止与丢帧

播放器帧间隔不均、掉帧统计偏少：帧时没有取倒数，下一截止没有向上对齐，丢帧没有按迟到时间取整，队列延迟没有乘帧数，垂直同步没有按刷新率对齐，空输入崩，批量调度只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
video/__init__.py
video/pacing.py
tests/test_pacing.py
```

## 当前状态

`video/pacing.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_pacing.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 帧时取倒数
2. 截止向上对齐
3. 丢帧按迟到取整
4. 队列延迟乘帧数
5. 垂直同步对齐
6. 空输入兜底

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `video/pacing.py`
后 15 条用例应全部通过。
