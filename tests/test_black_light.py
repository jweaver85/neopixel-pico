from unittest import TestCase

from mock import patch

from lib.black_light import black_light
from .test_utils import create_options


class TestBlackLight(TestCase):

    @patch('lib.black_light.render')
    def test_black_light(self, render):
        options = create_options(num_pixels=5, step_size=255)
        for i in range(options.num_pixels):
            black_light(options)
            self.assertEqual(len(options.buffer), options.num_pixels)
            self.assertEqual(len(options.colors), i + 1)
