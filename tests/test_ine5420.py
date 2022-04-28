import ine5420.transform as transform
import pytest


@pytest.mark.parametrize(
    "x_window, x_window_min, x_window_max, x_viewport_min, x_viewport_max, expected",
    [
        (0,   0, 100,  0, 100,    0),
        (0,  50, 100,  0, 100, -100),
        (0,   0, 100, 50, 100,    0),
        (0,  50, 100, 50, 100,  -50),
        (25,  0, 100,  0, 100,   25),
        (25, 50, 100,  0, 100,  -50),
        (25,  0, 100, 50, 100, 12.5),
        (25, 50, 100, 50, 100,  -25),
    ],
)
def test_x_viewport(x_window, x_window_min, x_window_max, x_viewport_min, x_viewport_max, expected):
    assert transform.x_viewport(
        x_window, x_window_min, x_window_max, x_viewport_min, x_viewport_max) == expected


@pytest.mark.parametrize(
    "y_window, y_window_min, y_window_max, y_viewport_min, y_viewport_max, expected",
    [
        (0,   0, 100,  0, 100,    100),
        (0,  50, 100,  0, 100,   5150),
        (0,   0, 100, 50, 100,     50),
        (0,  50, 100, 50, 100,   2575),
        (25,  0, 100,  0, 100,     75),
        (25, 50, 100,  0, 100,   5125),
        (25,  0, 100, 50, 100,   37.5),
        (25, 50, 100, 50, 100, 2562.5),
    ],
)
def test_y_viewport(y_window, y_window_min, y_window_max, y_viewport_min, y_viewport_max, expected):
    assert transform.y_viewport(
        y_window, y_window_min, y_window_max, y_viewport_min, y_viewport_max) == expected
