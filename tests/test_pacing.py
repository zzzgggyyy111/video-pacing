import pytest

from video import pacing as mod

CASES = [
    ('frame_time', [60], 0.016666666666666666, True),
    ('frame_time', [0], 0.0, True),
    ('next_deadline', [1.01, 0.02], 1.02, True),
    ('dropped', [0.05, 0.02], 2, False),
    ('queue_latency', [3, 0.016], 0.048, True),
    ('vsync_align', [1.012, 60], 1.0166666666666666, True),
    ('vsync_align', [1.012, 0], 1.012, True),
    ('frame_time', [30], 0.03333333333333333, True),
    ('frame_time', [120], 0.008333333333333333, True),
    ('next_deadline', [0.0, 0.0], 0.0, True),
    ('dropped', [0.0, 0.02], 0, False),
    ('queue_latency', [0, 0.02], 0.0, True),
    ('vsync_align', [0.0, 60], 0.0, True),
    ('next_deadline', [0.02, 0.02], 0.02, True),
    ('dropped', [0.02, 0.0], 0, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_pacing_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
