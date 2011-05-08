#
# PyED -- an emacs like text editor in Python
#
# Copyright 2011 Pierre De Pascale (pierre.depascale _AT_ gmail.com)
#

from keymap import *
from mode import *
from command import *

from editor import *

FUNDAMENTAL_MAP = Keymap()
FUNDAMENTAL_MODE = Mode("Fundamental", "Fundamental mode", FUNDAMENTAL_MAP)

@interactive
def self_insert():
  """Insert the last key pressed at the current point position"""
  insert_char(last_key())

@interactive
def next_line():
  """Move the point to the next line"""
  set_point(point().next_line())

@interactive
def previous_line():
  """Move the point to the previous line"""
  set_point(point().previous_line())

@interactive
def forward_character():
  """Move the point to the next character"""
  set_point(point()+1)

@interactive
def backward_character():
  """Move the point to the previous character"""
  set_point(point().offset(-1))

@interactive
def insert_newline():
  """Insert a line break at the current point position"""
  insert_char("\n")

@interactive
def end_of_line():
  """Move the current point to the end of line"""
  set_point(point().end_of_line())

@interactive
def begining_of_line():
  """Move the current point to the begining of the line"""
  set_point(point().begining_of_line())

@interactive
def delete_forward():
  """Delete the next character"""
  point().delete_right_char()

@interactive
def delete_backward():
  """Delete the previous character"""
  point().delete_left_char()
  set_point(point().offset(-1))

@interactive
def quit_editor():
  """quit the editor"""
  raise "END"

FUNDAMENTAL_MAP.bind("down", "pyed.fundamental.next_line")
FUNDAMENTAL_MAP.bind("up", "pyed.fundamental.previous_line")
FUNDAMENTAL_MAP.bind("left", "pyed.fundamental.backward_character")
FUNDAMENTAL_MAP.bind("right", "pyed.fundamental.forward_character")

FUNDAMENTAL_MAP.bind("return", "pyed.fundamental.insert_newline")
FUNDAMENTAL_MAP.bind("^C", "pyed.fundamental.quit_editor")

FUNDAMENTAL_MAP.bind("delete", "pyed.fundamental.delete_forward")
FUNDAMENTAL_MAP.bind("backspace", "pyed.fundamental.delete_backward")

FUNDAMENTAL_MAP.bind("end", "pyed.fundamental.end_of_line")
FUNDAMENTAL_MAP.bind("home", "pyed.fundamental.begining_of_line")

for ch in range(ord(' '), ord('z')):
  FUNDAMENTAL_MAP.bind(chr(ch), "pyed.fundamental.self_insert")

