import pandas as pd
import numpy as np
import time
import random

delete_threshold = 30
path_imgs = []
start_time = time.time()
one_hot = pd.read_csv("./one_hot.csv", header=None).to_numpy()
others_path_img = []
# Remove any classes having < delete_threshold labels
count_labels = pd.read_csv("./count_labels.csv", header=None).to_numpy()
diag_index = np.diag_indices(len(count_labels))
remove_indices = np.where((count_labels[diag_index] < delete_threshold) == True)
one_hot = np.delete(one_hot, remove_indices, 1)



# Balance data

## Balace the min class first
def balance_min_class(balance_classes, one_hot):
    # Get min class
    remove_indices = np.where((count_labels[diag_index] < delete_threshold) == True)
    diag_matrix = np.delete(count_labels.copy(), remove_indices, 1)
    diag_matrix = np.delete(diag_matrix, remove_indices, 0)
    min_class_index = diag_matrix[np.diag_indices(len(diag_matrix))].argmin()
    index_min_class = np.array(np.where(one_hot[:, min_class_index] == 1)).squeeze()
    for item in index_min_class:
        path_imgs.append(item)

    for i in range(len(index_min_class)):
        balance_classes = np.add(balance_classes, one_hot[index_min_class[i]])
    one_hot = np.delete(one_hot, index_min_class, 0)
    return balance_classes, one_hot

def balance_others_class(balance_classes, one_hot):
    # Get class 
    remove_indices = np.where((count_labels[diag_index] >= delete_threshold) == True)
    diag_matrix = np.delete(count_labels.copy(), remove_indices, 1)
    diag_matrix = np.delete(diag_matrix, remove_indices, 0)
    other_class_index = diag_matrix[np.diag_indices(len(diag_matrix))].argmin()
    index_other_class = np.array(np.where(one_hot[:, other_class_index] == 1)).squeeze()
    for item in index_other_class:
        path_imgs.append(item)

    for i in range(len(index_other_class)):
        balance_classes = np.add(balance_classes, one_hot[index_other_class[i]])
    one_hot = np.delete(one_hot, index_other_class, 0)
    return balance_classes, one_hot

balance_classes = np.zeros((one_hot.shape[1], ), dtype=int)
# balance_classes, one_hot = balance_others_class(balance_classes, one_hot)
print(balance_classes)
len_one_hot = len(one_hot)

## Then balance other classes
balance_threshold = 30
prob_min = 1
count = 0
while True:
    count += 1
    if random.random() < prob_min:
        min_indices = np.where(balance_classes == np.amin(balance_classes))
        # near_near_min_indices = np.where(balance_classes == np.amin(balance_classes) + 2)
        near_min_indices = np.where(balance_classes == np.amin(balance_classes) + 1)
        min_indices = np.append(min_indices, near_min_indices)
        # min_indices = np.append(min_indices, near_near_min_indices)
        tmp = one_hot[:, min_indices].copy().squeeze()
        if len(tmp.shape) < 2:
            tmp = np.reshape(tmp, (tmp.shape[0], 1))
        most_one_of_zero = np.count_nonzero(tmp, axis=1).argmax()
        balance_classes = np.add(balance_classes, one_hot[most_one_of_zero])
        one_hot = np.delete(one_hot, most_one_of_zero, 0)
        path_imgs.append(most_one_of_zero)
    else:
        max_indices = np.where(balance_classes == np.amax(balance_classes))
        tmp = one_hot[:, max_indices].copy().squeeze()
        if len(tmp.shape) < 2:
            tmp = np.reshape(tmp, (tmp.shape[0], 1))
        most_zero_of_one = (tmp == 0).sum(1).argmax()
        balance_classes = np.add(balance_classes, one_hot[most_zero_of_one])
        one_hot = np.delete(one_hot, most_zero_of_one, 0)
        path_imgs.append(most_zero_of_one)
    if (balance_classes >= balance_threshold).all() or count == len_one_hot-1:
        print(balance_classes)
        np.savetxt('balance_classes.csv', balance_classes, delimiter=',')
        break
end_time = time.time()
print("Total time: {:.3f} seconds".format(end_time - start_time))

dict_path = {"image": [], "id": []}
mapping = pd.read_csv("json_mapping.csv")
for id_path in path_imgs:
    dict_path["id"].append(id_path)
    dict_path["image"].append(mapping.iloc[id_path][0])
df = pd.DataFrame(dict_path)
df.to_csv("image_path.csv", index=False)