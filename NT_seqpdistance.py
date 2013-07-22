#!usr/bin/python
# Calculate pairwise sequence distance of NT

from cogent import LoadSeqs
from cogent import PROTEIN, DNA
from cogent.evolve.models import JTT92, JC69
from cogent.phylo import nj, distance
from cogent.app.muscle_v38 import align_unaligned_seqs
from seqpdistance import phyl_tree
import sys

# Read .fasta file by passing filename. Returns a (name-sequence) tuple
def read_fasta(fp):
	name, seq, temp = [], [], []
	for line in open(fp):
		line = line.rstrip()
		if line.startswith(">"):
			name.append(line.replace(">",""))
			if (temp!=[]):
				seq.append(''.join(temp))
			temp = []
		else:
			temp.append(line.rstrip())
	seq.append(''.join(temp))
	return name, seq

specie, seq = read_fasta("mtdna.fasta")

# NCBI protein sequence location is inclusive.
# Take cytb and cytc subsequences from mtdna and spit them out to fasta file.
cytb_nt = []
cytc_nt = []

cytb_nt.append(seq[0][14172:15312]) # Tiger
cytb_nt.append(seq[1][15084:16224]) # Cougar
cytb_nt.append(seq[2][15126:16266]) # Leopard
cytb_nt.append(seq[3][15065:16205]) # C. Leopard
cytb_nt.append(seq[4][14168:15308]) # Asian Mongoose
cytb_nt.append(seq[5][15037:16177]) # Cat
cytb_nt.append(seq[6][14920:16060]) # Snow Leopard
cytb_nt.append(seq[7][14185:15325]) # Red Fox

cytc_nt.append(seq[0][6279:7824]) # Tiger
cytc_nt.append(seq[1][6262:7807]) # Cougar
cytc_nt.append(seq[2][6304:7849]) # Leopard
cytc_nt.append(seq[3][6243:7788]) # C. Leopard
cytc_nt.append(seq[4][5347:6892]) # Asian Mongoose
cytc_nt.append(seq[5][6215:7760]) # Cat
cytc_nt.append(seq[6][6098:7643]) # Snow Leopard
cytc_nt.append(seq[7][5350:6895]) # Red Fox

# Write to file
fb = open("nt_cytb.fasta", "w")
fc = open("nt_cytc.fasta", "w")
for i, name in enumerate(specie):
	fb.write(">" + name)
	fc.write(">" + name)
	fb.write(cytb_nt[i])
	fc.write(cytc_nt[i])
fc.close()
fb.close()
