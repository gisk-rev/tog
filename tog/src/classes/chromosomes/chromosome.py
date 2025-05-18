from tog.src.classes.handlers_manager import HandlersManager as HM
from enum import Enum

# ------------
# Chromosomes.
# ------------


class Chromosome(Enum):

    _1 = '1'
    _2 = '2'
    _3 = '3'
    _4 = '4'
    _5 = '5'
    _6 = '6'
    _7 = '7'
    _8 = '8'
    _9 = '9'
    _10 = '10'
    _11 = '11'
    _12 = '12'
    _13 = '13'
    _14 = '14'
    _15 = '15'
    _16 = '16'
    _17 = '17'
    _18 = '18'
    _19 = '19'
    _20 = '20'
    _21 = '21'
    _22 = '22'
    _X = 'X'
    _Y = 'Y'

    @property
    def code(self):
        return self.value

    @property
    def group(self):
        return HM.chromosomes.get_group(self.value)

    @property
    def size(self):
        return HM.chromosomes.get_size(self.value)

    @property
    def centromere_position(self):
        return HM.chromosomes.get_centromere_position(self.value)

    @property
    def genes_number(self):
        return HM.chromosomes.get_genes_number(self.value)

    @property
    def bases_number(self):
        return HM.chromosomes.get_bases_number(self.value)

    @property
    def is_sex_chromosome(self):
        status = HM.chromosomes.get_is_sex_chromosome(self.value)
        return True if int(status) == 1 else False