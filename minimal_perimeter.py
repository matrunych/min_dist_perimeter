import math

def minimal_perimeter(points):
    points_set  = set(points)
    points_new = list(points_set)
    points_x = sorted(points_new, key=lambda x: x[0])
    points_y = sorted(points_new, key=lambda x: x[1])

    per, p1, p2, p3 = _minimal_perimeter(points_x, points_y)

    return per, p1, p2, p3

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def _minimal_perimeter(points_x, points_y):
    n = len(points_x)

    if n <= 4:
        return brute_force_perimeter(points_x)

    middle = n // 2
    left_X = points_x[:middle]
    right_X = points_x[middle:]
    left_Y, right_Y = [], []
    middle_X = points_x[middle][0]


    for point in points_y:
        if point[0] <= middle_X:
            left_Y.append(point)
        else:
            right_Y.append(point)


    left_per, leftX_p1, leftX_p2, leftX_p3 = _minimal_perimeter(left_X, left_Y)

    right_per, rightX_p1, rightX_p2, rightX_p3 = _minimal_perimeter(right_X, right_Y)

    min_per, min_p1, min_p2, min_p3 = (left_per, leftX_p1, leftX_p2, leftX_p3)\
        if left_per <= right_per else(right_per, rightX_p1, rightX_p2, rightX_p3)

    closest_Y = [x for x in points_y if
                 abs(x[0] - middle_X) <= min_per]

    len_y = len(closest_Y)
    # if len_y > 2:
    #     for i in range(len_y - 1):
    #         for j in range(i + 1, min(i + 7, len_y)):
    #             for k in range(j + 1, min(j + 7, len_y)):
    #                 p1 = closest_Y[i]
    #                 p2 = closest_Y[j]
    #                 p3 = closest_Y[k]
    #                 temp_per = distance(p1, p2) + distance(p1, p3) + distance(p2, p3)
    #                 if temp_per < min_per:
    #                     min_p1 = p1
    #                     min_p2 = p2
    #                     min_p3 = p3
    #                     min_per = temp_per

    if len_y > 2:
        for i in range(len_y):
            for j in range(1, 8):
                for k in range(1, 8):
                    if i + k + j >= len_y:
                        break

                    p1 = closest_Y[i]
                    p2 = closest_Y[i+j]
                    p3 = closest_Y[i+j+k]
                    temp_per = distance(p1, p2) + distance(p1, p3) + distance(p2, p3)
                    if temp_per < min_per:
                        min_p1 = p1
                        min_p2 = p2
                        min_p3 = p3
                        min_per = temp_per

    return min_per, min_p1, min_p2, min_p3


def brute_force_perimeter(points_x):
    n = len(points_x)


    perimeter = math.inf

    point1 = 0
    point2 = 0
    point3 = 0

    if n == 3:
        point1, point2, point3 = points_x[0], points_x[1], points_x[2]
        perimeter = distance(point1, point2) + distance(point1, point3) + distance(point2, point3)

        return perimeter, point1, point2, point3

    for i in range(n - 2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                temp_perimeter = distance(points_x[i], points_x[j])\
                                + distance(points_x[i], points_x[k]) +\
                                 distance(points_x[j], points_x[k])

                if temp_perimeter < perimeter:
                    perimeter = temp_perimeter
                    point1 = points_x[i]
                    point2 = points_x[j]
                    point3 = points_x[k]

    return perimeter, point1, point2, point3

arr = [(447, 323), (781, 905), (40, 510), (952, 246), (409, 123), (913, 668), (203, 705), (504, 546), (752, 56), (557, 410), (181, 171), (849, 280), (97, 56), (10, 725), (608, 990), (107, 86), (642, 738), (448, 389), (241, 287), (808, 821), (979, 589), (729, 693), (695, 820), (341, 483), (69, 801), (500, 203), (545, 748), (592, 628), (56, 4), (743, 309), (959, 268), (3, 830), (300, 691), (626, 472), (827, 429), (786, 372), (170, 543), (98, 782), (383, 518), (510, 110), (543, 140), (801, 422), (16, 176), (958, 501), (280, 20), (685, 392), (469, 256), (26, 641), (62, 738), (265, 217), (349, 311), (181, 986), (409, 726), (151, 798), (888, 386), (631, 971), (176, 939), (226, 926), (480, 817), (415, 249), (971, 338), (250, 799), (917, 73), (243, 514), (892, 511), (994, 55), (962, 682), (802, 197), (916, 282), (333, 965), (513, 127), (82, 744), (678, 412), (595, 877), (828, 476), (855, 315), (294, 388), (32, 604), (264, 267), (995, 532), (71, 144), (75, 787), (529, 376), (48, 454), (466, 500), (439, 271), (937, 86), (46, 360), (435, 41), (708, 710), (638, 171), (508, 85), (359, 679), (709, 890), (736, 706), (491, 333), (414, 972), (492, 699), (810, 636), (325, 719)]


# arr = [(82, 66),(41, 25), (33, 62), (98, 19), (41, 25), (92, 94), (17, 29), (78, 30), (25, 92), (19, 82), (42, 31)]
print(minimal_perimeter(arr))