import cx_Freeze
import pynput
import pyperclip
import queue

executables = [cx_Freeze.Executable("copyPast.py", base="Win32GUI"),
               cx_Freeze.Executable("copyPastEditor.py", base="Win32GUI")]

cx_Freeze.setup(
    name="Copy Past",
    options={'build_exe': {"packages": ["pynput", "pyperclip", "queue"],
                           "include_files": ["copies.xml"]}},
    version="0.01",
    executables=executables
)
