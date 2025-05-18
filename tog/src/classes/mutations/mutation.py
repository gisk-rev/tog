from tog.src.classes.handlers_manager import HandlersManager as HM
from enum import Enum

# ----------
# Mutations.
# ----------


class Mutation(Enum):

    CHROMOSOMAL_DELETION = 'cdel'
    CHROMOSOMAL_DUPLICATION = 'cdup'
    CHROMOSOMAL_INSERTION = 'cins'
    CHROMOSOMAL_INVERSION = 'cinv'
    CHROMOSOMAL_TRANSLOCATION = 'ctra'

    NUCLEOTIDES_DELETION = 'ndel'
    NUCLEOTIDES_INSERTION = 'nins'

    SUBSTITUTION_MISSENSE = 'smis'
    SUBSTITUTION_NONSENSE = 'snon'
    SUBSTITUTION_SILENT = 'ssil'
    
    @property
    def code(self):
        return self.value

    @property
    def full_name(self):
        return HM.mutations.get_full_name(self.value)

    @property
    def effect(self):
        return HM.mutations.get_effect(self.value)
