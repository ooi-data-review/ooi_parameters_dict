# ooi-parameters-dict
A repository containing a pickle (.pkl) file containing a serialized Python dictionary of streams and each streams corresponding science parameters.


To use:
import pickle

# read python dict back from the file
pkl_file = open('ooi_plotting_parameters.pkl', 'rb')
varDict = pickle.load(pkl_file)
pkl_file.close()
