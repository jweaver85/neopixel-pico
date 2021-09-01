from unittest import TestCase

from mock import patch

from lib.america_walk import america_walk
from .test_utils import create_options

class TestAmericaWalk(TestCase):

    @patch('lib.america_walk.render')
    def test_america_walk(self, render):
        options = create_options(num_pixels=3, step_size=255)

        for i in range(3):
            america_walk(options)
            self.assertEqual(len(options.buffer), 4)
            self.assertEqual(len(options.colors), i+1)
