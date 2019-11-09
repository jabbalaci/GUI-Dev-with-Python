#!/usr/bin/env python3

import sys

from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QShortcut


class Shortcuts:
    def __init__(self):
        self.window_shortcuts = {}
        self.menubar_actions = {}

    def enable_all_window_shortcuts(self):
        for shortcut in self.window_shortcuts.values():
            shortcut.setEnabled(True)

    def disable_conflicting_window_shortcuts(self):
        for key in self.menubar_actions:
            if key in self.window_shortcuts:
                self.window_shortcuts[key].setEnabled(False)

    def _normalize(self, key):
        return key.upper().replace(" ", "")

    def register_window_shortcut(self, key, q_shortcut, connect_function):
        key = self._normalize(key)
        self.window_shortcuts[key] = q_shortcut
        q_shortcut.activated.connect(connect_function)

    def register_menubar_action(self, key, q_action, connect_function):
        key = self._normalize(key)
        self.menubar_actions[key] = q_action
        q_action.setShortcut(key)
        q_action.triggered.connect(connect_function)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.shortcuts = Shortcuts()

        key = "Ctrl+Q"
        self.shortcutQuit = QShortcut(QKeySequence(key), self)
        self.shortcuts.register_window_shortcut(key, self.shortcutQuit, self.close)

        self.InitWindow()
        self.shortcuts.disable_conflicting_window_shortcuts()

    def InitWindow(self):
        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu("&File")

        key = "Ctrl+H"
        hideItem = QAction("Hide Menu Bar", self)
        self.shortcuts.register_menubar_action(key, hideItem, self.my_hide)

        key = "Ctrl+Q"
        quitItem = QAction("Quit", self)
        self.shortcuts.register_menubar_action(key, quitItem, self.close)

        fileMenu.addAction(hideItem)
        fileMenu.addAction(quitItem)

    def my_hide(self):
        self.mainMenu.hide()
        self.shortcuts.enable_all_window_shortcuts()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())