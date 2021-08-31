from unittest import TestCase

from mock import patch

from src.lib.sparkle_shift import sparkle_shift
from .test_utils import create_options


class TestSparkleShift(TestCase):

    @patch('src.lib.sparkle_shift.render')
    def test_sparkle_shift(self, render):
        options = create_options(num_pixels=100, step_size=1)
        sparkle_shift(options)
        render.reset_mock()
        options.pixels.reset_mock()

        for i in range(options.num_pixels):
            sparkle_shift(options)
            self.assertEqual(len(options.colors), options.num_pixels)
            self.assertEqual(render.call_count, options.num_pixels)
            options.pixels.write.assert_called_once()
            options.pixels.reset_mock()
            render.reset_mock()
