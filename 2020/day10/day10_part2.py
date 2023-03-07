from functools import cache


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]


def answer2(data: list[int], start: int = 0) -> int:
    adapters = data[:]
    adapters.append(0)
    adapters = sorted(adapters)
    adapters.append(adapters[-1] + 3)

    @cache
    def dp(i: int) -> int:
        if len(adapters) - 1 == i:
            return 1
        ans = 0
        for j in range(i + 1, len(adapters)):
            if adapters[j] - adapters[i] <= 3:
                ans += dp(j)
        return ans

    return dp(start)


def main() -> None:
    data = get_data("day10_input")
    ans2 = answer2(data)
    print(ans2)


if __name__ == "__main__":
    main()
