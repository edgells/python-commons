import cProfile
import time

profiler = cProfile.Profile()


@profiler.runcall
def main():
    time.sleep(5)
    print("main method running")


profiler.print_stats()
