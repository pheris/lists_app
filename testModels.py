# coding=utf-8
import models
import unittest
import __builtin__


class TestCharacter(unittest.TestCase):

  def test_new(self):
    expected_name = 'a nāme'
    expected_reference_a = models.Reference('101:12-14')
    expected_reference_b = models.Reference('9:12')
    new_character = models.Character(expected_name)
    self.assertEqual(new_character.name, expected_name)
    self.assertEqual(new_character.references)

  def test_eq(self):
    alice = models.Character('Ālice')
    bob = models.Character('Bôb')
    alice_copy = models.Character('Ālice')
    self.assertEqual(alice, alice)
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

  def test_eq(self):
    alice = models.Character('Ālice')
    reference_a = models.Reference('2:13, 14, 15')
    reference_a_copy = models.Reference('2:13, 14, 15')
    reference_different = models.Reference('15:16-19, 20')
    reference_same_chapter= models.Reference('2:10, 11, 12')
    reference_same_verses = models.Reference('3:13, 14, 15')
    self.assertEqual(reference_a, reference_a)
    self.assertEqual(reference_a, reference_a_copy)
    self.assertNotEqual(reference_a, reference_different)
    self.assertNotEqual(reference_a, reference_same_chapter)
    self.assertNotEqual(reference_a, reference_same_verses)

class TestCharacterReference(unittest.TestCase):

  def test_new(self):
    expected_name = 'a nāme'
    expected_reference_a = models.Reference('101:12-14')
    expected_reference_b = models.Reference('9:12')
    new_character = models.Character(expected_name)
    self.assertEqual(new_character.name, expected_name)
    self.assertEqual(new_character.references)

  def test_eq(self):
    alice = models.Character('Ālice')
    bob = models.Character('Bôb')
    alice_copy = models.Character('Ālice')
    self.assertEqual(alice, alice)
    self.assertEqual(alice, alice_copy)
    self.assertNotEqual(alice, bob)

# class TestCharacterList(unittest.TestCase):

#   def assert_new_character_list(self, list_text, chapter, character_verse_map):
#     new_list = models.CharacterList(list_text)
#     for i, character in enumerate(new_list.characters):
#       self.assertEqual(character, characters[i])
#     self.assertEqual(new_list.reference.chapter, chapter)
#     self.assertEqual(new_list.reference.verses, verses)

#   def test_new(self):
#     self.assert_new_character_list((u'2:30-38 angels, Ādam; 2:34, 2:36 Iblīs;'
#                                     u'2:35-36, 2:38 Ādam’s wife'),
#                                     2,
#                                     [12])


if __name__ == '__main__':
  unittest.main()