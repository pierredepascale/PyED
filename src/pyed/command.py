#
# PyED -- an emacs like text editor in Python
#
# Copyright 2011 Pierre De Pascale (pierre.depascale _AT_ gmail.com)
#

class Command:
  """Command represents a user command bound to keys"""
  def __init__(self, name, description, code):
    self.name = name
    self.code = code
    self.description = description

  def run(self):
    """Run the command"""
    self.code()

# This is the list of all commands
COMMANDS = []


def interactive(f):
  """Decorator to annotate a function to make it a command that
  can be bound to keys or called interactively"""
  global COMMANDS
  COMMANDS += [Command(f.__module__+"."+f.__name__, f.__doc__, f)]
  return f

def find_command(name):
  """Find the command named NAME. If the command is not found, None is returned"""
  for c in COMMANDS:
    if c.name == name:
      return c
  return None
