"""
A History object takes in two strategies and keeps track of the history of those two strategies playing against each other in a Simulator 


Arg strategy1: a strategy that returns either a number between 0 and 2, inclusive
Arg strategy2: a strategy that returns either a number between 0 and 2, inclusive

Important methods:
    
    get_chronological_history()
        Gets the history of moves by both strategies in chronological order (will not be able to tell which history is which)
        Data is returned as a list of two element tuples of this format: (strategy1_move, strategy2_move)
        
    get_own_chronological_history(own_strategy)
        Gets the history of moves by the own_strategy, in chronological order
        Data is returned as a list of moves in the range [0, 2], inclusive of this format [own_strategy_move_1, own_strategy_move_2, ...]
        Arg own_strategy: the strategy that you're calling this from (used to determine which sequence of moves is "own")
    
    get_opponent_chronological_history(own_strategy)
        Gets the history of moves by the opponent, in chronological order
        Data is returned as a list of moves in the range [0, 2], inclusive of this format [opponent_strategy_move_1, opponent_strategy_move_2, ...]
        Arg own_strategy: the strategy that you're calling this from (used to determine the opponent)
    
    
    get_opponent_frequency(own_strategy)
        Given which strategy is calling to get the opponent's move frequency, the function returns the opponent's move frequency
        Arg own_strategy: the strategy that you're calling this from (used to determine the opponent)
        Returns a tuple of frequencies in the format of (rock_frequency, paper_frequency, scissor_frequency)
    


===============EXAMPLE===============

With history

    strategy1 = always_rock_strategy
    strategy2 = biased_strategy(.9, 1)                                  #A biased strategy that favors paper 90% of the time
    history = History(strategy1, strategy2)             
    print( simulator(strategy1, strategy2, history) )
    
    print( history.get_chronological_history() )
    print( history.get_opponent_chronological_history(strategy1) )      #Gets Strategy 2's chronological_history of moves
    print( history.get_opponent_frequency(strategy1) )                  #Gets Strategy 2's frequency of moves
    
"""

class History():

    def __init__(self, strategy1, strategy2):
        #Creates two types of history - (1) a chronological sequence of the moves played and (2) a representation of the relative frequencies of moves by each AI
        self.chronological_history = []
        self.length = 0

        #Dictionaries containing the moves counts of each strategy thus far
        self.strategy1_move_count = {0:0, 1:0, 2:0}
        self.strategy2_move_count = {0:0, 1:0, 2:0}

        self.strategy1 = strategy1
        self.strategy2 = strategy2

    def add(self, x):
        """
        Adds to both types of historical documentation of the game being played
        Arg x: a tuple composed of two elements of structure (strategy1_play, strategy2_play)
        """
        
        assert type(x) == tuple, "Incorrect argument passed into add - needs a tuple"
        assert len(x) == 2, "Incorrect length of tuple passed in - structure should be in form of (strategy1_play, strategy2_play) with a length of 2"

        #Get the move each strategy made and advance the move_count for that move for that strategy
        self.strategy1_move_count[ x[0] ] += 1
        self.strategy2_move_count[ x[1] ] += 1

        #Add their moves to the history and increment the length
        self.chronological_history.append(x)
        self.length += 1

    def get_opponent_frequency(self, own_strategy):
        """
        Given which strategy is calling to get the opponent's move frequency, the function returns the opponent's move frequency
        Arg own_strategy: the function that is called within the simulator (used to determine the opponent)
        Returns a tuple of frequencies in the format of (rock_frequency, paper_frequency, scissor_frequency)
        """
    
        #If no moves have occurred yet, all frequencies are zero
        if len(self) == 0:
            return (0, 0, 0)

        #Get the opponent's move count dictionary
        if own_strategy == self.strategy1:
            opponent_move_count = self.strategy2_move_count
        else:
            opponent_move_count = self.strategy1_move_count

        #Compute frequencies and return in tuple
        return (opponent_move_count[0]/len(self),
                opponent_move_count[1]/len(self),
                opponent_move_count[2]/len(self))

    def get_chronological_history(self):
        """
        Gets the history of moves (represented as a list of two element tuples) by both strategies in chronological order (will not be able to tell which history is which)
        """
        
        return self.chronological_history

    def get_own_chronological_history(self, own_strategy):
        """
        Gets the history of moves by the own_strategy, in chronological order
        Arg own_strategy: the function that is called within the simulator (used to determine which sequence of moves is "own")
        """
        
        #Uses the own_strategy passed in to find the index the opponent move will be at
        if own_strategy == self.strategy1:
            index = 0
        else:
            index = 1

        #Returns a list of the opponent moves in chronological order
        return [turn[index] for turn in self.get_chronological_history()]
    
    def get_opponent_chronological_history(self, own_strategy):
        """
        Gets the history of moves by the opponent, in chronological order
        Arg own_strategy: the function that is called within the simulator (used to determine the opponent)
        """
        
        #Uses the own_strategy passed in to find the index the opponent move will be at
        if own_strategy == self.strategy1:
            index = 1
        else:
            index = 0

        #Returns a list of the opponent moves in chronological order
        return [turn[index] for turn in self.get_chronological_history()]

    def __len__(self):
        """Returns the length of the history"""
        return self.length
