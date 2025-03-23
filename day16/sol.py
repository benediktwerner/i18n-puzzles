#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass
class Piece:
    char: str
    rotates_to: str
    right: int
    down: int
    left: int
    up: int
    fixed: bool = False

    def possible_connections(self, d: int) -> set[int]:
        if self.fixed:
            match d:
                case 0:
                    return {self.right}
                case 1:
                    return {self.down}
                case 2:
                    return {self.left}
                case 3:
                    return {self.up}
                case _:
                    assert False, f"invalid direction {d}"
        return {self.right, self.down, self.left, self.up}

    def possible_rotations(self, possible_connections: list[set[int]]) -> list[int]:
        result = []
        curr = self
        i = 0
        while i == 0 or curr.char != self.char:
            if (
                curr.right in possible_connections[0]
                and curr.down in possible_connections[1]
                and curr.left in possible_connections[2]
                and curr.up in possible_connections[3]
            ):
                result.append(i)
            curr = PIECES[curr.rotates_to]
            i += 1
        return result

    def rotate(self, n: int) -> Piece:
        result = self
        for _ in range(n):
            result = PIECES[result.rotates_to]
        return result


PIECES = {
    "┼": Piece("┼", "┼", 1, 1, 1, 1, True),
    "├": Piece("├", "┬", 1, 1, 0, 1),
    "┬": Piece("┬", "┤", 1, 1, 1, 0),
    "┤": Piece("┤", "┴", 0, 1, 1, 1),
    "┴": Piece("┴", "├", 1, 0, 1, 1),
    "│": Piece("│", "─", 0, 1, 0, 1),
    "─": Piece("─", "│", 1, 0, 1, 0),
    "┌": Piece("┌", "┐", 1, 1, 0, 0),
    "┐": Piece("┐", "┘", 0, 1, 1, 0),
    "┘": Piece("┘", "└", 0, 0, 1, 1),
    "└": Piece("└", "┌", 1, 0, 0, 1),
    " ": Piece(" ", " ", 0, 0, 0, 0, True),
    "╔": Piece("╔", "╗", 2, 2, 0, 0),
    "╗": Piece("╗", "╝", 0, 2, 2, 0),
    "╝": Piece("╝", "╚", 0, 0, 2, 2),
    "╚": Piece("╚", "╔", 2, 0, 0, 2),
    "═": Piece("═", "║", 2, 0, 2, 0),
    "║": Piece("║", "═", 0, 2, 0, 2),
    "╦": Piece("╦", "╣", 2, 2, 2, 0),
    "╣": Piece("╣", "╩", 0, 2, 2, 2),
    "╩": Piece("╩", "╠", 2, 0, 2, 2),
    "╠": Piece("╠", "╦", 2, 2, 0, 2),
    "╬": Piece("╬", "╬", 2, 2, 2, 2, True),
    "╤": Piece("╤", "╢", 2, 1, 2, 0),
    "╢": Piece("╢", "╧", 0, 2, 1, 2),
    "╧": Piece("╧", "╟", 2, 0, 2, 1),
    "╟": Piece("╟", "╤", 1, 2, 0, 2),
    "╨": Piece("╨", "╞", 1, 0, 1, 2),
    "╞": Piece("╞", "╥", 2, 1, 0, 1),
    "╥": Piece("╥", "╡", 1, 2, 1, 0),
    "╡": Piece("╡", "╨", 0, 1, 2, 1),
    "╒": Piece("╒", "╖", 2, 1, 0, 0),
    "╖": Piece("╖", "╛", 0, 2, 1, 0),
    "╛": Piece("╛", "╙", 0, 0, 2, 1),
    "╙": Piece("╙", "╒", 1, 0, 0, 2),
    "╓": Piece("╓", "╕", 1, 2, 0, 0),
    "╕": Piece("╕", "╜", 0, 1, 2, 0),
    "╜": Piece("╜", "╘", 0, 0, 1, 2),
    "╘": Piece("╘", "╓", 2, 0, 0, 1),
}


with open("input.txt", encoding="cp437") as f:
    grid = [
        [replace(PIECES.get(c, PIECES[" "])) for c in line[6:-6]]
        for line in f.read().splitlines()[4:-5]
    ]

grid[0][1].fixed = True
grid[-1][-2].fixed = True

result = 0
changes = True

while changes:
    changes = False
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.fixed:
                continue
            possible_connections = [
                grid[y + dy][x + dx].possible_connections((d + 2) % 4)
                for d, (dx, dy) in enumerate(((1, 0), (0, 1), (-1, 0), (0, -1)))
            ]
            possible_rotations = cell.possible_rotations(possible_connections)
            assert possible_rotations, f"impossible {x}, {y}, {possible_connections}"
            if len(possible_rotations) == 1:
                grid[y][x] = replace(cell.rotate(possible_rotations[0]), fixed=True)
                result += possible_rotations[0]
                changes = True

for row in grid:
    print("".join(c.char for c in row))

print(result)
