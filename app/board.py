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
        self.board_food = list() #board['food']
        
        self.occupancy = list()
        
        for x in range(0, self.board_width):                
            column = [0]*self.board_height
            self.occupancy.append(column)


        snakes = board['snakes']

        for s in snakes:
            b = s['body']
            for node in b:
                occupancy[int(b['x'])][int(b['y'])] = OccupiedSpace(self, int(b['x']), int(b['y']))
            
              

        
    @classmethod
    def board_food_count():
        return len(self.board_food)
        


# An occupied space is considered all snake bodies on the map, including your own
class OccupiedSpace:
    def __init__(self, state, x, y):
        self.x = x
        self.y = y
        self.turns_to_empty = distance_between(x, y, state.x, state.y)


# Returns a tuple containing the rise over run
# adding these two values together will get you the total distance between
def distance_between(x1, y1, x2, y2):
    x = abs(x2-x1)
    y = abs(y2-y1)
    return x+y
    
