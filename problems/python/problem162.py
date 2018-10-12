def find_peak(li, offset):
    if not li:
        return None
    if len(li) <= 3:
        max_val = max(li)
        ind = li.index(max_val)
        return ind + offset


    mid_ind = len(li)//2
    if li[mid_ind-1] < li[mid_ind] < li[mid_ind+1]:
        return find_peak(li[mid_ind+1:], offset=offset+mid_ind+1)
    elif li[mid_ind-1] > li[mid_ind] > li[mid_ind+1]:
        return find_peak(li[:mid_ind], offset=offset)
    elif li[mid_ind-1] < li[mid_ind] > li[mid_ind+1]:
        return mid_ind + offset
    else:
        return find_peak(li[mid_ind+1:], offset=offset+mid_ind+1)
    
if __name__ == "__main__":
    print(find_peak([1,2,3,1], 0))
    print(find_peak([1,2,1,3,5,6,4], 0))
    print(find_peak([2,1], 0))
    print(find_peak([1,2,3,4], 0))
    print(find_peak([1,3,2,1],0))
