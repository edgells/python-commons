import cProfile
import tempfile
import os
import pstats
import time


def profile(column='time', list=5):
    def _profile(function):
        def __profile(*args, **kwargs):
            s = tempfile.mkdtemp()
            profiler = cProfile.Profile()
            profiler.runcall(function, *args, **kwargs)
            profiler.dump_stats(s)
            p = pstats.Stats(s)
            p.sort_stats(column).print_stats(list)

        return __profile

    return _profile


@profile('time', 6)
def main():
    time.sleep(5)
    print("main method running")


if __name__ == '__main__':
    main()