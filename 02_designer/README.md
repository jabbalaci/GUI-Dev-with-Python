Using Qt Designer
=================

The GUI part of this example was created with Qt Designer.

Manjaro
-------

Under Manjaro, I had to install the package `qt5-tools`,
which made the command `designer` available.

Windows
-------

To install Qt Designer, issue the following command in your terminal:

    pip install pyqt5-tools

It will install PyQt5 globally on your system.

On my machine, Python was installed to the folder
`C:\Python37`, thus `designer.exe` was put here:

    c:\Python37\Scripts\designer.exe

Usage
-----

Open `show.ui` in Designer, edit it, then save it.

Run `compile.sh` (on Windows: `compile.bat`) to convert
`show.ui` to a Python source code. Content of this script:

    pyuic5 show.ui -o showGui.py

Finally, run `main.py`.
