import heapq
import timeit

DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class PriorityQueue:
    def __init__(self) -> None:
        self.heap = []

    def heappush(self, value):
        self.heap.append(value)
        idx = len(self.heap) - 1
        parent = (idx - 1) // 2

        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def heappop(self):
        if not self.heap:
            raise IndexError
        if len(self.heap) == 1:
            return self.heap.pop()
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]  # swapping
        value = self.heap.pop()
        idx = 0

        while (
            idx * 2 + 1 < len(self.heap) and self.heap[idx * 2 + 1] < self.heap[idx]
        ) or (idx * 2 + 2 < len(self.heap) and self.heap[idx * 2 + 2] < self.heap[idx]):
            if (
                idx * 2 + 2 >= len(self.heap)
                or self.heap[idx * 2 + 1] < self.heap[idx * 2 + 2]
            ):
                self.heap[idx], self.heap[idx * 2 + 1] = (
                    self.heap[idx * 2 + 1],
                    self.heap[idx],
                )  # swapping
                idx = idx * 2 + 1
            else:
                self.heap[idx], self.heap[idx * 2 + 2] = (
                    self.heap[idx * 2 + 2],
                    self.heap[idx],
                )  # swapping
                idx = idx * 2 + 2

        return value

    def __str__(self) -> str:
        return f"{self.heap}"

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        end = len(self.heap)

        if end > self.start:
            result = self.heap[self.start]
            self.start += 1
            return result
        else:
            raise StopIteration


def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return [[int(num) for num in line.strip()] for line in f]


def enlarge_data(data: list, times=5) -> list[list[int]]:
    grid = [[0] * times * len(data) for _ in range(len(data * times))]
    for i in range(len(data) * times):
        for j in range(len(data) * times):
            grid[i][j] = (
                data[i % len(data)][j % len(data)]
                + (i // len(data))
                + (j // len(data))
                - 1
            ) % 9 + 1
    return grid


def dijkstra_builtin(graph: list):
    priority_queue = [(0, 0, 0)]
    visited = set()

    while priority_queue:
        cost, x, y = heapq.heappop(priority_queue)
        if x == y == len(graph) - 1:
            return cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in DIR:
            new_x = x + dx
            new_y = y + dy
            if (
                0 <= new_x and new_x < len(graph) and 0 <= new_y and new_y < len(graph)
            ) and (new_x, new_y) not in visited:
                heapq.heappush(
                    priority_queue, (cost + graph[new_x][new_y], new_x, new_y)
                )
    return -1


def dijkstra_impl(graph: list):
    priority_queue = PriorityQueue()
    priority_queue.heappush([0, 0, 0])
    visited = set()

    while priority_queue:
        cost, x, y = priority_queue.heappop()
        if x == y == len(graph) - 1:
            return cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in DIR:
            new_x = x + dx
            new_y = y + dy
            if (
                0 <= new_x and new_x < len(graph) and 0 <= new_y and new_y < len(graph)
            ) and (new_x, new_y) not in visited:
                priority_queue.heappush((cost + graph[new_x][new_y], new_x, new_y))
    return -1


def parse_data() -> list[list[int]]:
    data = get_data("day15_input")
    data = enlarge_data(data)
    return data


def main():
    data = parse_data()
    builtin_heapq = dijkstra_builtin(data)
    impl_heapq = dijkstra_impl(data)
    assert builtin_heapq == impl_heapq
    print(impl_heapq)

    # builtin_heapq_timer = timeit.Timer(
    #     "dijkstra_builtin(parse_data())",
    #     "from __main__ import dijkstra_builtin, parse_data",
    # )
    # impl_heapq_timer = timeit.Timer(
    #     "dijkstra_impl(parse_data())",
    #     "from __main__ import dijkstra_impl, parse_data",
    # )
    # print(builtin_heapq_timer.timeit(number=1)) # 0.8717341999290511
    # print(impl_heapq_timer.timeit(number=1)) # 4.007083100033924


if __name__ == "__main__":
    main()
