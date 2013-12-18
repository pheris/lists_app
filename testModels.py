# coding=utf-8

import models
import unittest
import __builtin__

# class TestSequenceFunctions(unittest.TestCase):

#     def setUp(self):
#         self.seq = range(10)

#     def test_shuffle(self):
#         # make sure the shuffled sequence does not lose any elements
#         random.shuffle(self.seq)
#         self.seq.sort()
#         self.assertEqual(self.seq, range(10))

#         # should raise an exception for an immutable sequence
#         self.assertRaises(TypeError, random.shuffle, (1,2,3))

#     def test_choice(self):
#         element = random.choice(self.seq)
#         self.assertTrue(element in self.seq)

#     def test_sample(self):
#         with self.assertRaises(ValueError):
#             random.sample(self.seq, 20)
#         for element in random.sample(self.seq, 5):
#             self.assertTrue(element in self.seq)

class TestCharacter(unittest.TestCase):

  def test_new(self):
    expected_name = 'a nāme'
    new_character = models.Character(expected_name)
    self.assertEqual(new_character.name, expected_name) 

class TestReference(unittest.TestCase):

  def assert_new_reference(self, reference_text, expected_chapter, expected_verses):
    new_reference = models.Reference(reference_text)
    self.assertEqual(new_reference.chapter, expected_chapter)
    self.assertEqual(new_reference.verses, expected_verses)


  def test_new(self):
    self.assert_new_reference('2:12', 2, [12])
    self.assert_new_reference('3:12-14', 3, [12, 13, 14])
    self.assert_new_reference('15:12-14, 16', 15, [12, 13, 14, 16])
    self.assert_new_reference('17:12-14, 16-18', 17, [12, 13, 14, 16, 17, 18])
    self.assert_new_reference('101:12-14, 16, 18-20', 101, [12, 13, 14, 16, 18, 19, 20])
    

if __name__ == '__main__':
  unittest.main()