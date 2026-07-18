from random import randint


def movezeros(numbers):
    for num in numbers:
        if num == 0:
            numbers.remove(num)
            numbers.append(num)
    return numbers


def expected(numbers):
    non_zero = [x for x in numbers if x != 0]
    zeros = [0] * (len(numbers) - len(non_zero))
    return non_zero + zeros


for test in range(100_000_000):
    size = randint(0, 50)
    arr = [randint(0, 5) for _ in range(size)]

    your_output = movezeros(arr.copy())
    expected_output = expected(arr)

    if your_output != expected_output:
        print("FAILED")
        print("Test Number :", test)
        print("Input        :", arr)
        print("Your Output  :", your_output)
        print("Expected     :", expected_output)
        break
else:
    print("PASSED 100,000,000 RANDOM TESTS")