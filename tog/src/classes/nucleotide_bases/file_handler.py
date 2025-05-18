from tog.src.abstracts.abs_file_handler import AbsFileHandler
from typing import Final

# ---------------------------------------
# Class FileHandler for Nucleotide Bases.
# ---------------------------------------


class FileHandler(AbsFileHandler):

    # Columns.
    FULL_NAME: Final = 'full_name'
    CHEMICAL_NAME: Final = 'chemical_name'
    FORMULA: Final = 'formula'
    MOLAR_MASS: Final = 'molar_mass'
    SMILES: Final = 'smiles'

    def __init__(self):
        super().__init__('nucleotide_bases.csv')

    ############################
    ########## PUBLIC ##########
    ############################

    def get_full_name(self, id):
        return self._find_value(id, self.FULL_NAME)

    def get_chemical_name(self, id):
        return self._find_value(id, self.CHEMICAL_NAME)

    def get_formula(self, id):
        return self._find_value(id, self.FORMULA)

    def get_molar_mass(self, id):
        return self._find_value(id, self.MOLAR_MASS)

    def get_smiles(self, id):
        return self._find_value(id, self.SMILES)
