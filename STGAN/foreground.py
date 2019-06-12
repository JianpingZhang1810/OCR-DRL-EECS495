import numpy as np
import scipy.misc

celebA_path = "/clever/northwestern/jianping/CelebA/dataset"
output_path = "dataset"

part_dict = {}
with open("{0}/split.txt".format(celebA_path)) as file:
	for line in file:
		token = line.strip().split()
		part_dict[token[0]] = token[1]

for type in ["train","test"]:
	L = []
	for key in part_dict:
		if part_dict[key]==("0" if type=="train" else "2" if type=="test" else None):
			L.append(key)
	count = len(L)
	images = np.ones([count,144,144,3],dtype=np.uint8)
	for i in range(len(L)):
		key = L[i]
		#img = scipy.misc.imread("{0}/dataset/{1}".format(celebA_path,key))
		img = scipy.misc.imread("{0}".format(key))
		images[i] = img
		print("{0} {1}/{2} done".format(type,i,len(L)))
	np.save("{0}/background_{1}.npy".format(output_path,type),images)

