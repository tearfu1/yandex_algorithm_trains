def bigger_than_neighbours(numbers):
    ans = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i - 1] < numbers[i] > numbers[i + 1]:
            ans += 1
    return ans


def main():
    nums = list(map(int, input().split()))
    if len(nums) > 2:
        print(bigger_than_neighbours(nums))
    else:
        print(0)

main()