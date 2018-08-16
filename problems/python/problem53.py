# I thought wayyyy too hard about this one...

def longest_cons_sum(li):
    cur_max = running_total = li[0]
    for num in li[1:]:
        running_total = max(running_total + num, num)
        cur_max = max(running_total, cur_max)
    return cur_max
