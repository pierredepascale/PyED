#
# PyED -- an emacs like text editor in Python
#
# Copyright 2011 Pierre De Pascale (pierre.depascale _AT_ gmail.com)
#

from buffer import *
from window import *
from command import *

import mode

import curses

KEY_TRANSLATION = {
  curses.KEY_DOWN: "down",
  curses.KEY_UP: "up",
  curses.KEY_LEFT: "left",
  curses.KEY_RIGHT: "right",
  curses.KEY_HOME: "home",
  curses.KEY_END: "end",
  curses.KEY_BACKSPACE: "backspace",
  curses.KEY_DC: "delete",
  curses.KEY_IC: "insert",
  curses.KEY_NPAGE: "pagedown",
  curses.KEY_PPAGE: "pageup",
  10: "return" }

class Editor:
  """The class Editor implements the top level part of the editor"""
  def __init__(self):
    buffer = Buffer("#\n# Welcome to PyED\n#\n\n")
    self._window = Window(buffer)
    self._last_key = None
    self._message = None
    self._width = 0
    self._height = 0
    self._window.set_point(buffer.end())

  def window(self): return self._window

  def last_key(self):
    """Return the last key pressed"""
    return self._last_key

  def run(self):
    """Run the editor main loop (read and execute command)"""
    try:
      screen = curses.initscr()
      curses.noecho()
      curses.raw()
      curses.meta(1)
      screen.keypad(1)
      height, width = screen.getmaxyx()
      self._width = width
      self._height = height
      self._window.set_size(width, height-1)
      self.redisplay(screen)
      while 1:
        cmd = self.read_command(screen)
        if cmd is None:
          curses.beep()
          self.message("No command on key '%s'" % self.last_key())
        else:
          self.message(None)
          cmd.run()
        self.redisplay(screen)
    finally:
      screen.keypad(0)
      curses.meta(0)
      curses.noraw()
      curses.endwin()

  def redisplay(self, screen):
    """Redisplay the screen of the editor"""
    # first erase the screen
    screen.erase()
    # redisplay the main window
    self._window.redisplay(screen)
    # display the message if one exists
    if self._message is not None:
      screen.addstr(self._height-1, 0, self._message)
    # finally refresh the screen
    screen.refresh()

  def read_command(self, screen):
    """Read the next command from the keyboard"""
    key = self.read_key(screen)
    self._last_key = key
    return self._window.find_command(key)

  def read_key(self, screen):
    """Read the next key press"""
    while 1:
      key = screen.getch()
      if key == 10 or key==13:
        return "return"
      elif key == 9:
        return "tab"
      elif key < 26:
        return "^"+chr(64+key)
      elif key < 128:
        return chr(key)
      elif key < 255:
        return curses.keyname(key)
      else:
        return KEY_TRANSLATION[key]
    
  def message(self, text):
    """Show TEXT as a message on the last line of the screen"""
    self._message = text

EDITOR = None

def set_editor(editor):
  """Sets the toplevel editor instance"""
  global EDITOR
  EDITOR = editor

def run_editor():
  """Run the editor toplevel"""
  EDITOR.run()

def point():
  """Return the current point"""
  return EDITOR.window().point()

def set_point(mark):
  """Sets the current point to MARK"""
  EDITOR.window().set_point(mark)
  
def mark():
  """Returns the mark set or None if no mark has been defined"""
  return EDITOR.window().mark()

def insert_char(char):
  """Insert CHAR at the point position and advance point"""
  point().insert_char(char)

def last_key():
  """Return the last key pressed"""
  return EDITOR.last_key()

def window():
  """Return the current window"""
  return EDITOR.window()

def message(text):
  """Display TEXT as a message at the next refresh of the screen"""
  EDITOR.message(text)
