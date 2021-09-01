from unittest import TestCase

from mock import patch

from lib.split_america_walk import split_america_walk
from .test_utils import create_options


class TestSplitAmericaWalk(TestCase):

    @patch('lib.split_america_walk.render')
    def test_split_america_walk(self, render):
        options = create_options(num_pixels=10, step_size=255)
        split_america_walk(options)

        # for i in range(options.num_pixels):
        #     split_america_walk(options)
        #     print('iteration: %s, len(colors): %s' % ((i+1), len(options.colors)))
        #     self.assertEqual(len(options.buffer), 4)
        #     self.assertEqual(len(options.colors), (2*i) + 1)