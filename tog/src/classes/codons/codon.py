from tog.src.classes.handlers_manager import HandlersManager as HM
from tog.src.base.converter import Converter
from enum import Enum

# -------
# Codons.
# -------


class Codon(Enum):

    AAA = 'AAA'
    AAC = 'AAC'
    AAG = 'AAG'
    AAU = 'AAU'
    ACA = 'ACA'
    ACC = 'ACC'
    ACG = 'ACG'
    ACU = 'ACU'
    AGA = 'AGA'
    AGC = 'AGC'
    AGG = 'AGG'
    AGU = 'AGU'
    AUA = 'AUA'
    AUC = 'AUC'
    AUG = 'AUG'
    AUU = 'AUU'

    CAA = 'CAA'
    CAC = 'CAC'
    CAG = 'CAG'
    CAU = 'CAU'
    CCA = 'CCA'
    CCC = 'CCC'
    CCG = 'CCG'
    CCU = 'CCU'
    CGA = 'CGA'
    CGC = 'CGC'
    CGG = 'CGG'
    CGU = 'CGU'
    CUA = 'CUA'
    CUC = 'CUC'
    CUG = 'CUG'
    CUU = 'CUU'

    GAA = 'GAA'
    GAC = 'GAC'
    GAG = 'GAG'
    GAU = 'GAU'
    GCA = 'GCA'
    GCC = 'GCC'
    GCG = 'GCG'
    GCU = 'GCU'
    GGA = 'GGA'
    GGC = 'GGC'
    GGG = 'GGG'
    GGU = 'GGU'
    GUA = 'GUA'
    GUC = 'GUC'
    GUG = 'GUG'
    GUU = 'GUU'

    TAA = 'TAA'
    TAC = 'TAC'
    TAG = 'TAG'
    TAT = 'TAT'
    TCA = 'TCA'
    TCC = 'TCC'
    TCG = 'TCG'
    TCT = 'TCT'
    TGA = 'TGA'
    TGC = 'TGC'
    TGG = 'TGG'
    TGT = 'TGT'
    TTA = 'TTA'
    TTC = 'TTC'
    TTG = 'TTG'
    TTT = 'TTT'

    UAA = 'UAA'
    UAC = 'UAC'
    UAG = 'UAG'
    UAU = 'UAU'
    UCA = 'UCA'
    UCC = 'UCC'
    UCG = 'UCG'
    UCU = 'UCU'
    UGA = 'UGA'
    UGC = 'UGC'
    UGG = 'UGG'
    UGU = 'UGU'
    UUA = 'UUA'
    UUC = 'UUC'
    UUG = 'UUG'
    UUU = 'UUU'

    @property
    def code(self):
        return self.value

    @property
    def amino_acid(self):
        code = HM.codons.get_amino_acid(self.value)
        return Converter.get_enum_amino_acid(code)

    @property
    def is_stop_codon(self):
        status = HM.codons.get_is_stop_codon(self.value)
        return True if int(status) == 1 else False

    @property
    def nucleotide_bases(self):
        return Converter.get_enum_nucleotide_bases(self.value)

    @staticmethod
    def get_stop_codons():
        """
        Get a list with only the stop codons.

        Returns
        -------
        stop_codons : Codon[]
            A list of stop codons.
        """
        return [Codon.TAA, Codon.TAG, Codon.TGA,
                Codon.UAA, Codon.UAG, Codon.UGA]
