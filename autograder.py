from starter_RPS import * 
#from agents import *
import agents
import Simulator
import History
import numpy as np
import random

import sys
from io import StringIO

class Capture(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio 
        sys.stdout = self._stdout

def test_RPS():
    prompt = "Please input which Step you'd like to test (0 through 5)\n"
    choice = input(prompt).strip()
    name = "random name"
    
    #Test cases for Step 0
    if choice == "0":
        assert get_name() != ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<", "Step 0 is \
        incorrect, please fill in a name"
        print("Testing for step 0 complete")
        
    
    
    #Test cases for Step 1
    if choice == "1":
        #dummy functions to help run tests
        # def play_again_dummy():
        #     print("Want to play again? (or your custom prompt)")
        #     print("Note: This test will test the entire step at once, so complete it before trying")
        #     print("If the test suite does not exit, likely a valid input has not been passed in, so try typing input below")
        #     print("The test should be able to exit on 'YES'")
        #     # Test by passing in terminal arguments i.e. 'YES', 'yes', 'no', 'nO', 'asda'
        #     with Capture() as output:
        #         play_again()
        #     print("Your prompt: " + output[0]) # Shouldn't be the default
        #     assert output[0] != ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<", "Add a new prompt!"
        #     print("Your input: " + output[1]) # Can be anything
        #     print("Choice output: " + output[2]) # Must be lowercase
        #     assert output[2] == output[2].lower(), "Make sure you're making the input lowercase"
        #     print("Result: " + output[3]) # Needs to deterministically be true, false, or invalid
        # play_again_dummy()
        # def play_again_test():
        #     play_again()
        #     print(sys.argv[0])
        #     # """play_again test cases
        #     # >>> play_again
        #     # True
        #     # """
        # play_again_test()
        
        print("See doctest for play_again")
        print("Testing for step 1 complete")
    
    #Test cases for Step 2
    if choice == "2":
        # Coupon collectors to ensure all values should be taken given rand sampling
        expected = 6  # rounded up from 3* (1 + 1/2 + 1/3), or ~3 log 3
        outputs = ["rock", "paper", "scissors"]
        rcount = 0
        scount = 0
        pcount = 0
        for i in range(2*expected):
            move = basic_ai()
            assert move in outputs, "Step 2 returns the wrong output"
            if (move == "rock"):
                rcount += 1
            if (move == "scissors"):
                scount += 1
            if (move == "paper"):
                pcount += 1
        assert rcount > 0, " You seem to be getting a low number of rocks"
        assert scount > 0, " You seem to be getting a low number of scissors"
        assert pcount > 0, " You seem to be getting a low number of papers"
        print("Testing for step 2 complete")
    
    #Test cases for Step 3
    if choice == "3":
        def determine_winner_dummy(name, move, ai_move):
            if move == ai_move:
                return "Tie, no one wins!"
            
            #Win case 1
            elif move == "rock" and ai_move == "scissors":
                return name + " wins!"
            
            #Win case 2
            elif move == "paper" and ai_move == "rock":
                return name + " wins!"
            
            #Win case 3    
            elif move == "scissors" and ai_move == "paper":
                return name + " wins!"
            
            #Losing case
            else:
                return determine_winner(name, scissor, rock)
        name = 'urName'
        rock = 'rock'
        paper = 'paper'
        scissor = 'scissors'
        assert determine_winner_dummy(name, rock, scissor) == \
        determine_winner(name, rock, scissor), "step 4 1st case incorrect"
        assert determine_winner_dummy(name, paper, rock) == \
        determine_winner(name, paper, rock), "step 4 2nd case incorrect"
        assert determine_winner_dummy(name, scissor, paper) == \
        determine_winner(name, scissor, paper), "step 4 3rd case incorrect"
        assert determine_winner(name, scissor, rock) != \
        ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<", "step 4 losing case needs a unique message"
        assert determine_winner_dummy(name, scissor, rock) == \
        determine_winner(name, scissor, rock), "step 4 losing case incorrect (or above cases are covering too many options"
        print("Testing for step 3 complete")
        
    #Test cases for Step 4
    if choice == "4":
        #assert basic_ai() == ("rock" or "paper" or "scissors"), "step 4 is incorrect"
        # def play_dummy():
        #     print("Enter your move! (or your custom prompt)")
        #     print("Note: This test will test the entire step at once, so complete it before trying")
        #     print("If the test suite does not exit, likely a valid input has not been passed in, so try typing input below")
        #     with Capture() as output:
        #         play("Your Name")
        #     print("Your prompt: " + output[0]) # Shouldn't be the default
        #     assert output[0] != ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<", "Add a new prompt!"
        #     print("Your input: " + output[1]) # Can be anything
        #     print("Choice output: " + output[2]) # Must be lowercase
        #     assert output[2] == output[2].lower(), "Make sure you're making the input lowercase"
        #     #print("Result: " + output[3]) # Needs to deterministically be true, false, or invalid
        #     assert 'wins' in output[3], "make sure you have the right functional abstraction"
        #     assert len(output) == 7, "If no print statements have been deleted, then wrong silent behavior" 
            
        # play_dummy()
        print("See doctest for play")
        print("Testing for step 4 complete")
    #Test cases for Step 5
    if choice == "5":
        # print("What's your name? (or your custom prompt)")
        # print("After you enter your name, run the play sequence")
        # with Capture() as output:
        #     main()
        # assert output[0] != ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<", "Add a new prompt!"
        # assert output[1] == 'True', "make sure you have correct initial behavior for continue playing"
        # #assert output[2], "Play again message here"
        print("See doctest for main")
        print("Testing for step 5 complete")
    return None   
        

def test_Agents():
    prompt = "Please input which Step you'd like to test (0 through 5)\n"
    choice = input(prompt).strip()
    
    #Test cases for Step 0
    if choice == "0":
        
        #Testing general output
        for i in range(1000):
            assert 0 == agents.rock_strategy(), "rock_strategy is incorrect"
            assert 1 == agents.paper_strategy(), "paper_strategy is incorrect"
            assert 2 == agents.scissors_strategy(), "scissors_strategy is incorrect"
            assert 0 <= agents.simple_strategy() <= 2, "simple_strategy is incorrect"
            
        #Testing simulator runs
        assert Simulator.simulator(agents.rock_strategy, agents.paper_strategy, simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert Simulator.simulator(agents.paper_strategy, agents.rock_strategy, simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        assert Simulator.simulator(agents.scissors_strategy, agents.rock_strategy, simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert Simulator.simulator(agents.rock_strategy, agents.scissors_strategy, simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        assert Simulator.simulator(agents.paper_strategy, agents.scissors_strategy, simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert Simulator.simulator(agents.scissors_strategy, agents.paper_strategy, simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        assert (Simulator.simulator(agents.rock_strategy, agents.rock_strategy,          simulation_count=1000, silent=True) == 
                Simulator.simulator(agents.paper_strategy, agents.paper_strategy,        simulation_count=1000, silent=True) ==
                Simulator.simulator(agents.scissors_strategy, agents.scissors_strategy,  simulation_count=1000, silent=True) == 
               (0, 0, 1)), "Simulation failed -- when run against each other, the strategies did not completely tie"
               
        #Simple strategy should always win 1/3, lose 1/3, and tie 1/3 -- no matter the complexity of its opponent
        sr = [round(x, 2) for x in Simulator.simulator(agents.simple_strategy, agents.rock_strategy,       silent=True)]
        sp = [round(x, 2) for x in Simulator.simulator(agents.simple_strategy, agents.paper_strategy,      silent=True)]
        ss = [round(x, 2) for x in Simulator.simulator(agents.simple_strategy, agents.scissors_strategy,   silent=True)]
        assert sr == sp == ss and sr[0] == sr[1] == sr[2] == .33, "Simulation failed. Error in strategies"
        
        print("Passed all tests -- Step 0 complete")
    
    #"One test I definitely want to do for agents is creating a smart strategy that specifically can trash a reflexive_strategy that ALWAYS picks a move "
    if choice == "1":

        always_rock = agents.biased_strategy(1, 0)
        always_paper = agents.biased_strategy(1, 1)
        always_scissors = agents.biased_strategy(1, 2)
        
        
        assert Simulator.simulator(agents.rock_strategy, always_rock, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return rock" 
        assert Simulator.simulator(agents.paper_strategy, always_paper, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return paper"
        assert Simulator.simulator(agents.scissors_strategy, always_scissors, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return scissors"
        
        never_rock = agents.biased_strategy(0, 0)
        never_paper = agents.biased_strategy(0, 1)
        never_scissors = agents.biased_strategy(0, 2)
        
        never_rock_results = [never_rock for i in range(1000)]
        never_paper_results = [never_paper for i in range(1000)]
        never_scissors_results = [never_scissors for i in range(1000)]

        assert 0 not in never_rock_results, "Error: Invalid value generation for biased_strategy(0, 0)"
        assert 1 not in never_paper_results, "Error: Invalid value generation for biased_strategy(0, 1)"
        assert 2 not in never_scissors_results, "Error: Invalid value generation for biased_strategy(0, 2)"
        print("Passed all tests -- Step 1 complete")

    if choice == "2":
        
        simple = agents.triple_biased_strategy(1/3, 1/3, 1/3)
        simple_test = simulator(simple_strategy, simple, simulation_count= 100000, silent = True)
        assert simple_test[0] >= 0.32 and simple_test[0] <= 0.34 and simple_test[1] >= 0.32 and simple_test[1] <= 0.34 and simple_test[2] >= 0.32 and simple_test[2] <= 0.34, "Error"

        chance = [i / 1000 for i in range(1000)]
        #Maybe make a function to do this to efficiently assign paper_chance and scissors_chance to i?
        for i in chance:
            rock_chance = i
            paper_chance = round((1 - i) / 2, 3)
            scissors_chance = paper_chance
            strat = triple_biased_strategy(rock_chance, paper_chance, scissors_chance)
            results = [strat() for _ in range(1000)]
            rock_results = len([i for i in results if i == 0])
            paper_results = len([i for i in results if i == 1])
            scissors_results = len([i for i in results if i == 2])
            assert rock_results / len(results) >= rock_chance - 0.01 or rock_results / len(results) <= rock_chance + 0.01, "Check when you're returning rock"
            assert paper_results / len(results) >= paper_chance - 0.01 or paper_results / len(results) <= paper_chance + 0.01, "Check when you're returning paper"
            assert scissors_results / len(results) >= scissors_chance - 0.01 or scissors_results / len(results) <= scissors_chance + 0.01, "Check when you're returing scissors"
            #Try to incorporate History object
        print("Passed all tests -- Step 2 complete")
    
    
    if choice == "3":
        strat = agents.deterministic_strategy()
        deterministic_order = [0, 1, 2, 1, 0]
        simple_test_results = []
        for _ in range(len(deterministic_order)):
            simple_test_results.append(strat())
        assert simple_test_results == deterministic_order, "Failed simple test"

        for _ in range(10000):
            random_test_results = []
            strategy = agents.deterministic_strategy()
            turns = random.randint(1, 1000)
            for _ in range(turns):
                random_test_results.append(strategy())
            answer = deterministic_order * (turns // len(deterministic_order))
            for i in range(turns - len(answer)):
                answer.append(deterministic_order[i])

            assert answer == random_test_results, "Deterministic strategy does not match expected output"
        print("Passed all tests -- Step 3 complete")
    
    if choice == "4":
        agents.history = History.History(agents.rock_strategy, agents.reflexive_strategy)
        assert round(Simulator.simulator(agents.rock_strategy, agents.reflexive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
        agents.history = History.History(agents.paper_strategy, agents.reflexive_strategy)
        assert round(Simulator.simulator(agents.paper_strategy, agents.reflexive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
        agents.history = History.History(agents.scissors_strategy, agents.reflexive_strategy)
        assert round(Simulator.simulator(agents.scissors_strategy, agents.reflexive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
        trials = 1000
        wins = 0
        for _ in range(trials):
            #generate 3 random numbers that add up to 1
            rates = np.random.random(3)
            rates /= rates.sum()
            #rates = (.1, .1, .8)
            strategy1 = agents.triple_biased_strategy(rates[0], rates[1], rates[2])
            strategy2 = agents.reflexive_strategy
            
            agents.history = History.History(strategy1, strategy2)
            
            results = Simulator.simulator(strategy1, strategy2, history_storage = agents.history, simulation_count = 1000, silent = True)
            if results[1] > results[0]:
                wins += 1
            if results[0] - results[1] > 0:
                assert results[0] - results[1] < 0.1
        assert wins/trials > 0.9, "error"

        print("Passed all tests -- Step 4 complete")

    if choice == "5":
        agents.history = History.History(agents.rock_strategy, agents.predictive_strategy)
        assert round(Simulator.simulator(agents.rock_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
       
        agents.history = History.History(agents.paper_strategy, agents.predictive_strategy)
        assert round(Simulator.simulator(agents.paper_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
     
        agents.history = History.History(agents.scissors_strategy, agents.predictive_strategy)
        assert round(Simulator.simulator(agents.paper_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1

        trials = 1000
        wins = 0
        for _ in range(trials):
            test_length = random.randint(2, 10)
            test_list = [random.randint(0, 2) for _ in range(test_length)]
            deterministic = deterministic_list(test_list)
            agents.history = History.History(deterministic, agents.predictive_strategy)
            result = Simulator.simulator(deterministic, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)
            print(result)
            if result[0] < result[1]:
                wins += 1
        assert wins / trials >= 0.8, "Your strategy does not win enough"

        print("Passed all tests -- Step 5 complete")

def deterministic_list(lst):
    deterministic_order = lst
    length_of_sequence = len(deterministic_order)
    
    index = 0

    def generate_deterministic_move():
        nonlocal index
        value = deterministic_order[index % length_of_sequence]
        index += 1
        return value
    return generate_deterministic_move

if __name__ == "__main__":
    
    prompt = "Type the number of the testing suite would you like to use: \n\t1) RPS\n\t2) AI Agents\n"
    test_suite = input( prompt )
    
    if test_suite == '1':
        test_RPS()
    elif test_suite == '2':
        test_Agents()
    else:
        error_msg = "Error, the testing suite you specified is not valid -- please run again and select 1 to test RPS or 2 to test AI Agents"
        print(error_msg)
    import doctest
    doctest.testmod()
    
    
    
    
    