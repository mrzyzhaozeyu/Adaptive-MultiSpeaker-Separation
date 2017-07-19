########################
## DATA CONFIGURATION ##
########################

data_root = 'data/LibriSpeech'
data_subset = 'dev-clean'

#########################
## AUDIO CONFIGURATION ##
#########################

fs = 8000 
fftsize = 256
overlap = 2
window = 'hann'


#########################

embedding_size = 40
threshold = 1e-8
chunk_size = 40
batch_size = 32