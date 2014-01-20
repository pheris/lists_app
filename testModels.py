# coding=utf-8
import models
import unittest
import __builtin__

class TestStoreable(unittest.TestCase):

  def test_get(self):
    models.Storeable('wolf', 'lapus big')
    models.Storeable('fox', 'lapus small')
    self.assertEqual('lapus big', models.Storeable.get('wolf'))
    self.assertEqual('lapus small', models.Storeable.get('fox'))

  def test_total(self):
    initialTotal = models.Storeable.total()
    self.assertEqual(initialTotal,  models.Storeable.total())
    new_character_a = models.Storeable('Anna', 'Female')
    self.assertEqual(initialTotal + 1,  models.Storeable.total())
    new_character_b = models.Storeable('Bill', 'Male')
    self.assertEqual(initialTotal + 2,  models.Storeable.total())
    new_character_c = models.Storeable('Bill', 'Male 2')
    self.assertEqual(initialTotal + 2,  models.Storeable.total())

class TestCharacter(unittest.TestCase):

  def test_new(self):
    new_character_a = models.Character(u'a nāme')
    self.assertEqual(u'a nāme', new_character_a.name)
    new_character_b = models.Character('b nāme')
    self.assertEqual('b nāme', new_character_b.name)

  def test_mentions(self):
    john = models.Character('John')
    self.assertEqual(1, john.getMentions())
    john_copy = models.Character('John')
    self.assertEqual(2, john.getMentions())
    self.assertEqual(2, john_copy.getMentions())

  def test_eq(self):
    alice = models.Character(u'Ālice')
    bob = models.Character(u'Bôb')
    alice_copy = models.Character(u'Ālice')
    self.assertEqual(alice, alice)
    self.assertEqual(alice, alice_copy)
    self.assertNotEqual(alice, bob)

  def test_get(self):
    wolf = models.Character('wolf')
    fox = models.Character('fox')
    self.assertEqual(wolf, models.Character.get('wolf'))
    self.assertEqual(fox, models.Character.get('fox'))

class TestReference(unittest.TestCase):

  def assert_new_reference(self, text, chapter, verses, characters):
    new_reference = models.Reference(text, characters)
    self.assertEqual(new_reference.text, text)
    self.assertEqual(new_reference.chapter, chapter)
    self.assertEqual(new_reference.verses, verses)
    self.assertEqual(new_reference.characters, characters)

  def test_new(self):
    angels = models.Character('angels')
    wolf = models.Character('wolf')
    snake = models.Character('snake')
    characters = [angels, wolf, snake]
    self.assert_new_reference('2:12', 2, [12], characters)
    self.assert_new_reference('2:13, 14, 15', 2, [13, 14, 15], characters)
    self.assert_new_reference('3:12-14', 3, [12, 13, 14], characters)
    self.assert_new_reference('15:12-14, 16', 15, [12, 13, 14, 16], characters)
    self.assert_new_reference('17:12-14, 16-18', 17, [12, 13, 14, 16, 17, 18],
                              characters)
    self.assert_new_reference('101:12-14, 16, 18-20', 101,
                              [12, 13, 14, 16, 18, 19, 20], characters)

  def test_eq(self):
    characters = [models.Character('Gog')]
    reference_a = models.Reference('2:13, 14, 15', characters)
    reference_a_copy = models.Reference('2:13, 14, 15', characters)
    reference_different = models.Reference('15:16-19, 20', characters)
    reference_same_chapter= models.Reference('2:10, 11, 12', characters)
    reference_same_verses = models.Reference('3:13, 14, 15', characters)
    self.assertEqual(reference_a, reference_a)
    self.assertEqual(reference_a, reference_a_copy)
    self.assertNotEqual(reference_a, reference_different)
    self.assertNotEqual(reference_a, reference_same_chapter)
    self.assertNotEqual(reference_a, reference_same_verses)

  def test_get(self):
    characters = [models.Character('Magog')]
    reference_c = models.Reference('11:13, 14, 15', characters)
    reference_d = models.Reference('112:1-3', characters)
    self.assertEqual(reference_c, models.Reference.get('11:13, 14, 15'))
    self.assertEqual(reference_d, models.Reference.get('112:1-3'))

class TestReferenceList(unittest.TestCase):

  def test_new(self):
    simple_list_text = u'2:30-38 angels, Ādam; 2:34, 36 Iblīs; 2:35-36, 38 Ādam’s wife'
    simple_reference_list = models.ReferenceList(simple_list_text)
    angels_reference = simple_reference_list.references[0]
    print(simple_reference_list.characters.keys())
    self.assertEqual(simple_reference_list.characters['angels'],
      models.Character('angels'))
    self.assertEqual(simple_reference_list.characters['Ādam'],
      models.Character('Ādam'))
    self.assertEqual(simple_reference_list.characters['Iblīs'],
      models.Character('Iblīs'))
    self.assertEqual(simple_reference_list.characters['Ādam’s wife'],
      models.Character('Ādam’s wife'))
    self.assertEqual(angels_reference.chapter, 2)
    self.assertEqual(angels_reference.verses, range(30, 39))
    self.assertEqual(angels_reference.characters[0],
      models.Character('angels'))
    self.assertEqual(angels_reference.characters[1], models.Character('Ādam'))
    iblis_reference = simple_reference_list.references[1]
    self.assertEqual(iblis_reference.chapter, 2)
    self.assertEqual(iblis_reference.verses, [34, 36])
    self.assertEqual(iblis_reference.characters[0], models.Character('Iblīs'))
    adam_wife_reference = simple_reference_list.references[2]
    self.assertEqual(adam_wife_reference.chapter, 2)
    self.assertEqual(adam_wife_reference.verses, [35, 36, 38])
    self.assertEqual(adam_wife_reference.characters[0],
      models.Character('Ādam’s wife'))

if __name__ == '__main__':
  unittest.main()