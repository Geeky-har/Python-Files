import pickle

data_list = []
fobj = open("iris.data", "r")

for i in fobj:
    con = fobj.readline()
    data_list.append(con)

# to pickle the iris dataset

fobj2 = open("irisPickle.pkl", "wb")
pickle.dump(data_list, fobj2)
fobj2.close()

# code for unpickling the dataset

fobj3 = open("irisPickle.pkl", "rb")
content = pickle.load(fobj3)
print(content)
print(type(content))
