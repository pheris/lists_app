# coding=utf-8
import models
import unittest
import __builtin__


class TestCharacter(unittest.TestCase):

  def test_new(self):
    expected_name = 'a nāme'
    new_character = models.Character(expected_name)
    self.assertEqual(new_character.name, expected_name)

  def test_eq(self):
    alice = models.Character('Ālice')
    bob = models.Character('Bôb')
    alice_copy = models.Character('Ālice')
    self.assertEqual(alice, alice_copy)
    self.assertNotEqual(alice, bob)

class TestReference(unittest.TestCase):

  def assert_new_reference(self, reference_text, chapter, verses):
    new_reference = models.Reference(reference_text)
    self.assertEqual(new_reference.chapter, chapter)
    self.assertEqual(new_reference.verses, verses)

  def test_new(self):
    self.assert_new_reference('2:12', 2, [12])
    self.assert_new_reference('2:13, 14, 15', 2, [13, 14, 15])
    self.assert_new_reference('3:12-14', 3, [12, 13, 14])
    self.assert_new_reference('15:12-14, 16', 15, [12, 13, 14, 16])
    self.assert_new_reference('17:12-14, 16-18', 17, [12, 13, 14, 16, 17, 18])
    self.assert_new_reference('101:12-14, 16, 18-20', 101,
                              [12, 13, 14, 16, 18, 19, 20])

class TestCharacterList(unittest.TestCase):

  def assert_new_character_list(self, list_text, characters, chapter, verses):
    new_list = models.CharacterList(list_text)
    for i, character in enumerate(new_list.characters):
      self.assertEqual(character, characters[i])
    self.assertEqual(new_list.reference.chapter, chapter)
    self.assertEqual(new_list.reference.verses, verses)

  def test_new(self):
    self.assert_new_reference('2:12', 2, [12])
    self.assert_new_reference('2:13, 14, 15', 2, [13, 14, 15])
    self.assert_new_reference('3:12-14', 3, [12, 13, 14])
    self.assert_new_reference('15:12-14, 16', 15, [12, 13, 14, 16])
    self.assert_new_reference('17:12-14, 16-18', 17, [12, 13, 14, 16, 17, 18])
    self.assert_new_reference('101:12-14, 16, 18-20', 101,
                              [12, 13, 14, 16, 18, 19, 20])

if __name__ == '__main__':
  unittest.main()