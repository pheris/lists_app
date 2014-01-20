# coding=utf-8
from reference_list_manager import *
import unittest
import __builtin__


class TestReferenceListManager(unittest.TestCase):

  def test_new(self):
    manager = ReferenceListManager('./test_source.txt')

    list1 = manager.lists[0]
    angels_reference = list1.references[0]
    self.assertEqual(list1.characters[u'angels'], models.Character(u'angels'))
    self.assertEqual(list1.characters[u'Ādam'], models.Character(u'Ādam'))
    self.assertEqual(list1.characters[u'Iblīs'], models.Character(u'Iblīs'))
    self.assertEqual(list1.characters[u'Ādam’s wife'],
      models.Character(u'Ādam’s wife'))
    self.assertEqual(angels_reference.chapter, 2)
    self.assertEqual(angels_reference.verses, range(30, 39))
    self.assertEqual(angels_reference.characters[0],
      models.Character(u'angels'))
    self.assertEqual(angels_reference.characters[1], models.Character(u'Ādam'))
    iblis_reference = list1.references[1]
    self.assertEqual(iblis_reference.chapter, 2)
    self.assertEqual(iblis_reference.verses, [34, 36])
    self.assertEqual(iblis_reference.characters[0], models.Character(u'Iblīs'))
    adam_wife_reference = list1.references[2]
    self.assertEqual(adam_wife_reference.chapter, 2)
    self.assertEqual(adam_wife_reference.verses, [35, 36, 38])
    self.assertEqual(adam_wife_reference.characters[0],
      models.Character(u'Ādam’s wife'))

    list2 = manager.lists[1]
    sole_reference = list2.references[0]
    self.assertEqual(list2.characters[u'Mūsā'], models.Character(u'Mūsā'))
    self.assertEqual(list2.characters[u'‘Īsā'], models.Character(u'‘Īsā'))
    self.assertEqual(list2.characters[u'Ādam'], models.Character(u'Ādam'))
    self.assertEqual(sole_reference.chapter, 2)
    self.assertEqual(sole_reference.verses, [87])
    self.assertEqual(sole_reference.characters[0], models.Character(u'Mūsā'))
    self.assertEqual(sole_reference.characters[1], models.Character(u'‘Īsā'))
    self.assertEqual(sole_reference.characters[2], models.Character(u'Ādam'))


if __name__ == '__main__':
  unittest.main()