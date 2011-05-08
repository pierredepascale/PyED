# PyED -- an emacs like text editor in Python
#
# (c) 2011 Pierre De Pascale (pierre.depascale _AT_ gmail.com)
#

from keymap import *
from mode import *

import curses

class Window:
  """A Window displays a specific buffer"""
  def __init__(self, buffer, width=5, height=5):
    self._buffer = buffer
    self._start = buffer.start()
    self._point = buffer.start()
    self._mode = default_mode()
    self._mark = None
    self._width = width
    self._height = height

  def set_size(self, width, height):
    """Set the size WIDTH and HEIGHT of the window on screen"""
    self._width = width
    self._height = height

  def redisplay(self, screen):
    """Redisplay the window on SCREEN"""
    l = self._start
    for i in range(0,self._height-1):
      text = l.line_text()
      text = text[0:self._width]
      screen.addstr(i, 0, text)
      l = l.next_line()

    screen.attron(curses.A_REVERSE)
    title = " * PYED (%s) : %s" % (self._mode.name(), self._buffer.filename())
    title = title.ljust(self._width)
    screen.addstr(self._height-1, 0, title)
    screen.attroff(curses.A_REVERSE)

    x,y = self.screen_position(self._point)
    if x is None:
      curses.curs_set(0)
    else:
      curses.curs_set(1)
      screen.move(y,x)
    
  def select_buffer(self, buffer):
    """Make the window display BUFFER"""
    self._buffer = buffer
    self._start = buffer.start()
    self._point = buffer.start()
    self._mark = None

  def point(self):
    """Return the current point of the window"""
    return self._point

  def set_point(self, mark):
    """Sets the current point of the window to MARK"""
    self._point = mark
    
  def mark(self):
    """Return the mark of the window or None if no mark has been defined"""
    return self._mark
  
  def find_command(self, key):
    """Return the command bound on KEY in the mode active in the window.
    If no command are bound, None is returned"""
    mode = self._mode
    if mode is not None:
      return mode.find_command(key)
    else:
      return None

  def set_mode(self, mode):
    """Sets the mode to use for the window"""
    self._mode = mode

  def mode(self):
    """Return the mode currently active for the window"""
    return self._mode

  def screen_position(self, mark):
    """Return the (x,y) coordinate of MARK in the window.
    If the mark is not visible (None, None) is returned"""
    x,y = 0,0
    mark_bol = mark.begining_of_line()
    current = self._start
    while y < self._height-1 and not (current == mark_bol):
      current = current.next_line()
      y += 1

    if current == mark_bol:
      x = mark-current
      if x < self._width:
        return (mark-current), y
      else:
        return None, y
    else:
      return None, None
