"""
活性化関数

引数に np.array が来ても正しく動作するように作る
"""

import numpy as np
import matplotlib.pyplot as pl


def step(x):
    """ステップ関数"""
    y = x > 0  # np.array を不等号で演算すると条件に一致しているかどうかの boolean を持った np.array を返す
    return y.astype(np.int)  # boolean は int に変換すると True -> 1, False -> 0


def sigmoid(x):
    """シグモイド関数"""
    return 1 / (1 + np.exp(-x))  # np のブロードキャストを用いて全体を演算している


def ReLU(x):
    """ReLU関数: x が 0 以上ならそのままの値を返す。0 未満なら 0 を返す"""
    return np.maximum(0, x)


if __name__ == '__main__':
    x = np.arange(-5, 5, 0.1)

    pl.plot(x, step(x), label='step')
    pl.plot(x, sigmoid(x), label='sigmoid', linestyle='--')
    pl.plot(x, ReLU(x), label='ReLU', linestyle='-.')
    pl.ylim(-0.1, 1.1)  # y 軸の範囲を指定
    pl.legend()
    pl.show()
