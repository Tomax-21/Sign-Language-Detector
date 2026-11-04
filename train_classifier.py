import pickle

data_dict = pickle.load(open("./data.picle", "rb"))

print(data_dict.keys())
print(data_dict)