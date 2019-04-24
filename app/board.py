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
        self.occupancy = list()
        
        for x in range(0, self.board_width):
            column = [0]*self.board_height
            self.occupancy.append(column)

        self.board_food = list()
        self.board_food_count = len(self.board_food)
        
