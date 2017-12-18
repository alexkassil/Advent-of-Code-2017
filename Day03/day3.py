def find_ring(num):
    ring = 1
    largest = 1
    while num > largest:
        ring += 2
        largest = ring ** 2
        #print(largest)
    return ring

def location(num):
    ring = find_ring(num)
    ring_values = list(range((ring - 2) ** 2 + 1, ring ** 2 + 1))
#    print(ring_values)
    return ring_values

def mid(num):
    ring_values = location(num)
    mid_val = ring_values[len(location(num))//2-1]
    return mid_val

