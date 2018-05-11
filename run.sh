#!/bin/bash

# run.sh
#
# run ToComboSAD on a .wav file

if [ $# -ne 2 ]; then
  echo "Usage: run.sh <wavfile.wav>"
  echo "where wavfile is the name of a wav file"
  echo "output is <wavfile>.ToCombo.rttm"
  exit 1;
fi


SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
BASEDIR=`dirname $SCRIPT`

filename=$(basename "$1")
dirname=$(dirname "$1")
extension="${filename##*.}"
basename="${filename%.*}"

MCR=/usr/local/MATLAB/MATLAB_Runtime/v93
export LD_LIBRARY_PATH=$MCR/runtime/glnxa64:$MCR/bin/glnxa64:$MCR/sys/os/glnxa64:

echo $1 > $BASEDIR/filelist.txt

./run_get_TOcomboSAD_output_v3.sh $MCR $BASEDIR/filelist.txt 0 0.5 $BASEDIR/UBMnodct256Hub5.txt
python $BASEDIR/tocombo2rttm.py $1.ToCombo.txt > $dirname/$basename.ToCombo.rttm

