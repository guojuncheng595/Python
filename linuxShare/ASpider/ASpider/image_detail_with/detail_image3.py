#-*-coding:utf-8-*-

import numpy as np
import os
import time

from PIL import Image
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier


def load_dataset():
    X = []
    y = []
    for i in "23456789ABVDEFGHKMNPRSTUVWXYZ":
        target_path = "fenlei/" + i
        print(target_path)
        for title in os.listdir(target_path):
            pix = np.asarray(Image.open(os.path.join(target_path, title)).convert('L'))
            X.append(pix.reshape(25 * 30))
            y.append(target_path.split('/')[-1])

    X = np.asarray(X)
    y = np.asarray(y)
    return X, y

def check_everyone(model):
    pre_list = []
    y_list = []
    for i in "23456789ABCDEFGHKMNPRSTUVWXYZ":
        part_path = "part/" + i
        for title in os.listdir(part_path):
            pix = np.asarray(Image.open(os.path.join(part_path, title)).convert('L'))
            pix = pix.reshape(25 * 30)
            pre_list.append(pix)
            y_list.append(part_path.split('/')[-1])
    pre_list = np.asarray(pre_list)
    y_list = np.asarray(y_list)

    result_list = model.predict(pre_list)
    acc = 0
    for i in result_list == y_list:
        print(result_list,y_list,)

        if i == np.bool(True):
            acc += 1
    print(acc, acc / len(result_list))


X, y = load_dataset()
knn = KNeighborsClassifier()
knn.fit(X, y)
joblib.dump(knn, 'yipai.model')
check_everyone(knn)