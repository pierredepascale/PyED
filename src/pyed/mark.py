#
# PyED -- an emacs like text editor in Python
#
# Copyright 2011 Pierre De Pascale (pierre.depascale _AT_ gmail.com)
#
class Mark:
  """A Mark represents text position inside a buffer. 

  According to the Emacs tradition, a mark sits always between characters"""
  def __init__(self, pos, buffer):
    self._pos = pos
    self._buffer = buffer

  def buffer(self):
    """Return the buffer on which the mark points"""
    return self._buffer 

  def position(self):
    """Return the absolute position of the mark in the buffer"""
    return self._pos
  
  def column(self):
    """Return the column number of the mark"""
    bol = self._buffer.rfind('\n', 0, self._pos)
    if bol == -1:
      return self._pos
    else:
      return self._pos - bol

  # INSERTION
  def insert_char(self, char):
    """Insert CHAR at the mark position in the buffer and move the mark accordingly"""
    self._buffer.insert(char, self._pos)
    self._pos += 1

  def insert_string(self, str):
    """Insert STR at the mark position in the buffer and move the mark accordingly"""
    self._buffer.insert(str, self._pos)
    self._pos += len(str)

  # DELETION
  def delete_left_char(self):
    """Delete the character on the left of the mark. If the mark is at the begining
    of the buffer, nothing happens"""
    if self._pos > 0:
      self._buffer.delete(self._pos-1, self._pos)

  def delete_right_char(self):
    """Delete the character on the rifht of the mark. If the mark is at the end of 
    the buffer, nothing happens"""
    if self._pos < len(self._buffer):
      self._buffer.delete(self._pos, self._pos+1)

  #
  # MOTION
  #
  def begining_of_line(self):
    """Return a mark positionned at the begining of the line"""
    if self.is_bol():
      return Mark(self._pos, self._buffer)
    else:
      pos = self._buffer.rfind('\n', 0, self._pos)
      if pos == -1:
        return Mark(0, self._buffer)
      else:
        return Mark(pos+1, self._buffer)

  def end_of_line(self):
    """Return a mark positioned at the end of the line"""
    pos = self._buffer.find('\n', self._pos)
    if pos == -1:
      return self._buffer.end()
    else:
      return Mark(pos, self._buffer)

  def looking_at(self, text):
    """Predicate indicating if the text after the mark matches the string TEXT"""
    return self._buffer[self._pos:self._pos + len(text)] == text

  def left_char(self):
    """Return the character on the left of the mark"""
    return self._buffer[self._pos - 1]

  def right_char(self):
    """Return the character on the right of the mark"""
    return self._buffer[self._pos]
 
  def line_offset(self, _offset):
    """Return a mark positioned after OFFSET line"""
    if _offset < 0:
      pos = self._buffer.rfind("\n", 0, self._pos)
      if pos == -1:
        return self._buffer.start()
      else:
        return Mark(pos+1, self._buffer)
    else:
      pos = self._buffer.find('\n', self._pos)
      if pos == -1:
        return self._buffer.end()
      else:
        return Mark(pos+1, self._buffer)

  def same_line(self, mark):
    """Predicate indicating if MARK and SELF are on the same line"""
    return self.begining_of_line() == mark.begining_of_line()

  def line_text(self):
    """Return the contents of the line where the mark sits"""
    end = self._buffer.find('\n', self._pos)
    if end == -1:
      return self._buffer[self._pos:len(self._buffer)]
    else:
      return self._buffer[self._pos:end]

  def offset(self, offset):
    """Return a mark pointing in the same buffer but OFFSET characters forwards"""
    return Mark(self._pos + offset, self._buffer)
  
  def __add__(self, offset):
    """Return a mark pointing in the same buffer but OFFSET characters forwards"""
    return Mark(self._pos + offset, self._buffer)

  def __sub__(self, mark):
    """Return the number of characters between the two marks"""
    return self._pos - mark.position()

  def __lt__(self, mark):
    """Predicate if the mark sits before MARK"""
    return self._pos < mark.position()
  
  def __le__(self, mark):
    """Predicate if the mark does not sit after MARK"""
    return self._pos <= mark.position()
  
  def __ne__(self, mark):
    """Predicate if the marks point to different location in the buffer"""
    return self._buffer != mark.buffer() or self._pos != mark.position()

  def __eq__(self, mark):
    """Predicate if the marks point to the same location in the buffer"""
    return self._buffer == mark.buffer() and self._pos == mark.position()

  def next_line(self):
    """Return a mark pointing at the begining of the next line"""
    return self.line_offset(1)

  def previous_line(self):
    """Return a mark pointing at the begining of the previous line"""
    return self.line_offset(-1)

  def is_begining_of_line(self):
    """Predicate indicatin if the mark sits at the begining of a line"""
    return self._pos == 0 or self.left_char() == '\n'

  def is_end_of_line(self):
    """Predicate indicating if the mark is at the end of the line"""
    return self._pos == self.buffer().length() or self.right_char() == '\n'

  def is_bob(self):
    """Predicate indicating if the mark is at the begining of the buffer"""
    return self._pos == 0

  def is_eob(self):
    """Predicate indicating if the mark is at the end of the buffer"""
    return self._pos == self.buffer().length()

  def is_bol(self):
    """Predicate indicating if the mark is at the begining of a line"""
    return self._pos == 0 or self.left_char() == '\n'
