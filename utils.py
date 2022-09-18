def getBlockSize(window_dim, n, multiplier):
        return int(window_dim/ (n * multiplier))

def polToCart(vector):
    (angle,z) = vector
    (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
    return (dx, dy)