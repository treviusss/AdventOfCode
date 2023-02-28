from collections import Counter


def get_data(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [line.strip().split("\n") for line in f.read().split("\n\n")]


def question_counter(data: list) -> int:
    yes_answers = 0

    for group in data:
        counter = Counter()
        for person in group:
            for answer in person:
                counter.update(answer)
        for value in counter.values():
            if value == len(group):
                yes_answers += 1

    return yes_answers


def main() -> None:
    data = get_data("day6_input")
    print(question_counter(data))


if __name__ == "__main__":
    main()
