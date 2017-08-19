"""
次元
"""

import numpy as np


def num_of_dimensions(np_array):
    """受け取った numpy 配列の次元数を表示する"""
    print(f"{np.ndim(np_array)}次元")
    print(f"shape: {np_array.shape}")


def simple_neural_network():
    """
    内積を用いて簡単な NN を構築する
    内積を用いることで 出力 y を一度に計算できる
    """

    x = np.array([1, 2])
    print(x)
    print(x.shape)

    w = np.array([[1, 3, 5], [2, 4, 6]])
    print(w)
    print(w.shape)

    y = np.dot(x, w)
    print(y)
    print(y.shape)


if __name__ == '__main__':
    # 1次元
    # num_of_dimensions(np.array([1, 2, 3]))

    # 2次元（行列）
    ## 内積（ドット積）
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[1, 2], [3, 4], [5, 6]])
    print(A.shape)
    print(B.shape)
    print(np.dot(A, B))

    ## 列数と行数があっていれば１次元でも積を求めることが可能
    A = np.array([[1, 2], [3, 4], [5, 6]])
    B = np.array([1, 2])
    print(np.dot(A, B))

    print("simple_neural_network")
    simple_neural_network()
