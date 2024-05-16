import numpy as np
import scipy.io as io


def load_data():
    # Source data
    file = io.loadmat('./Data/Dataset_1Circle')
    s_bc = 101
    s = 1048
    f_train = file['f_bc_train']
    ux_train = file['ux_train'] * 1e5
    uy_train = file['uy_train'] * 1e5

    f_test = file['f_bc_test']
    ux_test = file['ux_test'] * 1e5
    uy_test = file['uy_test'] * 1e5

    xx = file['xx']
    yy = file['yy']
    xx = np.reshape(xx, (-1, 1))
    yy = np.reshape(yy, (-1, 1))
    X = np.hstack((xx, yy))

    f_train_mean = np.mean(np.reshape(f_train, (-1, s_bc)), 0)
    f_train_std = np.std(np.reshape(f_train, (-1, s_bc)), 0)
    ux_train_mean = np.mean(np.reshape(ux_train, (-1, s)), 0)
    ux_train_std = np.std(np.reshape(ux_train, (-1, s)), 0)
    uy_train_mean = np.mean(np.reshape(uy_train, (-1, s)), 0)
    uy_train_std = np.std(np.reshape(uy_train, (-1, s)), 0)

    f_train_mean = np.reshape(f_train_mean, (-1, 1, s_bc))
    f_train_std = np.reshape(f_train_std, (-1, 1, s_bc))
    ux_train_mean = np.reshape(ux_train_mean, (-1, s, 1))
    ux_train_std = np.reshape(ux_train_std, (-1, s, 1))
    uy_train_mean = np.reshape(uy_train_mean, (-1, s, 1))
    uy_train_std = np.reshape(uy_train_std, (-1, s, 1))

    F_train = np.reshape(f_train, (-1, 1, s_bc))
    F_train = (F_train - f_train_mean) / (f_train_std + 1.0e-9)
    Ux_train = np.reshape(ux_train, (-1, s, 1))
    Ux_train = (Ux_train - ux_train_mean) / (ux_train_std + 1.0e-9) + 8.5
    Uy_train = np.reshape(uy_train, (-1, s, 1))
    Uy_train = (Uy_train - uy_train_mean) / (uy_train_std + 1.0e-9) + 8.5

    F_test = np.reshape(f_test, (-1, 1, s_bc))
    F_test = (F_test - f_train_mean) / (f_train_std + 1.0e-9)
    Ux_test = np.reshape(ux_test, (-1, s, 1))
    Ux_test = (Ux_test - ux_train_mean) / (ux_train_std + 1.0e-9) + 8.5
    Uy_test = np.reshape(uy_test, (-1, s, 1))
    Uy_test = (Uy_test - uy_train_mean) / (uy_train_std + 1.0e-9) + 8.5

    return F_train, Ux_train, Uy_train, F_test, Ux_test, Uy_test, X, ux_train_mean, \
        ux_train_std, uy_train_mean, uy_train_std


def rescale(x, u_mean, u_std):
    x = x * (u_std + 1.0e-9) + u_mean
    return x
