#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt 

def one_hot_encoder(data, whole_set):
    """
     对整个list做encoder，而不是单个record
    """
    ret = []
    for i in data:
        idx = whole_set.index(i)
        ret.append([1 if j==idx else 0 for j in range(len(whole_set))])
    return ret


def one_hot_decoder(data, whole_set):
    ret = []
    for probs in data:
        idx = np.argmax(probs)
        ret.append(whole_set[idx])
    return ret


def plot_loss_figure(history, save_path):
    train_loss = history.history['loss']
    val_loss = history.history['val_loss']
    plt.plot(train_loss, 'b', val_loss, 'r')
    plt.xlabel('train_loss: blue   val_loss: red      epoch')
    plt.ylabel('loss')
    plt.title('loss figure')
    plt.savefig(save_path)


def pack_data(X, Y_nb, Y, max_nb_cha):
    """
    pack data to match keras format
    """
    data = {'output%d'%i:Y[i-1] for i in range(1, max_nb_cha+1)}
    data['input'] = X
    data['output_nb'] = Y_nb
    return data