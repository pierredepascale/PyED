#
# PyED -- an emacs like text editor in Python
#
# Copyright 2011 Pierre De Pascale (pierre.depascale _AT_ gmail.com)
#

import command

class Keymap:
  """A Keymap maps keys to command name"""
  def __init__(self):
    self.bindings = []

  def bind(self, key, command):
    """Binds KEY to COMMAND in keymap"""
    self.bindings += [(key, command)]

  def unbind(self, key):
    """Unbinds KEY in keymap"""
    self.bindings -= key

  def find_command(self, key):
    """Returns the command object bound to KEY or None if the key is unbound"""
    for b in self.bindings:
      if b[0] == key:
        return command.find_command(b[1])
    return None
