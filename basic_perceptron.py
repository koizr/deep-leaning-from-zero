"""
2.3 パーセプトロンの実装
"""

import numpy as np
import assertion


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    return activate(b, w, x)


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.4

    return activate(b, w, x)


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    return activate(b, w, x)


def XOR(x1, x2):
    """
    パーセプトロンは線形に出力を決定するので単層では実装できない
    しかし、複数の層を組み合わせることで実装できる
    """

    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)


def activate(b, w, x):
    """
    活性化関数
    受け取った値によって出力を発火させる
    """

    weighted_biased = np.sum(x * w) + b
    return step(weighted_biased)


def step(x):
    """
    ステップ関数
    活性化関数の実装のうちのひとつ
    """
    return 1 if x > 0 else 0


if __name__ == '__main__':
    print("AND")
    assertion.equal(AND(0, 0), 0)
    assertion.equal(AND(1, 0), 0)
    assertion.equal(AND(0, 1), 0)
    assertion.equal(AND(1, 1), 1)

    print("OR")
    assertion.equal(OR(0, 0), 0)
    assertion.equal(OR(1, 0), 1)
    assertion.equal(OR(0, 1), 1)
    assertion.equal(OR(1, 1), 1)

    print("NAND")
    assertion.equal(NAND(0, 0), 1)
    assertion.equal(NAND(1, 0), 1)
    assertion.equal(NAND(0, 1), 1)
    assertion.equal(NAND(1, 1), 0)

    print("XOR")
    assertion.equal(XOR(0, 0), 0)
    assertion.equal(XOR(1, 0), 1)
    assertion.equal(XOR(0, 1), 1)
    assertion.equal(XOR(1, 1), 0)
