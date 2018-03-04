#!/usr/bin/env python
# -*- coding:utf-8   -*-


input1 = [
        [0, 4, 0, 0, 0, 7, 1, 0, 0],
        [5, 3, 0, 0, 9, 0, 0, 7, 0],
        [0, 0, 7, 0, 6, 0, 9, 4, 0],
        [4, 0, 6, 0, 8, 0, 7, 5, 1],
        [0, 1, 0, 0, 0, 0, 6, 9, 0],
        [0, 5, 3, 0, 1, 0, 0, 0, 2],
        [9, 6, 0, 0, 3, 0, 0, 1, 0],
        [3, 7, 0, 0, 5, 1, 0, 0, 0],
        [1, 0, 0, 2, 0, 9, 3, 6, 7]
]

input2 = [
    [0, 0, 8, 2, 0, 0, 9, 0, 3],
    [3, 4, 2, 0, 9, 5, 0, 0, 7],
    [1, 9, 7, 0, 0, 0, 0, 0, 4],
    [0, 0, 5, 3, 1, 2, 4, 7, 9],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 7, 4, 5, 0, 0],
    [0, 2, 0, 0, 0, 1, 0, 0, 5],
    [0, 7, 0, 0, 0, 6, 8, 9, 1],
    [8, 0, 0, 4, 3, 0, 7, 0, 6]
]


input11 = [
    [6, 0, 0, 4, 0, 0, 0, 0, 0],
    [9, 4, 3, 8, 0, 5, 7, 0, 6],
    [0, 0, 0, 0, 0, 2, 0, 4, 0],
    [0, 0, 0, 6, 0, 8, 0, 7, 9],
    [0, 9, 5, 0, 0, 0, 1, 6, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 8],
    [7, 0, 0, 0, 8, 0, 0, 1, 3],
    [0, 0, 6, 0, 0, 9, 0, 0, 0],
    [0, 1, 0, 3, 0, 4, 0, 0, 0]
]

input12 = [
    [9, 0, 2, 3, 0, 0, 8, 0, 1],
    [0, 1, 5, 0, 0, 0, 3, 0, 0],
    [4, 0, 7, 0, 0, 0, 0, 5, 6],
    [0, 0, 8, 0, 0, 7, 1, 0, 2],
    [0, 0, 0, 0, 2, 6, 5, 9, 0],
    [0, 0, 0, 5, 8, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 6, 0, 0, 0, 0, 5],
    [0, 7, 9, 2, 0, 5, 0, 0, 0]
]


input21 = [
    [0, 0, 0, 0, 0, 5, 0, 7, 0],
    [1, 0, 0, 0, 0, 0, 0, 4, 9],
    [5, 7, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 6, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 2, 3, 0, 6],
    [9, 0, 0, 5, 0, 7, 0, 0, 0],
    [7, 0, 0, 0, 0, 9, 0, 0, 5],
    [0, 9, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 2, 8]
]


input31 = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 0, 0, 0, 2],
    [0, 7, 0, 9, 0, 0, 5, 1, 0],
    [0, 2, 0, 0, 0, 9, 0, 0, 0],
    [0, 3, 1, 0, 0, 0, 0, 4, 0],
    [0, 0, 9, 8, 0, 0, 0, 7, 0],
    [4, 0, 0, 0, 5, 0, 0, 0, 3],
    [0, 0, 8, 0, 0, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 6, 9]
]

input32 = [
    [0, 0, 0, 0, 0, 0, 3, 4, 0],
    [0, 0, 9, 0, 0, 5, 0, 0, 6],
    [2, 5, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 2, 0, 0, 0, 0, 7, 0],
    [5, 0, 0, 4, 0, 3, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 0, 0, 1, 9, 0, 0, 4],
    [0, 0, 0, 0, 0, 6, 0, 0, 3],
    [0, 0, 0, 2, 0, 0, 0, 8, 0]
]


def output(data):
    for i in range(9):
        l = data[i]
        for j in range(9):
            ll = l[j]
            if ll == 0:
                print '   ',
            else:
                print ' %d ' %(ll),

            if j == 2 or j == 5 or j == 8:
                print '||',

        print ''

        if i == 2 or i == 5:
            print("========================================")
        else:
            print("-----------------------------------------")


def is_conflict(data, num, x_axis, y_axis):
    assert(x_axis >= 0 and x_axis < 9)
    assert(y_axis >= 0 and y_axis < 9)
    assert(num >= 0 and num <= 9)

    if num in data[x_axis]:
        return True

    for x in range(9):
        if num == data[x][y_axis]:
            return True
    
    x1 = (x_axis / 3) * 3
    x2 = (x_axis / 3) * 3 + 3
    y1 = (y_axis / 3) * 3
    y2 = (y_axis / 3) * 3 + 3

    for x in range(x1, x2):
        for y in range(y1, y2):
            if data[x][y] == num:
                return True
    
    return False

def itor1(data):
    count = 0

    # Find by  line
    for x in range(9):
        for num in range(1, 10):
            selects = 0
            dst_x = x
            dst_y = -1
            for y in range(9):
                if data[x][y] != 0:
                    continue
                
                if not is_conflict(data, num, x, y):
                    selects = selects + 1
                    dst_x = x
                    dst_y = y

            if selects == 1:
                data[dst_x][dst_y] = num
                count = count + 1
                #print "xx set (%d, %d) ==>> %d " %(dst_x+1, dst_y+1, num)

    # Find by column
    for y in range(9):
        for num in range(1, 10):
            selects = 0
            dst_x = -1
            dst_y = y

            for x in range(9):
                if data[x][y] != 0:
                    continue
                
                if not is_conflict(data, num, x, y):
                    selects = selects + 1
                    dst_x = x
                    dst_y = y
                
            if selects == 1:
                data[dst_x][dst_y] = num
                count = count + 1
                #print "yy set (%d, %d) ==>> %d " %(dst_x+1, dst_y+1, num)

    # find in the small block
    for i in range(3):
        for j in range(3):
            for num in range(1, 10):
                selects = 0
                for x in range(i * 3, (i + 1) * 3):
                    for y in range(j * 3, (j + 1) * 3):
                        if data[x][y] != 0:
                            continue
                        
                        if not is_conflict(data, num, x, y):
                            selects = selects + 1
                            dst_x = x
                            dst_y = y

                if selects == 1:
                    data[dst_x][dst_y] = num
                    count = count + 1
                    #print "xy set (%d, %d) ==>> %d " %(dst_x+1, dst_y+1, num)
    
    return count


def traverse(data, x_axis, y_axis):
    if x_axis == 9:
        return True

    x_next = x_axis
    y_next = y_axis
    if y_axis < 8:
        y_next = y_axis + 1
    else:
        x_next = x_axis + 1
        y_next = 0

    if data[x_axis][y_axis] != 0:
        return traverse(data, x_next, y_next)

    dst_num = 0
    dst_count = 0
    for num in range(1, 10):
        data[x_axis][y_axis] = 0
        if is_conflict(data, num, x_axis, y_axis):
            continue

        data[x_axis][y_axis] = num
        if traverse(data, x_next, y_next):
            dst_num = num
            dst_count = dst_count + 1
            break
        else:
            data[x_axis][y_axis] = 0
        
    assert(dst_count == 0 or dst_count == 1)
    if dst_count == 0:
        return False
    
    data[x_axis][y_axis] = dst_num    
    return True


def finished(data):
    count = 0
    for x in range(9):
        for y in range(9):
            if data[x][y] == 0:
                count = count + 1

    return count

if __name__ == '__main__':
    input = input32
    
    print("Sudoku:")
    output(input)

    while True:
        count = itor1(input)
        if count == 0:
            break
        
    # Traverse all the solution space
    traverse(input, 0, 0)

    last = finished(input)
    if last == 0:
        print("Done")
    else:
        print("Failed, ", last, " empty block least")
    
    print("Result:")
    output(input)
    
