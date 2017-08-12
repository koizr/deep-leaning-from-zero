"""
2.3 パーセプトロンの実装
"""


def AND(x1, x2):
    w1 = 0.5
    w2 = 0.5
    theta = 0.7

    weighted = x1 * w1 + x2 * w2
    return 1 if weighted > theta else 0


def OR(x1, x2):
    w1 = 0.5
    w2 = 0.5
    theta = 0.4

    weighted = x1 * w1 + x2 * w2
    return 1 if weighted > theta else 0


def NAND(x1, x2):
    w1 = -0.5
    w2 = -0.5
    theta = -0.7

    weighted = x1 * w1 + x2 * w2
    return 1 if weighted > theta else 0


def assert_equal(actual, expected):
    result = 'success' if actual == expected else 'failed'
    print(f"{result}: {actual} = {expected}")


if __name__ == '__main__':
    print("AND")
    assert_equal(AND(0, 0), 0)
    assert_equal(AND(1, 0), 0)
    assert_equal(AND(0, 1), 0)
    assert_equal(AND(1, 1), 1)

    print("OR")
    assert_equal(OR(0, 0), 0)
    assert_equal(OR(1, 0), 1)
    assert_equal(OR(0, 1), 1)
    assert_equal(OR(1, 1), 1)

    print("NAND")
    assert_equal(NAND(0, 0), 0)  # 今の方式では実装できない
    assert_equal(NAND(1, 0), 1)
    assert_equal(NAND(0, 1), 1)
    assert_equal(NAND(1, 1), 0)
