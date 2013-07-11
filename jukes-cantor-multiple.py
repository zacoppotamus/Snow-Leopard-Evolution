#!/usr/bin/env python
import sys
import math

USAGE = """USAGE: jukes-cantor-multiple.py <sequences>

  Input is a file containing two or more DNA or protein sequences, one
  per line.  Output is the matrix of Jukes-Cantor distance between
  them, printed to standard output.

"""

# Parse the command line.
if (len(sys.argv) != 2):
  sys.stderr.write(USAGE)
  sys.exit(1)
sequenceFileName = sys.argv[1]

# Read the two sequences.
sequenceFile = open(sequenceFileName, "r")
sequences = []
for line in sequenceFile:
  sequences.append(line.rstrip())
sequenceFile.close()
sys.stderr.write("Read %d sequences from %s.\n" %
                 (len(sequences), sequenceFileName))

# Complain if they are not the same length.
## NOT YET IMPLEMENTED.

# Consider each pair of sequences.
for sequence1 in sequences:
  for sequence2 in sequences:

    # Compute the number of differences.
    numDiffs = 0
    for index in range(0, len(sequence1)):
      if (sequence1[index] != sequence2[index]):
        numDiffs += 1
#    sys.stderr.write("%d differences.\n" % numDiffs)

    if (numDiffs == 0):
      distance = 0.0
    else:
      distance = -0.75 * math.log(1 - (4.0 / 3.0) *
                                  (float(numDiffs) / len(sequence1)), math.e)
    sys.stdout.write("%6.3f " % distance)
  sys.stdout.write("\n")
