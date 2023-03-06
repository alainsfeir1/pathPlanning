class AStar:
    """
    Encapsulate the behaviour of AStar algorithm.

    Attributes
    ----------
    x: int
        x coordinate.
    y: int
        y coordinate.
    path: list
        Path of AStar algorithm.
    cost: int
        Cost of AStar algorithm.
    parent: AStar
        Parent node of AStar algorithm.
    heuristic: dict
        Heuristic of AStar algorithm.
    neighbors: list
        Neighbors of AStar algorithm.
    direction: list
        Direction of AStar algorithm.

    Methods
    -------
    get_heuristic(self)
        Get the heuristic of AStar algorithm.

    update_neighbors(self, grid)
        Update the neighbors of AStar algorithm.

    update_direction(self)
        Update the direction of AStar algorithm.

    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.path = []
        self.cost = 0
        self.parent = None
        self.heuristic = {'x': x1, 'y': y1}
        self.neighbors = []
        self.direction = []

    def get_heuristic(self) -> int:
        """
        Get the heuristic of AStar algorithm.

        Returns
        -------
        int
            Heuristic of AStar algorithm.


        """
        return abs(self.x - self.heuristic['x']) + abs(self.y - self.heuristic['y'])

    def update_neighbors(self, grid: list) -> None:
        """
        Update the neighbors of AStar algorithm.

        Parameters
        ----------
        grid: list
            List of AStar algorithm.

        Returns
        -------
        None


        """
        self.neighbors = []
        if self.x < len(grid) - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.y < len(grid[self.x]) - 1:
            self.neighbors.append(grid[self.x][self.y + 1])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])

    def update_direction(self) -> None:
        """
        Update the direction of AStar algorithm.

        Returns
        -------
        None


        """
        self.direction = []
        if self.parent.x < self.x:
            self.direction.append('left')
        if self.parent.x > self.x:
            self.direction.append('right')
        if self.parent.y < self.y:
            self.direction.append('up')
        if self.parent.y > self.y:
            self.direction.append('down')


def astar(grid: list, start: tuple, end: tuple) -> list:
    """
    AStar algorithm.

    Parameters
    ----------
    grid: list
        List of AStar algorithm.
    start: tuple
        Start tuple of AStar algorithm.
    end: tuple
        End tuple of AStar algorithm.

    Returns
    -------
    list
        Path of AStar algorithm.

    """
    start_node = grid[start[0]][start[1]]
    end_node = grid[end[0]][end[1]]
    open_set = set([start_node])
    closed_set = set([])
    while len(open_set) > 0:
        current = None
        for node in open_set:
            if current is None or node.cost + node.get_heuristic() < current.cost + current.get_heuristic():
                current = node
        if current == end_node:
            path = []
            while current.parent is not None:
                path.append(current.direction)
                current = current.parent
            return path[::-1]
        open_set.remove(current)
        closed_set.add(current)
        for neighbor in current.neighbors:
            if neighbor not in closed_set:
                if neighbor not in open_set:
                    open_set.add(neighbor)
                neighbor.cost = current.cost + 1
                neighbor.parent = current
                neighbor.update_direction()
    return None


def main() -> None:
    """
    Main function.

    Returns
    -------
    None


    """
    grid = [[AStar(x, y) for y in range(10)] for x in range(10)]
    for x, row in enumerate(grid):
        for y, node in enumerate(row):
            node.update_neighbors(grid)
    path = astar(grid, (0, 0), (9, 9))
    print(path)


if __name__ == '__main__':
    main()
