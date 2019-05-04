import random

class State:
    def __init__(self, data):
        #general game data
        turn = int(data['turn'])
        game_id = data['game']['id']

        #(You)
        you = data['you']
        self.health = you['health']
        body = you['body']
        self.x = int(body[0]['x'])
        self.y = int(body[0]['y'])

        #board data
        board = data['board']
        self.board_width = int(board['width'])
        self.board_height = int(board['height'])
        self.board_food = board['food']
        
        self.occupancy = list()
        self.territory = list()
        
        for x in range(0, self.board_width):                
            column = [0]*self.board_height
            self.occupancy.append(column)
            
        for x in range(0, self.board_width):               
            column = [0]*self.board_height
            self.territory.append(column)

        self.snakes = board['snakes']

        for i, node in enumerate(body):
            x = int(node['x'])
            y = int(node['y'])
            time = len(body) - i
            self.occupancy[x][y] = time
        
        for s in self.snakes:
            b = s['body']
            for i, node in enumerate(b):
                x = int(node['x'])
                y = int(node['y'])
                time = len(b)-i
                self.occupancy[x][y] = time

		for x, row in enumerate(self.territory):
			for y, column in enumerate(x):
				
				#check you first
				you_dist = distance_between(you['body'][0]['x'], you['body'][0]['y'], x, y)
				snake_dist = distance_between(self.snakes[0]['body'][0]['x'], self.snakes[0]['body'][0]['y'], x, y)
				for s in self.snakes:
					test_dist = distance_between(s['body'][0]['x'], s['body'][0]['y'], x, y)
					if test_dist < snake_dist:
						snake_dist = test_dist
				if you_dist < snake_dist:
					self.territory[x][y] = 0
				else:
					self.territory[x][y] = 1
			
        
    @classmethod
    def board_food_count():
        return len(self.board_food)
        


# An occupied space is considered all snake bodies on the map, including your own
class OccupiedSpace:
    def __init__(self, state, x, y):
        self.x = x
        self.y = y
        self.turns_to_empty = 0


# Returns a tuple containing the rise over run
# adding these two values together will get you the total distance between
def distance_between(x1, y1, x2, y2):
    x = abs(x2-x1)
    y = abs(y2-y1)
    return x+y
    
def find_free_space(state):
    directions = ['up', 'down', 'left', 'right']
    direction = directions[0]
    safe_space = False

    while not safe_space:
        direction = random.choice(directions)
        dx = state.x
        dy = state.y
        
        if direction== 'left':
            dx = dx-1
        elif direction == 'right':
            dx = dx+1
        elif direction == 'up':
            dy = dy-1
        elif direction == 'down':
            dy = dy+1
            
        if dx > 0 and dx < 15:
            if dy > 0 and dy < 15:    
                if state.occupancy[dx][dy] == 0:
                    safe_space = True
            
    return direction


# for one turn, where S is snake count
# N = S*3
# no.permutations = !N

def find_nearest_food(state):
    for food in state.board_food:
        for snake in state.snakes:
            length = distance_between()
        

def find_best_move(turns, state):
    no_snakes = 1+ len(state.snakes)

	






    
