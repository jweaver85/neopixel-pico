from unittest import TestCase

from mock import patch

from src.lib.sparkle import sparkle
from .test_utils import create_options


class TestSparkle(TestCase):

    @patch('src.lib.sparkle.render')
    def test_sparkle(self, render):
        options = create_options(num_pixels=100, step_size=1)
        sparkle(options)
        render.reset_mock()
        options.pixels.reset_mock()

        for i in range(options.num_pixels):
            sparkle(options)
            self.assertEqual(len(options.colors), options.num_pixels)
            self.assertEqual(render.call_count, options.num_pixels)
            options.pixels.write.assert_called_once()
            options.pixels.reset_mock()
            render.reset_mock()
