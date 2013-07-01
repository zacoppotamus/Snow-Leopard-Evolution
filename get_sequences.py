#Get sequences for now leopard and some derivative species

import os
from Bio import SeqIO
from Bio import Entrez

Entrez.email = "me@izac.us"
species = {
	"uncia_uncia" : "187250378",
	"panthera_pardus" : "482514544",
	"panthera_leo_persica" : "482514544",
	"panthera_tigris_sumatrae" : "339716942",
	"neofelis_nebulosa" : "78157535",
	"felis_catus" : "1098523",
	"herpestes_javanicus" : "57014054"
}

for specie in species:
	filename = specie + ".gbk"
	if not os.path.isfile(filename):
	    net_handle = Entrez.efetch(db="nucleotide",id=species[specie],rettype="gb", retmode="text")
	    out_handle = open(filename, "w")
	    out_handle.write(net_handle.read())
	    out_handle.close()
	    net_handle.close()
	    print "Saved"


