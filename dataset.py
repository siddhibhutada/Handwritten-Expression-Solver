import os
from collections import defaultdict

imagefiles = []
image_file_dic_train=defaultdict(list)
image_file_dic_eval=defaultdict(list)
ignore_list=[]
for root, dirs, files in os.walk("C:\\Users\\Dell\\Downloads\\archive"):
    for name in files:
        if name.endswith((".jpg", ".jpeg")):
            if 'eval' in root:
                image_file_dic_eval[os.path.join(root)].append(os.path.join(root, name))
            else:
                image_file_dic_train[os.path.join(root)].append(os.path.join(root, name))
    # file = [
    #     [os.path.join(root)], [
    #         os.path.join(root, name)
    #         for name in files
    #         if name.endswith((".jpg", ".jpeg"))]]
    # imagefiles.append(file)
#print(imagefiles)
for k,v in image_file_dic_train.items():
    # print(k, v[:5])
    print(k)
