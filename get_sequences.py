#Get sequences for snow leopard and some derivative species

import os
from Bio import SeqIO
from Bio import Entrez

def save_seq_file (filename, g_id, type, append):
	# Comment the next line out after retrieving AA sequences
	if not os.path.isfile(filename):
	    net_handle = Entrez.efetch(db="nucleotide",id=g_id,rettype=type, retmode="text")
	    out_handle = open(filename, "a" if append else "w" )
	    out_handle.write(net_handle.read())
	    out_handle.close()
	    net_handle.close()
	    print "Saved"

Entrez.email = "me@izac.us"
species_mtdna = {
	"uncia_uncia" : "187250378",
	"panthera_pardus" : "187250348",
	"panthera_leo_persica" : "482514544",
	"panthera_tigris_sumatrae" : "339716942",
	"neofelis_nebulosa" : "78157535",
	"felis_catus" : "1098523",
	"herpestes_javanicus" : "57014054"
}

species_cytb = {
	"uncia_uncia" : "402234444",
	"panthera_pardus" : "187250361",
	"panthera_leo_persica" : "482514557",
	"panthera_tigris_sumatrae" : "339716955",
	"neofelis_nebulosa" : "115531622",
	"felis_catus" : "68299573",
	"herpestes_javanicus" : "58578661"
}

species_cytc = {
	"uncia_uncia" : "145558799",
	"panthera_pardus" : "187250351",
	"panthera_leo_persica" : "482514547",
	"panthera_tigris_sumatrae" : "339716945",
	"neofelis_nebulosa" : "115531612",
	"felis_catus" : "5835208",
	"herpestes_javanicus" : "58578653"
}

# Retrieve mtDNA sequences
for specie in species_mtdna:
	filename = specie + ".gbk"
	save_seq_file(filename, species_mtdna[specie], "gb", False)

# Retrieve Cytochrome B sequences and Cytochrome C Oxidase Subunit 1 sequences
for specie in species_cytb:
	filename = specie + "_cytb.gbk"
	save_seq_file(filename, species_cytb[specie], "gb", False)
	filename = specie + "_cytc.gbk"
	save_seq_file(filename, species_cytc[specie], "gb", False)

#Retrieve amino acid sequences
for specie in species_cytb:
	save_seq_file("cytb.fasta", species_cytb[specie], "fasta", True)
	save_seq_file("cytc.fasta", species_cytc[specie], "fasta", True)

for specie in species_mtdna:
	filename = specie + ".gbk"
	for seq_record in SeqIO.parse(filename,"genbank"):
		print specie
		print repr(seq_record.seq)
		sequence_length = len(seq_record.seq)
		print "Length:", len(seq_record.seq)
		sequence = seq_record.seq
		for base in 'ACGT':
			occurences = sequence.count(base)
			print base, occurences, "%:", float(occurences)/sequence_length
		print "\n"




