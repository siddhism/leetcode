class Node():
  def __init__(self, r, c, depth):
    self.depth = depth
    self.coord_r = r
    self.coord_c = c

def add_allowed_next_nodes(grid, starting_node):
  allowed_nodes = []
  n = len(grid) #nb of rows of grid
  m = len(grid[0]) #nbs of columns of grid
  
  if starting_node.coord_r+1 <= n:
    if grid[starting_node.coord_r+1, starting_node.coord_c] == 1:
      allowed_nodes.append(Node(starting_node.coord_r+1, starting_node.coord_c, starting_node.depth+1))
      
  if starting_node.coord_r-1 >= 0:
    if grid[starting_node.coord_r-1, starting_node.coord_c] == 1:
      allowed_nodes.append(Node(starting_node.coord_r-1, starting_node.coord_c, starting_node.depth+1))
      
  if starting_node.coord_c+1 <= m:
    if grid[starting_node.coord_r, starting_node.coord_c+1] == 1:
      allowed_nodes.append(Node(starting_node.coord_r, starting_node.coord_c+1, starting_node.depth+1))
      
  if starting_node.coord_c-1 >= 0:
    if grid[starting_node.coord_r, starting_node.coord_c-1] == 1:
      allowed_nodes.append(Node(starting_node.coord_r, starting_node.coord_c-1, starting_node.depth+1))
  
  return allowed_nodes
    

def shortestCellPath(grid, sr, sc, tr, tc):
    """
    @param grid: int[][]
    @param sr: int
    @param sc: int
    @param tr: int
    @param tc: int
    @return: int
    """
  
  to_explore = []
  
  starting_node = Node(r = sr, c = sc, depth = 0)
  # to_explore.insert(0, starting_node)
  to_explore.insert(0, add_allowed_next_nodes(grid, starting_node))
  
  while to_explore:
    next_node = to_explore.pop()
    
    if next_node.coord_r == tr and next_node.coord_c == tc:
      return next_node.depth
    
    to_explore.insert(0, add_allowed_next_nodes(grid, next_node))

  return -1
  

  
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0

print(shortestCellPath(grid, sr, sc, tr, tc))
