"""
活性化関数
"""

import numpy as np
import assertion
from typing import TypeVar

Numbers = TypeVar('Numbers', int, float, np.ndarray)


def step(x: np.ndarray) -> np.ndarray:
    """
    ステップ関数
    x が 0 以上なら 1 、そうでなければ 0 を返す
    """
    y = x > 0  # np.array を不等号で演算すると条件に一致しているかどうかの boolean を持った np.array を返す
    return y.astype(np.int)  # boolean は int に変換すると True -> 1, False -> 0


def sigmoid(x: np.ndarray) -> np.ndarray:
    """
    シグモイド関数
    x の値に応じて 0 から 1 までの値を返す
    """
    activated: np.ndarray = 1 / (1 + np.exp(-x))  # np のブロードキャストを用いて全体を演算している
    return activated


def ReLU(x: np.ndarray) -> np.ndarray:
    """
    ReLU関数
    x が 0 以上ならそのままの値を返す。0 未満なら 0 を返す
    """
    return np.maximum(0, x)


def identity(x: Numbers) -> Numbers:
    """
    恒等関数

    入力をそのまま出力する
    主に出力層で使用される
    """
    return x


def soft_max(x: np.ndarray) -> np.ndarray:
    """
    ソフトマックス関数

    複数ある出力層のうち、 いずれかひとつの出力層の出力を取得する
    戻り値の合計は必ず 1 になる特徴をもつ
    主に出力層で使用される
    """
    # exp は指数関数のため容易に大きな数値となりうる
    # オーバーフロー対策として引数のうち最大値を引いておく
    # これによる影響は出ない
    exp_x = np.exp(x - np.max(x))
    return exp_x / np.sum(exp_x)


def _main():
    import matplotlib.pyplot as pl

    x = np.arange(-5, 5, 0.1)

    pl.plot(x, step(x), label='step')
    pl.plot(x, sigmoid(x), label='sigmoid', linestyle='--')
    pl.plot(x, ReLU(x), label='ReLU', linestyle='-.')
    pl.ylim(-0.1, 1.1)  # y 軸の範囲を指定
    pl.legend()
    pl.show()


def _test_identify():
    x = 1.0
    assertion.equal(identity(x), x)


def _test_soft_max():
    yk = soft_max(np.array([100, 60, 1000]))
    assertion.equal(np.sum(yk), 1.0)


if __name__ == '__main__':
    _main()
    # TODO テストを切り出したい
    _test_identify()
    _test_soft_max()
