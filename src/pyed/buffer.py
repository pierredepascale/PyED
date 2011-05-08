#
# PyED -- an emacs like text editor in Python
#
# Copyright 2011 Pierre De Pascale (pierre.depascale _AT_ gmail.com)
#

from mark import Mark

class Buffer:
  """A Buffer represents the contents of a text file like a string"""
  def __init__(self, text=""):
    self.text = text
    self._filename = None

  def filename(self):
    """Return the filename associated with the buffer"""
    return self._filename

  def set_filename(self, filename):
    """Sets the filename of the buffer to FILENAME"""
    self._filename = filename

  def start(self):
    """Return a mark pointing at the begining of the buffer"""
    return Mark(0, self)

  def end(self):
    """Return a mark pointing at the end of the buffer"""
    return Mark(len(self.text), self)

  def __getitem__(self, index):
    """Return the character at the INDEX position"""
    return self.text[index]

  def length(self):
    """Return the length (number of characters including newlines) of the buffer"""
    return len(self.text)

  def __len__(self):
    """Return the length of the buffer"""
    return len(self.text)

  def insert(self, str, index):
    """Insert STR at INDEX in the buffer"""
    self.text = self.text[0:index] + str + self.text[index:len(self.text)]

  def delete(self, start, end):
    """Delete the text from START and END"""
    self.text = self.text[0:start] + self.text[end:len(self)]

  def clear(self):
    """Clear the text of the buffer, i.e empty the contents of the buffer"""
    self.text = ""

  def as_string(self):
    """Returns the contents of the buffer as a string"""
    return self.text

  def find(self, char, start):
    """Find in the buffer a CHAR starting at position START.
    If no CHAR has been found, -1 is returned"""
    return self.text.find(char, start)
    
  def rfind(self, char, start, end):
    """Find in the buffer the last occurence of CHAR in the range START and END"""
    return self.text.rfind(char, start, end)
