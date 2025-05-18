from tog.src.abstracts.abs_file_handler import AbsFileHandler
from typing import Final

# --------------------------------
# Class FileHandler for Mutations.
# --------------------------------


class FileHandler(AbsFileHandler):

    # Columns.
    FULL_NAME: Final = 'full_name'
    EFFECT: Final = 'effect'

    def __init__(self):
        super().__init__('mutations.csv')

    ############################
    ########## PUBLIC ##########
    ############################

    def get_full_name(self, id):
        return self._find_value(id, self.FULL_NAME)

    def get_effect(self, id):
        return self._find_value(id, self.EFFECT)
