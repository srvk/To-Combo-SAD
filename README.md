# TOcomboSAD
Speech activity detection 

# NOTE:

Any public reports or papers derived using these scripts should cite the following two papers:

[1] S.O. Sadjadi, J.H.L. Hansen, "Unsupervised Speech Activity Detection using Voicing Measures and Perceptual Spectral Flux," IEEE Signal Processing Letters, vol. 20, no. 3, pp. 197-200, March 2013 

[2] A. Ziaei, L. Kaushik, A. Sangwan, J.H.L. Hansen, "Speech Activity Detection for NASA Apollo Space Missions: Challenges and Solutions," ISCA Interspeech-2014, Paper #994, Singapore, Sept. 14-18, 2014

## Running

### Easier run script:
```
./run.sh <wavfile.wav>
```
Sets environment  
Runs ToComboSAD  
Converts to RTTM  
Places output in `<wavfile>.ToCombo.rttm`

Example:
```
sox /vagrant/test2.mp3 /vagrant/test2.wav
./run.sh /vagrant/test2.wav
cat /vagrant/test2.ToCombo.rttm
SPEAKER /vagrant/test2 1 0 1.98  <NA> <NA> spkr <NA>
SPEAKER /vagrant/test2 1 2.52 3.17  <NA> <NA> spkr <NA>
SPEAKER /vagrant/test2 1 6.49 3.3  <NA> <NA> spkr <NA>
SPEAKER /vagrant/test2 1 10.88 2.69  <NA> <NA> spkr <NA>
```
