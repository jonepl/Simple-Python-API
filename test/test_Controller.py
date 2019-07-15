import pytest

from app.controllers.Controller import Controller

def test_Controller_base_class():
    with pytest.raises(TypeError) as e:
        controller = Controller()
