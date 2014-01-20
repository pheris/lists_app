# coding=utf-8
import re
import utils

class Storeable(object):
  """Stores an object into a dataMap."""
  dataMap_ = {}

  def __init__(self, key, data):
    """Initializes a storeable object.

    Args:
        key: Object's key.
        data: Object's data.
    """
    self.__class__.dataMap_[key] = data

  @classmethod
  def get(self, key):
    return self.dataMap_[key]

  @classmethod
  def total(self):
    return len(self.dataMap_)

class Character(Storeable):
  """Stores a character's attributes."""

  def __init__(self, name):
    """Initializes a character.

      Args:
          name: A string containing the character's name.
    """
    self.name = name
    if (self.name in self.__class__.dataMap_.keys()):
      self.mentions_ = self.__class__.dataMap_[self.name].mentions_ + 1
      # self.mentionsInSharedLists_ = self.__class__.dataMap_[self.name].mentionsInSharedLists_
    else:
      self.mentions_ = 1
      # self.mentionsInSharedLists_ = {}
    super(Character, self).__init__(self.name, self)

  def getMentions(self):
    return self.__class__.dataMap_[self.name].mentions_

  # def addMentionInSharedListByCharacter(self, other):
  #   self.addMentionInSharedListByName(other.name)

  # def getNumberOfSharedListsByCharacter(self, other):
  #   return self.getNumberOfSharedListsByName(other.name)

  # def addMentionInSharedListByName(self, otherName):
  #   if self.name == otherName:
  #     return
  #   if self.getNumberOfSharedListsByName(otherName) == 0:
  #     self.mentionsInSharedLists_[otherName] = 1
  #   else:
  #     self.mentionsInSharedLists_[otherName] += 1

  # def getNumberOfSharedListsByName(self, otherName):
  #   if self.name == otherName:
  #     return 0
  #   if not(otherName in self.mentionsInSharedLists_.keys()):
  #     return 0
  #   return self.mentionsInSharedLists_[otherName]

  def __eq__(self, other):
    if isinstance(other, Character):
      return self.name == other.name
    return NotImplemented

class Reference(Storeable):
  """Stores a reference to a set of verses in a chapter."""

  def __init__(self, text, characters):
    """ Initializes a reference.

    Args:
        text: A string contianing verse numbers and ranges, like
            "1:2, 4, 5-7".
        characters: An array of Character objects mentioned in the verse ranges.
    """
    self.text = text
    self.characters = characters
    chapter_text, verses_text = re.split(':', self.text)
    self.chapter = int(chapter_text)
    self.verses = []
    for verse_ranges in re.split(r',\s', verses_text):
      if utils.is_number(verse_ranges):
        self.verses.append(int(verse_ranges))
      else:
        start_text, end_text = re.split('-', verse_ranges)
        start = int(start_text)
        end = int(end_text) + 1
        self.verses += range(start, end)
    super(Reference, self).__init__(self.text, self)

  def __eq__(self, other):
    if isinstance(other, Reference):
      return (self.chapter == other.chapter and
              self.verses == other.verses)
    return NotImplemented

class ReferenceList(Storeable):
  """Stores a reference list."""

  def __init__(self, text):
    """ Initializes a reference list.

    Args:
        text: A string containing a reference list.
    """
    self.text = text
    reference_texts = re.split(r';\s', self.text)
    self.references = []
    self.characters = {}
    regex = re.compile(r'(\d)\s(\w)', re.UNICODE)
    for complete_reference_text in reference_texts:
      groups = regex.split(complete_reference_text)
      reference_text = groups[0] + groups[1]
      characters_text = groups[2] + groups[3]
      names = re.split(',\s', characters_text)
      group_characters = []
      for name in names:
        new_character = Character(name)
        group_characters.append(new_character)
        self.characters[name] = new_character
      self.references.append(Reference(reference_text,
        group_characters))
    super(ReferenceList, self).__init__(self.text, self)

  def __eq__(self, other):
    if isinstance(other, Reference):
      return (self.references == other.references and
              self.characters == other.characters)
    return NotImplemented
