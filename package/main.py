from utilits.hello import hello, subtraction
from utilits.world import world, sum


def main():
    hello()
    world()
    print(subtraction(10, 3))
    print(sum(2, 3))


if __name__ == "__main__":
    main()
