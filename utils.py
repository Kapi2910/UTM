def getBlockSize(window_dim, n, multiplier):
        return int(window_dim/ (n * multiplier))

def blockPositiontoGridIndex(x, y, scale_factor):
    i, j = ( int(x * scale_factor), int(y * scale_factor))
    return (i, j)
    
def polToCart(vector):
    (angle,z) = vector
    (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
    return (dx, dy)