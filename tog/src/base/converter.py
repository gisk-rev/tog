# --------------------------------------------
# Class Converter.
# Singleton pattern.
# --------------------------------------------


class Converter(object):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Converter, cls).__new__(cls)
        return cls._instance

    ############################
    ########## PUBLIC ##########
    ############################

    def get_enum_amino_acid(amino_acid_code):
        from tog.src.classes.amino_acids.amino_acid import AminoAcid
        """
        Get the enum amino acid.

        Parameters
        ----------
        amino_acid_code : string
            An amino acid code.

        Returns
        -------
        found : AminoAcid
            The amino acid found.
        """
        found = None
        for amino_acid in AminoAcid:
            if amino_acid.value == amino_acid_code:
                found = amino_acid

        return found

    def get_enum_codons(codons_codes_list):
        from tog.src.classes.codons.codon import Codon
        """
        Get a list of enum codons.

        Parameters
        ----------
        codons_codes_list : string[]
            A list of codons codes.

        Returns
        -------
        codons : Codon[]
            A list of enum codons.
        """
        codons = []
        for codon in Codon:
            if codon.value in codons_codes_list:
                codons.append(codon)

        return codons
    
    def get_enum_nucleotide_bases(codon_code):
        from tog.src.classes.nucleotide_bases.nucleotide_base import NucleotideBase
        """
        Get a list of enum nucleotide bases.

        Parameters
        ----------
        codon_code : string
            A codon code.

        Returns
        -------
        nucleotide_bases : NucleotideBase[]
            A list of enum nucleotide bases.
        """
        nucleotide_bases = []
        for character in codon_code:
            for nucleotide_base in NucleotideBase:
                if nucleotide_base.value == character:
                    nucleotide_bases.append(nucleotide_base)

        return nucleotide_bases
