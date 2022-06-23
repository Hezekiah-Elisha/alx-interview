#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to
n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    @boxes is a lis of lists
    '''
    keys = [0]
    for n in keys:
        for key in boxes[n]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    return len(keys) == len(boxes)
