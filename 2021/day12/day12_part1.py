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

    def dfs(self, start, end, path):
        paths = []

        def inner_dfs(start, end, path):
            path = path + [start]
            if start == end:
                paths.append(path)
            for node in self.graph[start]:
                if node not in path or node.isupper():
                    inner_dfs(node, end, path)

        inner_dfs(start, end, path)
        return paths

    def dfs_iter(self):
        start = ("start", set(["start"]))
        ans = 0
        Q = [start]
        while Q:
            pos, small = Q.pop()
            if pos == "end":
                ans += 1
                continue
            for y in self.graph[pos]:
                if y not in small:
                    new_small = set(small)
                    if y.lower() == y:
                        new_small.add(y)
                    Q.append((y, new_small))

        return ans


def main():
    data = get_data("day12_input")
    graph = Graph(data)
    print(graph.dfs("start", "end", []).__len__())
    print(graph.dfs_iter())


if __name__ == "__main__":
    main()
