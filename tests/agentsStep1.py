test = {
  'name': 'biased_strategy',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> always_rock = agents.biased_strategy(1, 0);
          >>> always_paper = agents.biased_strategy(1, 1);
          >>> always_scissors = agents.biased_strategy(1, 2);
          >>> assert Simulator.simulator(agents.rock_strategy, always_rock, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return rock";
          >>> assert Simulator.simulator(agents.paper_strategy, always_paper, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return paper";
          >>> assert Simulator.simulator(agents.scissors_strategy, always_scissors, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return scissors";
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> never_rock = agents.biased_strategy(0, 0);
          >>> never_paper = agents.biased_strategy(0, 1);
          >>> never_scissors = agents.biased_strategy(0, 2);
          
          >>> never_rock_results = [never_rock for i in range(1000)];
          >>> never_paper_results = [never_paper for i in range(1000)];
          >>> never_scissors_results = [never_scissors for i in range(1000)];
          >>> assert 0 not in never_rock_results, "Error: Invalid value generation for biased_strategy(0, 0)";
          >>> assert 1 not in never_paper_results, "Error: Invalid value generation for biased_strategy(0, 1)";
          >>> assert 2 not in never_scissors_results, "Error: Invalid value generation for biased_strategy(0, 2)";
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
