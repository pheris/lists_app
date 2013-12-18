# coding=utf-8
import re

class Character:
  """Stores a character's attributes.

    Args:
        name: A string containing the character's name.
  """
  def __init__(self, name):
    self.name = name

class Reference:
  """Stores a reference to a set of verses in a chapter."""

  def __init__(self, reference_text):
    """ Initializes a reference.

    Args:
        reference_text: A string contianing verse numbers and ranges, like
            "1:2, 4, 5-7".
    """
    chapter_text, verses = re.split(":", reference_text)
    self.chapter = int(chapter_text)
    self.verses = []
    for verse_ranges in re.split(", ", verses):
      if len(verse_ranges) > 1:
        for verse_range in re.split("-", verse_ranges):
          if len(verse_range) == 1:
            self.verses.append(int(verse_range[0]))
          elif len(verse_range) == 2:
            start = int(verse_range[0])
            end = int(verse_range[1]) + 1
            self.verses += range(start, end)
      elif len(verse_ranges) == 1:
        self.verses.append(int(verse_ranges[0]))