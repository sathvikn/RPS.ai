import time
import os
strategy_output_msg = "Strategies must output an integer between 0 and 2, inclusive. Invalid output received."

"""
A simulator takes in two strategies, an optional history object, an optional simulation_count, and an optional silent boolean. Returns a tuple of the format (strategy1_win_percentage, strategy2_win_percentage, tie_percentage)
A history argument does NOT need to be passed in unless the strategy requires it. Simulation count does not need to be changed from the default unless an instructor specifies.


Arg strategy1: a strategy that returns either a number between 0 and 2, inclusive
Arg strategy2: a strategy that returns either a number between 0 and 2, inclusive
Arg history_storage: a history object that strategies can utilize to detect patterns and change their strategies (Defaults to None)
Arg simulation_count: the number of simulations that will be run (Defaults to 1,000,000)
Arg silent: determines whether the Simulator will be silent by not printing out anything (Defaults to False)
 
Returns a tuple in the format of (strategy1 win percentage, strategy2 win percentage, tie percentage)

===============EXAMPLES===============

(1) Without history

    strategy1 = always_rock_strategy
    strategy2 = always_paper_strategy
    print( simulator(strategy1, strategy2) )


(2) With history

    strategy1 = always_rock_strategy
    strategy2 = biased_strategy(.9, 1)                      #A biased strategy that favors paper 90% of the time
    history = History(strategy1, strategy2)             
    print( simulator(strategy1, strategy2, history) )

(3) With history and simulation count
    
    strategy1 = always_rock_strategy
    strategy2 = biased_strategy(.9, 1)                      #A biased strategy that favors paper 90% of the time
    history = History(strategy1, strategy2)             
    print( simulator(strategy1, strategy2, history, 500) )  #Runs only 500 simulated "games" of RPS, instead of 1 million 

===============EXAMPLES===============    
"""

def simulator(strategy1, strategy2, history_storage=None, simulation_count=1000000, silent=False):

    start = time.time()

    #Ensuring strategies output integers
    assert type(strategy1()) == type(strategy2()) == int, strategy_output_msg
    #assert type(strategy1(history_storage)) == type(strategy2()) == int, strategy_output_msg
    #Counts of each strategy's wins, losses, and ties
    count1, count2, ties = 0, 0, 0

    #Simulates the game logic
    for i in range(simulation_count):
        strategy1_play, strategy2_play = strategy1(), strategy2()
        #strategy1_play = strategy1()
        #strategy2_play = strategy2(history_storage)

        #Strategy output check
        if not (0 <= strategy1_play <= 2) or not (0 <= strategy2_play <= 2):
            assert False, strategy_output_msg

        #Tie case
        if strategy1_play == strategy2_play:
            ties += 1;

        #Win case for strategy1 (strategy1_play, strategy2_play) -> (0,2), (1,0), (2,1)
        elif (strategy1_play - strategy2_play == 1) or (strategy1_play - strategy2_play == -2):
            count1 += 1;

        #Loss case for strategy1 - if you did not tie and did not win, you lost
        else:
            count2 += 1;

        #Adding the round to the history
        if history_storage is not None:
            history_storage.add((strategy1_play, strategy2_play))


    end = time.time()
    
    if not silent:
        os.system('clear');
        print("Simulation of", simulation_count, "games of RPS with both strategies took", end-start, "seconds.")

    return (count1/simulation_count, count2/simulation_count, ties/simulation_count)
