"""
3.4 ニューラルネットワーク

適当なパラメータで3ネットワークを作ってみる
"""

import numpy as np
import activation
import assertion


def layer1(x):
    """隠れ層 第一層"""
    w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    b1 = np.array([0.1, 0.2, 0.3])
    a1 = np.dot(x, w1) + b1
    return activation.sigmoid(a1)


def layer2(z1):
    """隠れ層 第二層"""
    w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    b2 = np.array([0.1, 0.2])
    a2 = np.dot(z1, w2) + b2
    return activation.sigmoid(a2)


def output_layer(z2):
    """出力層"""
    w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    b3 = np.array([0.1, 0.2])
    a3 = np.dot(z2, w3) + b3
    return activation.identity(a3)


def forward(x):
    """
    ネットワークの入力方向から出力方向への伝達を行う
    :param x: 入力値
    :return: 出力値
    """
    z1 = layer1(x)
    z2 = layer2(z1)
    return output_layer(z2)


def main():
    x = np.array([1.0, 0.5])
    y = forward(x)
    assertion.equal(y.tolist(), [0.3168270764110298, 0.6962790898619668])


if __name__ == '__main__':
    main()
