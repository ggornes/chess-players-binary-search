def bubble_sort(a):
    """
    Sorting algorithm of complexity O(n^2)
    :param a: a list
    :return: sorted list
    """
    n = len(a)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if a[j] < [j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                already_sorted = False
        if already_sorted:
            break
    return a


def insertion_sort(a):
    """
    Sorting algorithm of complexity O(n^2)
    :param a: a list
    :return: sorted list
    """
    n = len(a)
    for i in range(1, n):
        key_item = a[i]
        j = i - 1
        while j >= 0 and a[j] > key_item:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key_item
    return a