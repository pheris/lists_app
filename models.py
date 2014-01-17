# coding=utf-8
import re
import utils

class Storeable(object):
  """Stores an object into a dataMap.

    Args:
        key: Object's key.
        data: Object's data.
  """
  dataMap_ = {}

  def __init__(self, key, data):
    self.__class__.dataMap_[key] = data

  @classmethod
  def get(self, key):
    return self.dataMap_[key]

  @classmethod
  def total(self):
    return len(self.dataMap_)

class Character(Storeable):
  """Stores a character's attributes.

    Args:
        name: A string containing the character's name.
  """

  def __init__(self, name):
    self.name = name
    super(Character, self).__init__(self.name, self)

  def __eq__(self, other):
    if isinstance(other, Character):
      return self.name == other.name
    return NotImplemented

class Reference(Storeable):
  """Stores a reference to a set of verses in a chapter."""

  def __init__(self, reference_text):
    """ Initializes a reference.

    Args:
        reference_text: A string contianing verse numbers and ranges, like
            "1:2, 4, 5-7".
    """
    self.reference_text = reference_text
    chapter_text, verses_text = re.split(":", self.reference_text)
    self.chapter = int(chapter_text)
    self.verses = []
    for verse_ranges in re.split(", ", verses_text):
      if utils.is_number(verse_ranges):
        self.verses.append(int(verse_ranges))
      else:
        start_text, end_text = re.split("-", verse_ranges)
        start = int(start_text)
        end = int(end_text) + 1
        self.verses += range(start, end)
    super(Reference, self).__init__(self.reference_text, self)

  def __eq__(self, other):
    if isinstance(other, Reference):
      return (self.chapter == other.chapter and
              self.verses == other.verses)
    return NotImplemented