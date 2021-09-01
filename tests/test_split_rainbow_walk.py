from unittest import TestCase

from mock import patch

from lib.split_rainbow_walk import split_rainbow_walk
from .test_utils import create_options


class TestSplitRainbowWalk(TestCase):

    @patch('lib.split_rainbow_walk.render')
    def test_split_rainbow_walk(self, render):
        options = create_options(num_pixels=10, step_size=255)
        split_rainbow_walk(options)