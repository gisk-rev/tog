from tog import AminoAcid, Chromosome, Codon
from tog import Mutation, NucleicAcid, NucleotideBase
import unittest

# -------------
# Class Tester.
# -------------


class Tester(unittest.TestCase):

    ############################
    ########## PUBLIC ##########
    ############################

    def test_amino_acids(self):
        """
        Test amino acids data.
        """
        for amino_acid in AminoAcid:
            self.assertTrue(amino_acid.full_name != '')
            self.assertTrue(amino_acid.chemical_name != '')
            self.assertTrue(amino_acid.formula != '')
            self.assertTrue(amino_acid.molar_mass != '')
            self.assertTrue(amino_acid.isoelectric_point != '')
            self.assertTrue(amino_acid.smiles != '')
            self.assertTrue(amino_acid.codons != '')

        codons = AminoAcid.ALANINE.codons
        self.assertTrue(codons[0] == Codon.GCA)

    def test_chromosomes(self):
        """
        Test chromosomes data.
        """
        for chromosome in Chromosome:
            self.assertTrue(chromosome.group != '')
            self.assertTrue(chromosome.size != '')
            self.assertTrue(chromosome.centromere_position != '')
            self.assertTrue(chromosome.genes_number != '')
            self.assertTrue(chromosome.bases_number != '')
            self.assertTrue(chromosome.is_sex_chromosome != '')

        self.assertTrue(Chromosome._X.is_sex_chromosome)
        self.assertTrue(Chromosome._Y.is_sex_chromosome)

    def test_codons(self):
        """
        Test codons data.
        """
        for codon in Codon:
            self.assertTrue(codon.amino_acid != '')
            self.assertTrue(codon.is_stop_codon != '')
            self.assertTrue(codon.nucleotide_bases != '')

        amino_acid = Codon.GCA.amino_acid
        self.assertTrue(amino_acid == AminoAcid.ALANINE)

        nucleotide_bases = Codon.GCA.nucleotide_bases
        self.assertTrue(nucleotide_bases[0] == NucleotideBase.GUANINE)
        self.assertTrue(nucleotide_bases[1] == NucleotideBase.CYTOSINE)
        self.assertTrue(nucleotide_bases[2] == NucleotideBase.ADENINE)

        self.assertTrue(Codon.TAA.is_stop_codon)
        self.assertTrue(Codon.TAG.is_stop_codon)
        self.assertTrue(Codon.TGA.is_stop_codon)
        self.assertTrue(Codon.UAA.is_stop_codon)
        self.assertTrue(Codon.UAG.is_stop_codon)
        self.assertTrue(Codon.UGA.is_stop_codon)

    def test_mutations(self):
        """
        Test mutations data.
        """
        for mutation in Mutation:
            self.assertTrue(mutation.full_name != '')
            self.assertTrue(mutation.effect != '')

    def test_nucleic_acids(self):
        """
        Test nucleic acids data.
        """
        for nucleic_acid in NucleicAcid:
            self.assertTrue(nucleic_acid.code != '')
            self.assertTrue(nucleic_acid.chemical_name != '')
            self.assertTrue(nucleic_acid.structure != '')
            self.assertTrue(nucleic_acid.nucleotide_bases != '')

        nucleotide_bases = NucleicAcid.DNA.nucleotide_bases
        self.assertTrue(nucleotide_bases[0] == NucleotideBase.ADENINE)
        self.assertTrue(nucleotide_bases[1] == NucleotideBase.THYMINE)
        self.assertTrue(nucleotide_bases[2] == NucleotideBase.CYTOSINE)
        self.assertTrue(nucleotide_bases[3] == NucleotideBase.GUANINE)

        nucleotide_bases = NucleicAcid.RNA.nucleotide_bases
        self.assertTrue(nucleotide_bases[0] == NucleotideBase.ADENINE)
        self.assertTrue(nucleotide_bases[1] == NucleotideBase.URACIL)
        self.assertTrue(nucleotide_bases[2] == NucleotideBase.CYTOSINE)
        self.assertTrue(nucleotide_bases[3] == NucleotideBase.GUANINE)

    def test_nucleotide_bases(self):
        """
        Test nucleotide bases data.
        """
        for nucleotide_base in NucleotideBase:
            self.assertTrue(nucleotide_base.full_name != '')
            self.assertTrue(nucleotide_base.chemical_name != '')
            self.assertTrue(nucleotide_base.formula != '')
            self.assertTrue(nucleotide_base.molar_mass != '')
            self.assertTrue(nucleotide_base.smiles != '')

if __name__ == '__main__':
	unittest.main()
