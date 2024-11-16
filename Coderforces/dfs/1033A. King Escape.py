n = int(input())
a, b = list(map(int, str(input()).split(' ')))
c, d = list(map(int, str(input()).split(' ')))
tx, ty = list(map(int, str(input()).split(' ')))


def get_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0  # 源点或坐标在轴线上


def is_same_quadrant(a, b, c1, c2):
    x1, y1 = c1[0] - a, c1[1] - b
    x2, y2 = c2[0] - a, c2[1] - b

    quadrant1 = get_quadrant(x1, y1)
    quadrant2 = get_quadrant(x2, y2)

    return quadrant1 == quadrant2


# 示例用法
c1 = (c, d)  # 坐标1
c2 = (tx, ty)  # 坐标2

print("YES" if is_same_quadrant(a, b, c1, c2) else "NO")  # 输出: True



