#
# PyED -- an emacs like text editor in Python
#
# Copyright 2011 Pierre De Pascale (pierre.depascale _AT_ gmail.com)
#

class Mode:
  """A Mode define how to interpret and edit a buffer"""

  def __init__(self, name, description, keymap=None):
    self._name = name
    self._description = description
    if keymap is None:
      self._keymap = Keymap()
    else:
      self._keymap = keymap

  def name(self): return self._name
  def description(self): return self._description
  def keymap(self): return self._keymap
  
  def find_command(self, key):    
    return self._keymap.find_command(key)

# The default mode for a buffer
DEFAULT_MODE = None


def set_default_mode(mode):
  """Set the default mode to use for buffers"""
  global DEFAULT_MODE
  DEFAULT_MODE = mode

def default_mode():
  """Return the default for buffers"""
  return DEFAULT_MODE
