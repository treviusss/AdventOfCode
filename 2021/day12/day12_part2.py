from collections import defaultdict


def get_data(filename: str) -> list:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


class Graph:
    def __init__(self, data) -> None:
        self.graph = self.parse_data(data)

    def parse_data(self, data: list):
        graph_dict = defaultdict(list)
        for line in data:
            start, end = line.split("-")
            graph_dict[start].append(end)
            graph_dict[end].append(start)
        return graph_dict

    def dfs(self, node, visited=set(), doubled=False):
        if node == "end":
            return 1
        total = 0
        for next in self.graph[node]:
            if next == "start":
                continue
            if next in visited and doubled:
                continue
            if next in visited:
                total += self.dfs(
                    next,
                    visited | {node} if node == node.lower() else visited,
                    True,
                )
            else:
                total += self.dfs(
                    next,
                    visited | {node} if node == node.lower() else visited,
                    doubled,
                )
        return total

    def dfs_iter(self):
        start = ("start", set(["start"]), False)
        ans = 0
        Q = [start]
        while Q:
            pos, small, double = Q.pop()
            if pos == "end":
                ans += 1
                continue
            for y in self.graph[pos]:
                if y not in small:
                    new_small = set(small)
                    if y.lower() == y:
                        new_small.add(y)
                    Q.append((y, new_small, double))
                elif y in small and not double and y not in ["start", "end"]:
                    Q.append((y, small, y))

        return ans


def main():
    data = get_data("day12_input")
    graph = Graph(data)
    print(graph.dfs("start"))
    print(graph.dfs_iter())


if __name__ == "__main__":
    main()
