"""视频帧调度：帧时、截止与丢帧：待实现的核心模块。"""


def frame_time(fps):
    """帧时。"""
    raise NotImplementedError

def next_deadline(now, frame):
    """下一截止。"""
    raise NotImplementedError

def dropped(late, frame):
    """丢帧数。"""
    raise NotImplementedError

def queue_latency(count, frame):
    """队列延迟。"""
    raise NotImplementedError

def vsync_align(time, refresh):
    """垂直同步对齐。"""
    raise NotImplementedError
