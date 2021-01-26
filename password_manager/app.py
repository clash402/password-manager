from password_manager.data.data_manager import DataManager
from password_manager.password import Password
from password_manager.ui import UI


class App:
    def __init__(self):
        self._ui = UI(DataManager(), Password())

    # PUBLIC METHODS
    def start(self):
        self._ui.mainloop()
