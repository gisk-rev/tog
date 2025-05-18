# TOG (Terms of Genetics)
TOG is a simple package that provides a set of basic genetics information in the form of enum types.

## Features
The current available information is:

* __AminoAcid__
    * *code*
    * *full_name*
    * *chemical_name*
    * *formula*
    * *molar_mass*
    * *isoelectric_point*
    * *smiles*
    * *codons*
* __Chromosome__
    * *code*
    * *group*
    * *size*
    * *centromere_position*
    * *genes_number*
    * *bases_number*
    * *is_sex_chromosome*
* __Codon__
    * *code*
    * *amino_acid*
    * *is_stop_codon*
    * *nucleotide_bases*
* __Mutation__
    * *full_name*
    * *effect*
* __NucleicAcid__
    * *code*
    * *chemical_name*
    * *structure*
    * *nucleotide_bases*
* __NucleotideBase__
    * *code*
    * *full_name*
    * *chemical_name*
    * *formula*
    * *molar_mass*
    * *smiles*

Feel free to contact me to request more information or report corrections.

## Installation
You need Python 3 (tested on version 3.13) and [Pandas](https://github.com/pandas-dev/pandas) to run this package.

Download with:
```
git clone https://github.com/gisk-rev/tog.git
```
Inside the repository folder:
```
pip install -e .
```
## How to use
```
from tog import AminoAcid, Chromosome, Codon, Mutation, NucleicAcid, NucleotideBase

# Amino acids.
print(AminoAcid.ALANINE.code)  # A
print(AminoAcid.ALANINE.full_name)  # alanine
print(AminoAcid.ALANINE.chemical_name)  # 2-aminopropanoic acid
print(AminoAcid.ALANINE.formula)  # C3H7NO2
print(AminoAcid.ALANINE.molar_mass)  # 89.09 g/mol
print(AminoAcid.ALANINE.isoelectric_point)  # 6.11
print(AminoAcid.ALANINE.smiles)  # CC(C(=O)O)N
print(AminoAcid.ALANINE.codons)  # [Codon.GCA, Codon.GCC, Codon.GCG, Codon.GCU]

# Chromosomes.
print(Chromosome._1.code)  # 1
print(Chromosome._1.group)  # A
print(Chromosome._1.size)  # large
print(Chromosome._1.centromere_position)  # metacentric
print(Chromosome._1.genes_number)  # 2968
print(Chromosome._1.bases_number)  # 245203898
print(Chromosome._1.is_sex_chromosome)  # False

# Codons.
print(Codon.GCA.code)  # GCA
print(Codon.GCA.amino_acid)  # AminoAcid.ALANINE
print(Codon.GCA.is_stop_codon)  # False
print(Codon.GCA.nucleotide_bases) # [NucleotideBase.GUANINE, NucleotideBase.CYTOSINE, NucleotideBase.ADENINE]

# Mutations.
print(Mutation.CHROMOSOMAL_DELETION.full_name)  # chromosomal deletion
print(Mutation.CHROMOSOMAL_DELETION.effect)  # large scale mutation

# Nucleic acids.
print(NucleicAcid.DNA.code)  # DNA
print(NucleicAcid.DNA.chemical_name)  # deoxyribonucleic acid
print(NucleicAcid.DNA.structure)  # double-helix chain
print(NucleicAcid.DNA.nucleotide_bases) # [NucleotideBase.ADENINE, NucleotideBase.THYMINE, NucleotideBase.CYTOSINE, NucleotideBase.GUANINE]

# Nucleotide bases.
print(NucleotideBase.ADENINE.code)  # A
print(NucleotideBase.ADENINE.full_name)  # adenine
print(NucleotideBase.ADENINE.chemical_name)  # 9H-purin-6-amine
print(NucleotideBase.ADENINE.formula)  # C5H5N5
print(NucleotideBase.ADENINE.molar_mass)  # 135.13 g/mol
print(NucleotideBase.ADENINE.smiles)  # C1=NC2=C(N1)C(=NC=N2)N
```

## License
This package is available under the MIT License.
