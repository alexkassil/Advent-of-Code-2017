def find_ring(num):
    "Find the ring that contains given number"
    ring = 1
    largest = 1
    while num > largest:
        ring += 2
        largest = ring ** 2
        #print(largest)
    return ring

def location(num):
    "Return all values association with the ring"
    ring = find_ring(num)
    ring_values = list(range((ring - 2) ** 2 + 1, ring ** 2 + 1))
    return ring_values

def mid(num):
    """Returns the 4 values appearing at the 
    NSEW position in the ring"""
    ring_values = location(num)
    mid_val = []
    length = len(ring_values)
    for i in range(1, 5):
        mid_val.append(ring_values[length//4*i-1-length//8])
    return mid_val

def dist_from_mid(num):
    "Returns the distance from NSEW value"
    dist = num**2
    mid_val = mid(num)
    for val in mid_val:
        dist = min(dist, abs(num-val))
    return dist

def dist(num):
    "Returns number of steps in shortest path"
    if num == 1:
        return 0
    return (find_ring(num) - 1)//2 + dist_from_mid(num)
