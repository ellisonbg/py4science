import pool
import randmat
import multiprocessing


if __name__ == '__main__':
    pp = pool.SimpleThreadPool(2)
    result = pp.map(randmat.eigvals_from_dim, 4*[500])
