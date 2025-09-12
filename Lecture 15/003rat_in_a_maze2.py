def f(maze:list[list[str]], m:int, n:int, i:int, j:int)->bool:
	# base case

	if i == m or j == n: # you've gone outside the maze
		return False

	if maze[i][j] == 'X': # you've reached a blocked cell
		return False

	if i == m-1 and j == n-1: # you've reached the destination
		return True

	# recursive case

	# f(i, j) = it is fn that checks if there is a path from i,jth cell to m-1,n-1th cell

	# decide the next step

	# option 1 : move down

	# option 2 : move right

	return f(maze, m, n, i+1, j) or f(maze, m, n, i, j+1)


maze = [['0', '0', '0', '0'],
		['0', '0', 'X', '0'], 
		['0', '0', '0', 'X'],
		['0', 'X', '0', '0']]

m = len(maze)
n = len(maze[0])

print(f(maze, m, n, 0, 0))