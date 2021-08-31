from unittest import TestCase

from mock import patch

from src.lib.split_edie_walk import split_edie_walk
from .test_utils import create_options


class TestSplitEdieWalk(TestCase):

    @patch('src.lib.split_edie_walk.render')
    def test_split_edie_walk(self, render):
        options = create_options(num_pixels=10, step_size=255)
        split_edie_walk(options)
