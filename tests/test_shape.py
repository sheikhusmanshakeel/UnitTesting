from unit_testing.shape import Square, Rhombus
import pytest
from pytest import *
from unittest.mock import Mock


@pytest.fixture
def square():
    square = Square(3)
    yield square
    print("This is teardown")


def test_calculate_area(square, tmpdir):
    print("this is tmpdir: {0}".format(tmpdir))
    assert square.calculate_area() == 9


@pytest.mark.parametrize("shape, area", [
    (Square(1, 10), 100),
    (Square(2, 4), 16),
    (Rhombus(3, 3, 2), 3)
], ids=(lambda s: str(s.id)))
def test_areas_of_different_shapes(shape, area):
    assert shape.calculate_area() == area


def test_send():
    sq = Square(1, 3)
    shape_sender = Mock()
    sq.send_shape(shape_sender)
    print(shape_sender.mock_calls)
    shape_sender.send.assert_called_with("Square")
