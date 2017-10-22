def isort(ls):
    for index in range(1, len(ls)):
        list_len = ls[index]
        pos = index
        # while pos > 0 and ls[pos-1] > list_len:
            # ls[pos] =