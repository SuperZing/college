# Define your method here
def main():
    try:
        steps = int(input())
        print(f'{step_to_miles(steps):.2f}')

    except ValueError as excpt:
        print(excpt)


def step_to_miles(steps):
    if steps < 0:
        raise ValueError('Exception: Negative step count entered.')
    
    return steps/2000


if __name__ == '__main__':

    # Type your code here.
    main()
