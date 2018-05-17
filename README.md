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
### low level run script:
-run_get_TOcomboSAD_output.sh (shell script for temporarily setting environment variables 
                               and executing the application)
   -to run the shell script, type
   
       ./run_get_TOcomboSAD_output.sh /usr/local/MATLAB/MATLAB_Runtime/v93/ <argument_list>
       
    at the command prompt. <argument_list> is all the 
    arguments you want to pass to your application. For example, 
    
       ./run_get_TOcomboSAD_output_v3.sh /usr/local/MATLAB/MATLAB_Runtime/v93 /home/vagrant/TOcomboSAD/wav_filelist.txt 0 0.5 /home/vagrant/TOcomboSAD/UBMnodct256Hub5.txt

Output will be in sa2.wav.ToCombo.txt and look like:

```
0	0.01	1
0.01	0.02	1
0.02	0.03	1
0.03	0.04	1
0.04	0.05	1
0.05	0.06	1
0.06	0.07	1
0.07	0.08	1
0.08	0.09	1
0.09	0.1	1
0.1	0.11	1
0.11	0.12	1
0.12	0.13	1
0.13	0.14	1
0.14	0.15	1
0.15	0.16	1
0.16	0.17	1
0.17	0.18	1
0.18	0.19	1
0.19	0.2	1
0.2	0.21	1
0.21	0.22	1
0.22	0.23	1
0.23	0.24	1
0.24	0.25	1
0.25	0.26	1
0.26	0.27	1
0.27	0.28	1
0.28	0.29	1
0.29	0.3	1
0.3	0.31	1
0.31	0.32	1
0.32	0.33	1
0.33	0.34	1
0.34	0.35	1
0.35	0.36	1
0.36	0.37	1
0.37	0.38	1
0.38	0.39	1
0.39	0.4	1
0.4	0.41	1
0.41	0.42	1
0.42	0.43	1
0.43	0.44	1
0.44	0.45	1
0.45	0.46	1
0.46	0.47	1
0.47	0.48	1
0.48	0.49	1
0.49	0.5	1
0.5	0.51	1
0.51	0.52	1
0.52	0.53	1
0.53	0.54	1
0.54	0.55	1
0.55	0.56	1
0.56	0.57	1
0.57	0.58	1
0.58	0.59	1
0.59	0.6	1
0.6	0.61	1
0.61	0.62	1
0.62	0.63	1
0.63	0.64	1
0.64	0.65	1
0.65	0.66	1
0.66	0.67	1
0.67	0.68	1
0.68	0.69	1
0.69	0.7	1
0.7	0.71	1
0.71	0.72	1
0.72	0.73	1
0.73	0.74	1
0.74	0.75	1
0.75	0.76	1
0.76	0.77	1
0.77	0.78	1
0.78	0.79	1
0.79	0.8	1
0.8	0.81	1
0.81	0.82	1
0.82	0.83	1
0.83	0.84	1
0.84	0.85	1
0.85	0.86	1
0.86	0.87	1
0.87	0.88	1
0.88	0.89	1
0.89	0.9	1
0.9	0.91	1
0.91	0.92	1
0.92	0.93	1
0.93	0.94	1
0.94	0.95	1
0.95	0.96	1
0.96	0.97	1
0.97	0.98	1
0.98	0.99	1
0.99	1	1
1	1.01	1
1.01	1.02	1
1.02	1.03	1
1.03	1.04	1
1.04	1.05	1
1.05	1.06	1
1.06	1.07	1
1.07	1.08	1
1.08	1.09	1
1.09	1.1	1
1.1	1.11	1
1.11	1.12	1
1.12	1.13	1
1.13	1.14	1
1.14	1.15	1
1.15	1.16	1
1.16	1.17	1
1.17	1.18	1
1.18	1.19	1
1.19	1.2	1
1.2	1.21	1
1.21	1.22	1
1.22	1.23	1
1.23	1.24	1
1.24	1.25	1
1.25	1.26	1
1.26	1.27	1
1.27	1.28	1
1.28	1.29	1
1.29	1.3	1
1.3	1.31	1
1.31	1.32	1
1.32	1.33	1
1.33	1.34	1
1.34	1.35	1
1.35	1.36	1
1.36	1.37	1
1.37	1.38	1
1.38	1.39	1
1.39	1.4	1
1.4	1.41	1
1.41	1.42	1
1.42	1.43	1
1.43	1.44	1
1.44	1.45	1
1.45	1.46	1
1.46	1.47	1
1.47	1.48	1
1.48	1.49	1
1.49	1.5	1
1.5	1.51	1
1.51	1.52	1
1.52	1.53	1
1.53	1.54	1
1.54	1.55	1
1.55	1.56	1
1.56	1.57	1
1.57	1.58	1
1.58	1.59	1
1.59	1.6	1
1.6	1.61	1
1.61	1.62	1
1.62	1.63	1
1.63	1.64	1
1.64	1.65	1
1.65	1.66	1
1.66	1.67	1
1.67	1.68	1
1.68	1.69	1
1.69	1.7	1
1.7	1.71	1
1.71	1.72	1
1.72	1.73	1
1.73	1.74	1
1.74	1.75	1
1.75	1.76	1
1.76	1.77	1
1.77	1.78	1
1.78	1.79	1
1.79	1.8	1
1.8	1.81	1
1.81	1.82	1
1.82	1.83	1
1.83	1.84	1
1.84	1.85	1
1.85	1.86	1
1.86	1.87	1
1.87	1.88	1
1.88	1.89	1
1.89	1.9	1
1.9	1.91	1
1.91	1.92	1
1.92	1.93	1
1.93	1.94	1
1.94	1.95	1
1.95	1.96	1
1.96	1.97	1
1.97	1.98	1
1.98	1.99	1
1.99	2	1
2	2.01	1
2.01	2.02	1
2.02	2.03	1
2.03	2.04	1
2.04	2.05	1
2.05	2.06	1
2.06	2.07	1
2.07	2.08	1
2.08	2.09	1
2.09	2.1	1
2.1	2.11	1
2.11	2.12	1
2.12	2.13	1
2.13	2.14	1
2.14	2.15	1
2.15	2.16	1
2.16	2.17	1
2.17	2.18	1
2.18	2.19	1
2.19	2.2	1
2.2	2.21	1
2.21	2.22	1
2.22	2.23	1
2.23	2.24	1
2.24	2.25	1
2.25	2.26	1
2.26	2.27	1
2.27	2.28	1
2.28	2.29	1
2.29	2.3	1
2.3	2.31	1
2.31	2.32	1
2.32	2.33	1
2.33	2.34	1
2.34	2.35	1
2.35	2.36	1
2.36	2.37	1
2.37	2.38	1
2.38	2.39	1
2.39	2.4	1
2.4	2.41	1
2.41	2.42	1
2.42	2.43	1
2.43	2.44	1
2.44	2.45	1
2.45	2.46	1
2.46	2.47	1
2.47	2.48	1
2.48	2.49	1
2.49	2.5	1
2.5	2.51	1
2.51	2.52	1
2.52	2.53	1
2.53	2.54	1
2.54	2.55	1
2.55	2.56	1
2.56	2.57	1
2.57	2.58	1
2.58	2.59	1
2.59	2.6	1
2.6	2.61	1
2.61	2.62	1
2.62	2.63	1
2.63	2.64	1
```
