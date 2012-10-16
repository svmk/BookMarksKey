import sublime, sublime_plugin, os
SETTINGS_NAME = 'BookMarksKey.sublime-settings'
def set_cursor_position(selected,position):
  selected.clear()
  selected.add(sublime.Region(position))
def load_bookmark(bookmark_num):
  settings  = sublime.load_settings(SETTINGS_NAME)
  position  = int(settings.get('bookmark_' + str(bookmark_num),0))
  file_name = settings.get('bookmark_file_name' + str(bookmark_num),'')
  if position >= 0 and file_name:
    active_window = sublime.active_window()
    active_view = active_window.active_view()
    if active_view.file_name() == file_name:
      set_cursor_position(active_view.sel(),position)
      active_window.focus_view(active_view)
    else:
      is_found = False
      for window in sublime.windows():
        for view in window.views():
          if view.file_name() == file_name:
            selected = view.sel()
            set_cursor_position(selected,position)
            active_window.focus_view(view)
            is_found = True
            break
      if not is_found and os.path.exists(file_name):
        active_window = sublime.active_window()
        active_view   = active_window.open_file(file_name)
        set_cursor_position(active_view.sel(),position)
        active_window.focus_view(active_view)

def save_bookmark(bookmark_num):
  view = sublime.active_window().active_view()
  selected = view.sel()
  settings = sublime.load_settings(SETTINGS_NAME)
  position = int(settings.get('bookmark_' + str(bookmark_num),0))
  if position >= 0:
    position = -1
  else:
    position = selected[0].a
  settings.set('bookmark_' + str(bookmark_num),position)
  settings.set('bookmark_file_name' + str(bookmark_num),view.file_name())
  sublime.save_settings(SETTINGS_NAME)

class BookMarksKeySetZeroCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(0)
    print 'it works!'
class BookMarksKeyShowZeroCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(0)

class BookMarksKeySetOneCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(1)
class BookMarksKeyShowOneCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(1)

class BookMarksKeySetTwoCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(2)
class BookMarksKeyShowTwoCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(2)

class BookMarksKeySetThreeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(3)
class BookMarksKeyShowThreeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(3)

class BookMarksKeySetFourCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(4)
class BookMarksKeyShowFourCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(4)

class BookMarksKeySetFiveCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(5)
class BookMarksKeyShowFiveCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(5)

class BookMarksKeySetSixCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(6)
class BookMarksKeyShowSixCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(6)

class BookMarksKeySetSevenCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(7)
class BookMarksKeyShowSevenCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(7)

class BookMarksKeySetEightCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(8)
class BookMarksKeyShowEightCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(8)

class BookMarksKeySetNineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    save_bookmark(9)
class BookMarksKeyShowNineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    load_bookmark(9)
