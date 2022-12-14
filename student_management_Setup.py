import sys
from sys import executable
from cx_Freeze import *
includefiles = ["student_icon.ico"]
excludes = []
packages = []
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table = {
    (
        "DesktopShortcut", # shortcut
        "DesktopFolder", # Directory_
        "first_program", # Name
        "TARGETDIR", #Component_
        "[TARGETDIR]\first_program.exe", #Target
        None, # Arguments
        None, # Description
        None, # Hotkey
        None, # Icon
        None, # IconIndex
        None, # ShowCmd
        "TARGETDIR", # WkDir
    )
}

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version = "0.1",
    description = " Student Management System",
    author = "Supriya",
    name = "Student Management System",
    options = {'build_exe':{'include_files':includefiles}, "bdist_msi": bdist_msi_options},
    executables=[
        Executable(
            script="first_program.py",
            base=base,
            icon="student_icon.ico"
        )]
)