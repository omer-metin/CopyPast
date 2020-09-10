from xml.etree import ElementTree

import pyperclip
from pynput import keyboard

COPIESXML = r".\copies.xml"


class CopyPast(object):

    def __init__(self):

        self.fn_pressed = False
        self._contr = keyboard.Controller()

    def on_press_key(self, key: keyboard.KeyCode):
        if str(key) == '<255>':
            self.fn_pressed = True
        elif self.fn_pressed:
            keyCodeStr = str(key).strip("'")
            if keyCodeStr.isnumeric():
                keyNum = int(keyCodeStr)
                if keyNum:
                    self._contr.press(keyboard.Key.backspace)
                    copy = self.get_copy_from_xml(keyNum-1)
                    if copy is None:
                        copy = ""
                    else:
                        self.copy2clip(copy)
                else:
                    self._contr.press(keyboard.Key.backspace)

    def on_release_key(self, key):
        if str(key) == '<255>':
            self.fn_pressed = False

    def copy2clip(self, txt):
        pyperclip.copy(txt)

    def get_copy_from_xml(self, ith):
        root = ElementTree.parse(COPIESXML).getroot()
        return root.getchildren()[ith].text


model = CopyPast()

with keyboard.Listener(on_press=model.on_press_key,
                       on_release=model.on_release_key) as l:
    l.join()
