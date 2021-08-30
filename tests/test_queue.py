from unittest import TestCase

from src.lib.queue import queue
from src.lib.utils import randColor

class TestQueue(TestCase):

    def test_push(self):
        q_max = 10
        q = queue([1 for i in range(q_max)], q_max)

        for _ in range(q_max * 2):
            q.push(2)

        self.assertListEqual(list(q), [2 for _ in range(q_max)])

    def test_pop_empty_queue(self):
        q = queue([], 10)
        self.assertEqual(q.pop(), None)
        self.assertListEqual(list(q), [])

    def test_pop_returns_item(self):
        item = randColor()
        q = queue([item], 13)
        returned = q.pop()
        self.assertEqual(item, returned)

    def test_pop_empty(self):
        q = queue([], 35)
        returned = q.pop()
        self.assertListEqual(list(q), [])
        self.assertEqual(returned, None)
