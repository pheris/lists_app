# coding=utf-8
import re
import models
import codecs

class ReferenceListManager:

  def __init__(self, filePath):
    """Builds an array of reference lists from a valid file path.

    Args:
        filePath: Valid reference lists file path.
    """
    self.lists = []
    with codecs.open(filePath, encoding='utf-8') as f:
      for line in f:
        self.lists.append(models.ReferenceList(line.rstrip('\n')))
