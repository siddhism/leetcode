#
# @lc app=leetcode id=353 lang=python
#
# [353] Design Snake Game
#

class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        from collections import deque
        self.width = width
        self.height = height
        self.foods = food
        self.sh = 0
        self.pos = (0, 0)
        self.map = {
            'L': [0, -1],
            'R': [0, 1],
            'U': [-1, 0],
            'D': [1, 0]
        }
        self.snake = deque([[0,0]]) # since head is at first point
    
    def is_end(self, r, c):
        # print ' r ', r, ' c' , c, ' w ', self.width,  ' h ', self.height
        if (r < 0 or r >= self.height) or (c < 0 or c >= self.width):
            return True
        return False
    
    def is_snake_crossing_boundary(self, new_head, direction):
        # add this to snake's current position and height
        is_end =  self.is_end(new_head[0], new_head[1])
        # head being at tail is fine as we'll move the tail just now, thoda ruko to sahi
        if is_end or (new_head in self.snake and new_head != self.snake[-1]):
            return True
        return False

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        # after each move snake's length will increase
        nr, nc = self.map.get(direction)
        # print 'directi
        # on ', nr, nc, ' pos before move ', self.pos
        new_head = [self.snake[0][0] + nr, self.snake[0][1] + nc]
        if self.is_snake_crossing_boundary(new_head, direction):
            return -1
        # print ' pos after move ', self.pos, ' food ', self.foods[self.sh]
        if self.foods and self.foods[0] == new_head:
            # eat food
            self.snake.appendleft(new_head)
            self.foods = self.foods[1:] # pop the item from food
            # self.foods.popleft()
        else:
            # not eating food, append head and remove tail
            self.snake.appendleft(new_head)
            self.snake.pop()
        return len(self.snake) - 1
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)