import cProfile
import profile


@profile.run
def make():
    print("hello world")


if __name__ == '__main__':
    make()
