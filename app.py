from data_manager import DataManager
from password import Password
from ui import UI


class App:
    def __init__(self):
        self._ui = UI(DataManager(), Password())

    # PUBLIC METHODS
    def start(self):
        self._ui.mainloop()
