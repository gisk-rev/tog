from tog.src.classes.handlers_manager import HandlersManager as HM
from enum import Enum

# -----------------
# Nucleotide bases.
# -----------------


class NucleotideBase(Enum):

    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'
    URACIL = 'U'

    @property
    def code(self):
        return self.value

    @property
    def full_name(self):
        return HM.nucleotide_bases.get_full_name(self.value)

    @property
    def chemical_name(self):
        return HM.nucleotide_bases.get_chemical_name(self.value)

    @property
    def formula(self):
        return HM.nucleotide_bases.get_formula(self.value)

    @property
    def molar_mass(self):
        return HM.nucleotide_bases.get_molar_mass(self.value)

    @property
    def smiles(self):
        return HM.nucleotide_bases.get_smiles(self.value)
