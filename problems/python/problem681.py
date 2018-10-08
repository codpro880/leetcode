import bisect
import itertools

def next_closest_time(time):
    if all_digits_same(time): 
        return time
    all_valid_times = gen_valid_times(time)
    sorted_times = sort_times(all_valid_times)
    t_str = "".join(time.split(":"))
    ind_to_insert = bisect.bisect(sorted_times, t_str)
    if len(sorted_times) == ind_to_insert:
        res_time = sorted_times[0]
    else:
        res_time = sorted_times[ind_to_insert]

    return res_time[0:2] + ":" + res_time[2:]

def all_digits_same(time):
    hour, minute = time.split(":")
    return hour[0] == hour[1] and hour[0] == minute[0] and hour[0] == minute[1]

def gen_valid_times(time):
    all_possible_times = gen_all_times(time)
    valid_times = remove_invalid_times(all_possible_times)
    return valid_times

def gen_all_times(time):
    hour, minute = time.split(":")
    dig1, dig2 = hour
    dig3, dig4 = minute
    digit_list = [dig1, dig2, dig3, dig4]
    perms = itertools.product(digit_list, repeat=4)
    perms = ["".join(perm) for perm in perms]
    perms = [perm for perm in perms if perm != hour + minute]
    return perms

def remove_invalid_times(all_possible_times):
    first_dig_set = set(["0", "1", "2"])
    second_dig_set = set(["0", "1", "2", "3", "4"])
    third_dig_set = set(["0", "1", "2", "3", "4", "5"])
    four_dig_set = set([str(x) for x in range(10)])

    res = []
    for t in all_possible_times:
        if t[0] == "2":
            if t[0] in first_dig_set and t[1] in second_dig_set and t[2] in third_dig_set and t[3] in four_dig_set:
                res.append(t)
            continue
        elif t[0] in first_dig_set and t[1] in four_dig_set and t[2] in third_dig_set and t[3] in four_dig_set:
            res.append(t)

    return res
    
def sort_times(all_valid_times):
    return sorted(all_valid_times)

if __name__ == "__main__":
    time = "23:59"
    print("22:22: ", next_closest_time(time))

    time = "00:00"
    print("00:00:", next_closest_time(time))

    time = "19:34"
    print("19:39: ", next_closest_time(time))
