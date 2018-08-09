import bisect
def get_kth_largest(l, k):
    if k > len(l)/2:
        return _get_kth_smallest(l, len(l) - k + 1)
    else:
        return _get_kth_largest(l, k)

def _get_kth(l, k, cmp_func, reverse):
    k_list = sorted(l[:k], reverse=reverse)
    for cur_elt in l[k:]:
        if cmp_func(cur_elt, k_list[-1]):
            k_list.pop()
            k_list = bin_insert(cur_elt, k_list, reverse)
    return k_list[-1]

def bin_insert(elt, k_list, reverse):
    if reverse:
        k_list = k_list[::-1]
    ind = bisect.bisect_left(k_list, elt)
    result = k_list[:ind] + [elt] + k_list[ind:]
    if reverse:
        result = result[::-1]
    return result

def _get_kth_smallest(l, k):
    return _get_kth(l, k, lambda x,y: x < y, reverse=False)

def _get_kth_largest(l, k):
    return _get_kth(l, k, lambda x,y: x > y, reverse=True)


if __name__ == "__main__":
    test = [3,2,1,5,6,4]
    k = 2
    print(get_kth_largest(test, k))

    test = [3, 7, 9, 0, 2, 1, 4, 6, 5, 8]
    k = 7
    print(get_kth_largest(test, k))
