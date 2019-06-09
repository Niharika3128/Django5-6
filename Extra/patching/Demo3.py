
import pickle

names = ["Ravi","Kumar","Mohan"]
file = open("sample","wb")
pickle.dump(names,file)
file.close()
print("Data Written to File")
