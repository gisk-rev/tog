from tog.src.abstracts.abs_file_handler import AbsFileHandler
from typing import Final

# ------------------------------------
# Class FileHandler for Nucleic Acids.
# ------------------------------------


class FileHandler(AbsFileHandler):

    # Columns.
    CHEMICAL_NAME: Final = 'chemical_name'
    STRUCTURE: Final = 'structure'
    NUCLEOTIDE_BASES: Final = 'nucleotide_bases'

    def __init__(self):
        super().__init__('nucleic_acids.csv')

    ############################
    ########## PUBLIC ##########
    ############################

    def get_chemical_name(self, id):
        return self._find_value(id, self.CHEMICAL_NAME)

    def get_structure(self, id):
        return self._find_value(id, self.STRUCTURE)

    def get_nucleotide_bases(self, id):
        return self._find_value(id, self.NUCLEOTIDE_BASES)
