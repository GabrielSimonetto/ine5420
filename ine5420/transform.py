def x_viewport_transform(
    x_window,
    x_window_min,
    x_window_max,
    x_viewport_min,
    x_viewport_max
):
    return (
        (x_window - x_window_min) / (x_window_max - x_window_min)
        * (x_viewport_max - x_viewport_min)
    )


def y_viewport_transform(
    y_window,
    y_window_min,
    y_window_max,
    y_viewport_min,
    y_viewport_max
):
    return (
        (1 - ((y_window - y_window_min) / y_window_max - y_window_min))
        * (y_viewport_max - y_viewport_min)
    )


def transform_viewport_coordinates(x, y, window_coordinates, viewport_coordinates):
    xvp = x_viewport_transform(
        x,
        window_coordinates.x_min,
        window_coordinates.x_max,
        viewport_coordinates.x_min,
        viewport_coordinates.x_max,
    )
    yvp = y_viewport_transform(
        y,
        window_coordinates.y_min,
        window_coordinates.y_max,
        viewport_coordinates.y_min,
        viewport_coordinates.y_max,
    )
    return (xvp, yvp)
