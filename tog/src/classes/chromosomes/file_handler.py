from tog.src.abstracts.abs_file_handler import AbsFileHandler
from typing import Final

# ----------------------------------
# Class FileHandler for Chromosomes.
# ----------------------------------


class FileHandler(AbsFileHandler):

    # Columns.
    GROUP: Final = 'group'
    SIZE: Final = 'size'
    CENTROMERE_POSITION: Final = 'centromere_position'
    GENES_NUMBER: Final = 'genes_number'
    BASES_NUMBER: Final = 'bases_number'
    IS_SEX_CHROMOSOME: Final = 'is_sex_chromosome'

    def __init__(self):
        super().__init__('chromosomes.csv')

    ############################
    ########## PUBLIC ##########
    ############################

    def get_group(self, id):
        return self._find_value(id, self.GROUP)

    def get_size(self, id):
        return self._find_value(id, self.SIZE)

    def get_centromere_position(self, id):
        return self._find_value(id, self.CENTROMERE_POSITION)

    def get_genes_number(self, id):
        return self._find_value(id, self.GENES_NUMBER)

    def get_bases_number(self, id):
        return self._find_value(id, self.BASES_NUMBER)

    def get_is_sex_chromosome(self, id):
        return self._find_value(id, self.IS_SEX_CHROMOSOME)
