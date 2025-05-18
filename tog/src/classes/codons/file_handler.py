from tog.src.abstracts.abs_file_handler import AbsFileHandler
from typing import Final

# -----------------------------
# Class FileHandler for Codons.
# -----------------------------


class FileHandler(AbsFileHandler):

    # Columns.
    AMINO_ACID: Final = 'amino_acid'
    IS_STOP_CODON: Final = 'is_stop_codon'

    def __init__(self):
        super().__init__('codons.csv')

    ############################
    ########## PUBLIC ##########
    ############################

    def get_amino_acid(self, id):
        return self._find_value(id, self.AMINO_ACID)

    def get_is_stop_codon(self, id):
        return self._find_value(id, self.IS_STOP_CODON)
