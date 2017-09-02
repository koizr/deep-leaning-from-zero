"""
アサーション
テストで使用する比較関数群
"""


def equal(actual, expected):
    """actual が expected と同値であるかどうかを標準出力する"""
    result = 'success' if actual == expected else 'failed'
    print(f"{result}: {actual} = {expected}")
