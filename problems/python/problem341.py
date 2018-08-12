# Leetcode's problem formulation here is a bit unpythonic. But here's how you'd do this in python (no hasNext)

def nested_iter(li):
    for item in li:
        if isinstance(item, list):
            yield from nested_iter(item)
        else:
            yield item

if __name__ == "__main__":
    li = [[1,1],2,[1,1]]
    x = nested_iter(li)
    for item in x:
        print(item)

    print("NEXT.")
    li = [1,[4,[6]]]
    x = nested_iter(li)
    for item in x:
        print(item)
