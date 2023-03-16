import unittest

from main import process_text


class TestProcessText(unittest.TestCase):
    def test_replace_spaces(self):
        self.assertEqual(process_text('input_1.txt', 'output_1.txt'), None)
        with open('output_1.txt', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'Доброе утро. Какой сегодня, чудесный день! Что будешь делать? 5 75. .. 65!')

    def test_remove_spaces_before_punctuation(self):
        self.assertEqual(process_text('input_2.txt', 'output_2.txt'), None)
        with open('output_2.txt', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '123. 123')

    def test_add_spaces_after_punctuation(self):
        self.assertEqual(process_text('input_3.txt', 'output_3.txt'), None)
        with open('output_3.txt', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'Привет. Привет')

    def test_multiple_spaces_before_punctuation(self):
        self.assertEqual(process_text('input_4.txt', 'output_4.txt'), None)
        with open('output_4.txt', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '1. 1')

    def test_multiple_spaces_between_words(self):
        self.assertEqual(process_text('input_5.txt', 'output_5.txt'), None)
        with open('output_5.txt', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'привет привет')
