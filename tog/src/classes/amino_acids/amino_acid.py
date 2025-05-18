from tog.src.classes.handlers_manager import HandlersManager as HM
from tog.src.base.converter import Converter
from enum import Enum

# ------------
# Amino acids.
# ------------


class AminoAcid(Enum):

    ALANINE = 'A'
    CYSTEINE = 'C'
    ASPARTIC_ACID = 'D'
    GLUTAMIC_ACID = 'E'
    PHENYLALANINE = 'F'
    GLYCINE = 'G'
    HISTIDINE = 'H'
    ISOLEUCINE = 'I'
    LYSINE = 'K'
    LEUCINE = 'L'
    METHIONINE = 'M'
    ASPARAGINE = 'N'
    PYRROLYSINE = 'O'
    PROLINE = 'P'
    GLUTAMINE = 'Q'
    ARGININE = 'R'
    SERINE = 'S'
    THREONINE = 'T'
    SELENOCYSTEINE = 'U'
    VALINE = 'V'
    TRYPTOPHAN = 'W'
    TYROSINE = 'Y'

    @property
    def code(self):
        return self.value

    @property
    def full_name(self):
        return HM.amino_acids.get_full_name(self.value)

    @property
    def chemical_name(self):
        return HM.amino_acids.get_chemical_name(self.value)

    @property
    def formula(self):
        return HM.amino_acids.get_formula(self.value)

    @property
    def molar_mass(self):
        return HM.amino_acids.get_molar_mass(self.value)

    @property
    def isoelectric_point(self):
        return HM.amino_acids.get_isoelectric_point(self.value)

    @property
    def smiles(self):
        return HM.amino_acids.get_smiles(self.value)

    @property
    def codons(self):
        codons = HM.amino_acids.get_codons(self.value)
        codons_codes_list =  codons.split('-')
        return Converter.get_enum_codons(codons_codes_list)
