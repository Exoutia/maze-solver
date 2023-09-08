from pathlib import Path

from maze_solver.models.maze import Maze
from maze_solver.view.renderer import SVGRenderer

file_name = "labyrinth.maze"
path = Path("src/test/mazes") / file_name

maze = Maze.load(path)
print(len(maze.squares), maze.height, maze.width)

SVGRenderer().render(maze).preview()
