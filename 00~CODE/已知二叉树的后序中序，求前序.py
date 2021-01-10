后序序列 = 'ABCDEFG'
中序序列 = 'BDCAFGE'


# 前序是 根 - 左 - 右
def 已知中序后序求前序(中序, 后序):

    if len(后序) == 0:
        return []

    根 = 后序[-1]  # 拿到后序的最后一个元素，即 根
    # 在中序定位位置
    root_index = 中序.index(根)
    左边的中序 = 中序[:root_index]
    右边的中序 = 中序[root_index + 1:]
    左边的后序 = 后序[:len(左边的中序)]
    右边的后序 = 后序[len(左边的中序):-1]

    左边的前序 = 已知中序后序求前序(左边的中序, 左边的后序)
    右边的前序 = 已知中序后序求前序(右边的中序, 右边的后序)

    return [根] + 左边的前序 + 右边的前序


前序序列 = 已知中序后序求前序(后序序列, 中序序列)
print(前序序列)
