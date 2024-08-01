#!/usr/bin/python3
"""
0. Lockboxes mandatory file task 0
"""

def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    """
    n = len(boxes)
    unlocked = set()
    unlocked.add(0)
    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                stack.append(key)
    return len(unlocked) == n
