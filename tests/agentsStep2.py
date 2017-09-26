test = {
  'name': 'triple_biased_strategy',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> simple = agents.triple_biased_strategy(1/3, 1/3, 1/3)
          >>> simple_test = Simulator.simulator(agents.simple_strategy, simple, simulation_count= 100000, silent = True)
          >>> assert simple_test[0] >= 0.32 and simple_test[0] <= 0.34 and simple_test[1] >= 0.32 and simple_test[1] <= 0.34 and simple_test[2] >= 0.32 and simple_test[2] <= 0.34, "Error"
          >>> assert Simulator.simulator(agents.rock_strategy, agents.triple_biased_strategy(0, 1, 0), simulation_count = 1000, silent = True) == (0, 1, 0), "Doesn't adequately counter rock_strategy"
          >>> assert Simulator.simulator(agents.paper_strategy, agents.triple_biased_strategy(0, 0, 1), simulation_count = 1000, silent = True) == (0, 1, 0), "Doesn't adequately counter paper_strategy"
          >>> assert Simulator.simulator(agents.scissors_strategy, agents.triple_biased_strategy(1, 0, 0), simulation_count = 1000, silent = True) == (0, 1, 0), "Doesn't adequately counter scissors_strategy"
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> chance = [i / 1000 for i in range(1000)]
          >>> for i in chance:
          ...     rock_chance = i
          ...     paper_chance = round((1 - i) / 2, 3)
          ...     scissors_chance = paper_chance
          ...     strat = agents.triple_biased_strategy(rock_chance, paper_chance, scissors_chance)
          ...     results = [strat() for _ in range(1000)]
          ...     rock_results = len([i for i in results if i == 0])
          ...     paper_results = len([i for i in results if i == 1])
          ...     scissors_results = len([i for i in results if i == 2])
          ...     assert rock_results / len(results) >= rock_chance - 0.01 or rock_results / len(results) <= rock_chance + 0.01, "Check when you're returning rock"
          ...     assert paper_results / len(results) >= paper_chance - 0.01 or paper_results / len(results) <= paper_chance + 0.01, "Check when you're returning paper"
          ...     assert scissors_results / len(results) >= scissors_chance - 0.01 or scissors_results / len(results) <= scissors_chance + 0.01, "Check when you're returing scissors"
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import agents as agents
      >>> import History as History
      >>> import Simulator as Simulator
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
