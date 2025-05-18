from tog.src.classes.handlers_manager import HandlersManager as HM
from tog.src.base.converter import Converter
from enum import Enum

# --------------
# Nucleic acids.
# --------------


class NucleicAcid(Enum):

    DNA = 'DNA'
    RNA = 'RNA'

    @property
    def code(self):
        return self.value

    @property
    def chemical_name(self):
        return HM.nucleic_acids.get_chemical_name(self.value)

    @property
    def structure(self):
        return HM.nucleic_acids.get_structure(self.value)

    @property
    def nucleotide_bases(self):
        nucleotide_bases = HM.nucleic_acids.get_nucleotide_bases(self.value)
        return Converter.get_enum_nucleotide_bases(nucleotide_bases)
