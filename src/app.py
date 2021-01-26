from src.data_manager import DataManager
from src.password import Password
from src.ui import UI


class App:
    def __init__(self):
        self._ui = UI(DataManager(), Password())

    # PUBLIC METHODS
    def start(self):
        self._ui.mainloop()
