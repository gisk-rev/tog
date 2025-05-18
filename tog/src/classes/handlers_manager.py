from tog.src.classes.amino_acids.file_handler import FileHandler as AminoAcidsHandler
from tog.src.classes.chromosomes.file_handler import FileHandler as ChromosomesHandler
from tog.src.classes.codons.file_handler import FileHandler as CodonsHandler
from tog.src.classes.mutations.file_handler import FileHandler as MutationsHandler
from tog.src.classes.nucleic_acids.file_handler import FileHandler as NucleicAcidsHandler
from tog.src.classes.nucleotide_bases.file_handler import FileHandler as NucleotideBasesHandler
from typing import Final

# ----------------------
# Class HandlersManager.
#
# Singleton pattern.
# ----------------------


class HandlersManager(object):

    _instance = None

    # Handlers.
    amino_acids = None
    chromosomes = None
    codons = None
    mutations = None
    nucleic_acids = None
    nucleotide_bases = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HandlersManager, cls).__new__(cls)
            cls.__set_handlers()
        return cls._instance

    #############################
    ########## PRIVATE ##########
    #############################

    @classmethod
    def __set_handlers(cls):
        """
        Set the files handlers.
        """
        cls.amino_acids: Final = AminoAcidsHandler()
        cls.chromosomes: Final = ChromosomesHandler()
        cls.codons: Final = CodonsHandler()
        cls.mutations: Final = MutationsHandler()
        cls.nucleic_acids: Final = NucleicAcidsHandler()
        cls.nucleotide_bases: Final = NucleotideBasesHandler()
