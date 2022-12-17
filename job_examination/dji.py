radius, x_center, y_center, x1, y1, x2, y2 = list(map(int, input().split()))
x1, y1 = x1 - x_center, y1 - y_center
x2, y2 = x2 - x_center, y2 - y_center
print(radius, x_center, y_center, x1, y1, x2, y2)

if x1 * x2 < 0 and y1 * y2 < 0:
    # 矩形包含原点
    print(True)
else:
    x1, x2 = min(abs(x1), abs(x2)), max(abs(x1), abs(x2))
    y1, y2 = min(abs(y1), abs(y2)), max(abs(y1), abs(y2))
    if x1 ** 2 + y1 ** 2 <= radius ** 2:
        print(True)
    else:
        print(False)
