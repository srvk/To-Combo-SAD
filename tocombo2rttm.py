#!/usr/bin/env python
#
# tocombo2rttm.py
#
# Given output of ToComboSAD, consisting of a list of (onset, offset, 0 or 1)
# as frames of either speech or nonspeech
# produce a sequence of utterances in RTTM format, collapsing duplicate frames

# Apache 2.0


import sys

firsttime=True

# iterate through file

fread = open(sys.argv[1], 'r')

lastframe = "0"
thesum = 0
theonset = 0
filename = sys.argv[1].split(".")[0]  # massage into basename (all before first ".")

for frame in fread.readlines():
    frame = frame.replace('\n','').strip()
    fields = frame.split('\t')

    onset = fields[0]
    offset = fields[1]
    yesno = fields[2]

    if yesno == "0": # output utterance when transition from 1 to 0
        if lastframe == "1":
            print "SPEAKER", filename, "1", theonset, thesum, " <NA> <NA> spkr <NA>"
    else:
        if lastframe == "1": # keep adding up "on" frames
            thesum = thesum + 0.01
        else: # went from off to on: reset sum, start counting
            thesum = 0.01
            theonset = onset
    lastframe = yesno

# last frame may be "1" - if so, we need to output a final utterance
if yesno == "1":
    print "SPEAKER", filename, "1", theonset, thesum, " <NA> <NA> spkr <NA>"

fread.close()
