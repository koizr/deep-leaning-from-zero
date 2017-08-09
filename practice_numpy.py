import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([10, 20, 30])

    # 2 つの配列の要素をそれぞれ計算する
    # 同じ要素数でないとエラーになる
    print(a + b)
    print(a / b)

    # スカラ値との演算をすると、要素全体に演算する
    # この機能をブロードキャストという
    print(a * 5)

    # 多次元配列を扱うことも可能
    d = np.array([[1, 2], [3, 4]])
    print(d)
    print(d.shape) # 行列の形状を表示する
    print(d.dtype) # 値の種類を表示する

    # 行列でも1次元の場合と同じように計算できる
    # .shape の結果が異なっていたらエラー
    print(d + 100)
    print(d * np.array([[0., 0.2], [0.3, 0.4]]))

    x = np.array([[51, 55], [14, 19], [0, 9]])

    # 要素へのアクセスは通常の配列と同じようにできる
    print(x[0][1])
    print([item for item in x])

    # 要素をフラットにする
    print(x.flatten())

    # d から index が 1, 0, 0 の要素を取得し配列にする
    print(x[np.array([1, 0, 0])])

    # 要素ごとに条件に一致するか判定する
    print(x.flatten() > 15)

    # 条件に一致する要素だけ取得する（1次元配列になる）
    print(x[x > 15])
