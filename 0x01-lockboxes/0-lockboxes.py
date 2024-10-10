#!/usr/bin/python3
"""
A project that determines if all boxes are opened.
"""


def canUnlockAll(boxes):
    """
    Determines wheather series of boxes can be opened.
    """

    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for k in range(1, len(boxes)):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
