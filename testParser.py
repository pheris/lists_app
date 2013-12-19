# coding=utf-8

import unittest
import __builtin__
import models


class TestParser(unittest.TestCase):

  def assert_parse_line(self, line_text, expected_characters, expected_verses):
    new_reference = models.Reference(reference_text)
    self.assertEqual(new_reference.chapter, expected_chapter)
    self.assertEqual(new_reference.verses, expected_verses)


  def test_new(self):
    expected_name = 'a nāme'
    new_character = models.Character(expected_name)
    self.assertEqual(new_character.name, expected_name)

  def parse_line(self):
    x = 1

if __name__ == '__main__':
  unittest.main()