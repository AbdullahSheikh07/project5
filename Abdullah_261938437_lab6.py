class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return (self.length+self.width)*2
   

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())
print(newRectangle.rectangle_perimeter())

def __init__(self, player_id, player_name, player_runs, dob, shirt_number):
    self.player_id = player_id
    self.player_name = player_name
    self.player_runs = player_runs
    self.dob = dob
    self.shirt_number = shirt_number

    # Add player runs to class variable total_runs
    Player.total_runs += player_runs

def display_info(self):
    print("Player ID:", self.player_id)
    print("Player Name:", self.player_name)
    print("Player Runs:", self.player_runs)
    print("Player Date of Birth:", self.dob)
    print("Player Shirt Number:", self.shirt_number)

def get_runs(self):
    return self.player_runs

def add_runs(self, runs):
    self.player_runs += runs
    Player.total_runs += runs

# Getter and setter for player ID
def get_player_id(self):
    return self.player_id

def set_player_id(self, player_id):
    self.player_id = player_id

# Getter and setter for player name
def get_player_name(self):
    return self.player_name

def set_player_name(self, player_name):
    self.player_name = player_name

# Getter and setter for player runs
def get_player_runs(self):
    return self.player_runs

def set_player_runs(self, player_runs):
    # Subtract old player runs from class variable total_runs
    Player.total_runs -= self.player_runs

    # Add new player runs to class variable total_runs
    Player.total_runs += player_runs

    self.player_runs = player_runs

# Getter and setter for player date of birth
def get_dob(self):
    return self.dob

def set_dob(self, dob):
    self.dob = dob

# Getter and setter for player shirt number
def get_shirt_number(self):
    return self.shirt_number

def set_shirt_number(self, shirt_number):
    self.shirt_number = shirt_number

# Method to return class variable total_runs
@classmethod
def get_total_runs(cls):
    return cls.total_runs

    
