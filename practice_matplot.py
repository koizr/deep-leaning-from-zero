"""
1.6 Matplitlib
"""

import numpy as np
import matplotlib.pyplot as pl

if __name__ == '__main__':
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)

    # グラフの描画
    pl.plot(x, y)
    pl.show()

    y1 = np.sin(x)
    y2 = np.cos(x)

    pl.plot(x, y1, label='sin')
    pl.plot(x, y2, label='cos', linestyle='dashed')
    pl.xlabel('x')  # x軸のラベル
    pl.ylabel('y')  # y軸のラベル
    pl.title('sin & cos')  # 表のタイトル
    pl.legend()  # ラベルで指定した判例をグラグにプロット
    pl.show()

    # matplotlib.image モジュールでグラフに画像を表示することができる
