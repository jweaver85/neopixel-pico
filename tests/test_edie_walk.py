from unittest import TestCase

from mock import patch

import src.lib.utils
from src.lib.edie_walk import (
    RED, BLUE, WHITE, edie_walk
)
from .test_utils import create_options


class TestEdieWalk(TestCase):

    @patch("src.lib.edie_walk.render")
    def test_edie_walk(self, render):
        options = create_options(num_pixels=3, step_size=255)
        edie_walk(options)
        render.assert_called_once_with(options)
        self.assertEqual(len(options.buffer), 4)

