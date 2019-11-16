import pandas as pd
import numpy as np
import os

mode = "train"

df = pd.read_csv('./data/characters-digits-'+mode+'.csv', header=None)

mappings = pd.read_csv('./data/characters-digits-mapping.txt', sep='\s+', header=None)
mappings = mappings.values[:,1]

one_hots_ques1 = np.eye(2)
one_hots_ques2 = np.eye(4)
one_hots_ques3 = np.eye(mappings.shape[0])

img = []
tar_ques1 = []
tar_ques2 = []
tar_ques3 = []

for i in range(df.shape[0]):
	print(i)

	t = 1 if(df.iloc[i][0] >= 0 and df.iloc[i][0] <= 9 ) else 0
	tar_ques1.append(one_hots_ques1[t])

	temp = df.iloc[i][0]
	if(temp >= 0 and temp <= 9):
		temp = 0 if(temp%2 == 0) else 1
	else:
		temp = 2 if(temp in vowels) else 3
	tar_ques2.append(one_hots_ques2[temp])
	
	tar_ques3.append(one_hots_ques3[df.iloc[i][0]])
	img.append(np.reshape(np.array(df.iloc[i][1:]), (1, 28, 28)).T)

img = np.array(img)

tar_ques1 = np.array(tar_ques1)
tar_ques2 = np.array(tar_ques2)
tar_ques3 = np.array(tar_ques3)

np.save("./npy_files/img_"+mode+".npy", img)

np.save("./npy_files/tar_"+mode+"_binary.npy", tar_ques1)
np.save("./npy_files/tar_"+mode+"_ques2.npy", tar_ques2)
np.save("./npy_files/tar_"+mode+".npy", tar_ques3)