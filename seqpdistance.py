#!usr/bin/python
#Calculate pairwise sequence distance

from cogent import LoadSeqs
from cogent import PROTEIN, DNA
from cogent.phylo import distance
from cogent.evolve.models import AH96_mtmammals, JC69
from cogent.phylo import nj, distance
import sys

def phyl_tree():
	mytree = nj.nj(d.getPairwiseDistances())
	print ("\n\n")
	print mytree.asciiArt()

al = LoadSeqs("cytb.fasta", moltype=PROTEIN, interleaved=False)
d = distance.EstimateDistances(al, submodel = AH96_mtmammals())
d.run()
sys.stdout = open("cytb distances.txt", "w")
print d
phyl_tree()

al = LoadSeqs("cytc.fasta", moltype=PROTEIN, interleaved=False)
d = distance.EstimateDistances(al, submodel = AH96_mtmammals())
d.run()
sys.stdout = open("cytc distances.txt", "w")
print d
phyl_tree()

al = LoadSeqs("mtdna.fasta", moltype=DNA, interleaved=True, aligned=False)
d = distance.EstimateDistances(al, submodel = JC69())
d.run()
sys.stdout = open("mtdna distances.txt", "w")
print d
phyl_tree()

# Strip sequence for every specie, align it with red fox and get their pairwise distance
