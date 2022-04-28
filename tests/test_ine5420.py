from ine5420 import transform
from ine5420.utils import BoundaryRepresentation
import pytest


@pytest.fixture
def boundary_0_0_100_100():
    return BoundaryRepresentation(x_min=0, y_min=0, x_max=100, y_max=100)


@pytest.fixture
def boundary_50_0_100_100():
    return BoundaryRepresentation(x_min=50, y_min=0, x_max=100, y_max=100)


@pytest.fixture
def boundary_0_50_100_100():
    return BoundaryRepresentation(x_min=0, y_min=50, x_max=100, y_max=100)


@pytest.fixture
def boundary_50_50_100_100():
    return BoundaryRepresentation(x_min=50, y_min=50, x_max=100, y_max=100)


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
    assert transform.x_viewport_transform(
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
    assert transform.y_viewport_transform(
        y_window, y_window_min, y_window_max, y_viewport_min, y_viewport_max) == expected


def test_transform_viewport_coordinates_1(boundary_0_0_100_100):
    assert transform.transform_viewport_coordinates(
        0, 0, boundary_0_0_100_100, boundary_0_0_100_100) == (0, 100)

    assert transform.transform_viewport_coordinates(
        0, 25, boundary_0_0_100_100, boundary_0_0_100_100) == (0, 75)

    assert transform.transform_viewport_coordinates(
        25, 0, boundary_0_0_100_100, boundary_0_0_100_100) == (25, 100)

    assert transform.transform_viewport_coordinates(
        25, 25, boundary_0_0_100_100, boundary_0_0_100_100) == (25, 75)


def test_transform_viewport_coordinates_2(boundary_0_0_100_100, boundary_50_0_100_100):
    assert transform.transform_viewport_coordinates(
        0, 0, boundary_0_0_100_100, boundary_50_0_100_100) == (0, 100)

    assert transform.transform_viewport_coordinates(
        0, 25, boundary_0_0_100_100, boundary_50_0_100_100) == (0, 75)

    assert transform.transform_viewport_coordinates(
        25, 0, boundary_0_0_100_100, boundary_50_0_100_100) == (12.5, 100)

    assert transform.transform_viewport_coordinates(
        25, 25, boundary_0_0_100_100, boundary_50_0_100_100) == (12.5, 75)


def test_transform_viewport_coordinates_3(boundary_0_0_100_100, boundary_0_50_100_100):
    assert transform.transform_viewport_coordinates(
        0, 0, boundary_0_0_100_100, boundary_0_50_100_100) == (0, 50)

    assert transform.transform_viewport_coordinates(
        0, 25, boundary_0_0_100_100, boundary_0_50_100_100) == (0, 37.5)

    assert transform.transform_viewport_coordinates(
        25, 0, boundary_0_0_100_100, boundary_0_50_100_100) == (25, 50)

    assert transform.transform_viewport_coordinates(
        25, 25, boundary_0_0_100_100, boundary_0_50_100_100) == (25, 37.5)
