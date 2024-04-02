# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def twoNumberSum(array, targetSum):
    for i in range(0, len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []

    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
