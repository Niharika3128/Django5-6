

import pickle

file = open("sample","rb")

names = pickle.load(file)

print(names)