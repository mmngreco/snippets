import time


def timeit(n, func, *args, verbose=True):
    out = []

    for i in range(n):

        tic = time.time()
        func(*args)
        toc = time.time()

        tdelta = toc - tic
        out.append(tdelta)

    mean = stats.mean(out)
    std = stats.stdev(out)

    if verbose:
        print(f"{func.__name__} : {mean:.4f} ({std:.4f})")

    return mean, std
