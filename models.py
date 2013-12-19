# coding=utf-8
import re
import utils

class Character:
  """Stores a character's attributes.

    Args:
        name: A string containing the character's name.
  """
  def __init__(self, name):
    self.name = name

  def __eq__(self, other):
    if isinstance(other, Character):
      return self.name == other.name
    return NotImplemented

class Reference:
  """Stores a reference to a set of verses in a chapter."""

  def __init__(self, reference_text):
    """ Initializes a reference.

    Args:
        reference_text: A string contianing verse numbers and ranges, like
            "1:2, 4, 5-7".
    """
    chapter_text, verses_text = re.split(":", reference_text)
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