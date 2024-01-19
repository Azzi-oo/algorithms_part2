def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    res = []
    for i in range(1, n+1):
        res.append(x*i)
    return res
