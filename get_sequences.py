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
	"puma_concolor" : "364284064",
	"panthera_tigris_sumatrae" : "339716942",
	"neofelis_nebulosa" : "78157535",
	"felis_catus" : "1098523",
	"herpestes_javanicus" : "57014054",
	"vulpes_vulpes" : "353731398"
}

species_cytb = {
	"uncia_uncia" : "402234444",
	"panthera_pardus" : "187250361",
	"puma_concolor" : "359741848",
	"panthera_tigris_sumatrae" : "339716955",
	"neofelis_nebulosa" : "115531622",
	"felis_catus" : "68299573",
	"herpestes_javanicus" : "58578661",
	"vulpes_vulpes" : "393713550"
}

species_cytc = {
	"uncia_uncia" : "145558799",
	"panthera_pardus" : "187250351",
	"puma_concolor" : "359741838",
	"panthera_tigris_sumatrae" : "339716945",
	"neofelis_nebulosa" : "115531612",
	"felis_catus" : "5835208",
	"herpestes_javanicus" : "58578653",
	"vulpes_vulpes" : "353731401"
}

# Retrieve mtDNA sequences
for specie in species_mtdna:
	filename = specie + ".fasta"
	save_seq_file(filename, species_mtdna[specie], "fasta", False)

# Retrieve amino acid sequences (CTB and COX1). Put cytb of fox (outgroup) in separate file
for specie in species_cytb:
	if specie != 'vulpes_vulpes':
		save_seq_file("cytb.fasta", species_cytb[specie], "fasta", True)
	else:
		save_seq_file("vulpes_vulpes.fasta", species_cytb[specie], "fasta", False)
	save_seq_file("cytc.fasta", species_cytc[specie], "fasta", True)

# Very basic NT statistical analysis
for specie in species_mtdna:
	filename = specie + ".fasta"
	for seq_record in SeqIO.parse(filename,"fasta"):
		print specie
		print repr(seq_record.seq)
		sequence_length = len(seq_record.seq)
		print "Length:", len(seq_record.seq)
		sequence = seq_record.seq
		for base in 'ACGT':
			occurences = sequence.count(base)
			print base, occurences, "%:", float(occurences)/sequence_length
		print "\n"

# Write all mtdna .fasta files in one
for specie in species_mtdna:
	fin = open(specie+".fasta", "r")
	data = fin.read()
	fin.close()
	fout = open("mtdna.fasta", "a")
	fout.write(data)
	fout.close()



