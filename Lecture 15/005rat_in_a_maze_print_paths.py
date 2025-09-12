def print_path(path:list[list[str]], m:int, n:int)->None:
	for i in range(m):
		for j in range(n):
			print(path[i][j], end='')
		print()
	print()


def f(maze:list[list[str]], path:list[list[str]], m:int, n:int, i:int, j:int)->None:

	# base case

	if i == m or j == n:
		return

	if maze[i][j] == 'X':
		return

	if i == m-1 and j == n-1:
		path[i][j] = '1'
		print_path(path, m, n)
		path[i][j] = '0'
		return

	# recursive case

	path[i][j] = '1'
	f(maze, path, m, n, i, j+1)
	f(maze, path, m, n, i+1, j)
	path[i][j] = '0' # backtracking

	

maze = [['0', '0', '0', '0'],
		['0', '0', 'X', '0'], 
		['0', '0', '0', 'X'],
		['0', 'X', '0', '0']]

m = len(maze)
n = len(maze[0])

path = [['0'] * n for _ in range(m)]

f(maze, path, m, n, 0, 0)