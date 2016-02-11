#! /usr/local/bin/python
import csv
import pickle
import pprint

file = '/Users/michaesm/Downloads/pickle_file_parameters_dont_plot.csv'
save_dir = '/Users/michaesm/Documents/'

reader = csv.reader(open(file, 'r'))

def save_obj(obj, name, s_dir):
    with open(s_dir + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def insertIntoDataStruct(aDict, key, value):
    if not key in aDict:
        aDict[key] = [value]
    else:
        aDict[key].append(value)


d = {}

for row in reader:
    k,v = row
    insertIntoDataStruct(d, k, v)


# for key in d.keys():
    # d[key].append('lon')
    # d[key].append('lat')
    # d[key].append('int_ctd_pressure')

output = open('/Users/michaesm/Documents/ooi_nonscience_parameters.pkl', 'wb')
pickle.dump(d, output)
output.close()
