test = {
  'name': 'Always, Simple Strategies',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> for i in range(1000):
          ...     assert 0 == agents.rock_strategy(), "rock_strategy is incorrect";
          ...     assert 1 == agents.paper_strategy(), "paper_strategy is incorrect";
          ...     assert 2 == agents.scissors_strategy(), "scissors_strategy is incorrect";
          ...     assert 0 <= agents.simple_strategy() <= 2, "simple_strategy is incorrect";
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> assert Simulator.simulator(agents.rock_strategy,        agents.paper_strategy, simulation_count=1000, silent=True) == (0, 1, 0),    "Simulation failed. Error in strategies";
          >>> assert Simulator.simulator(agents.paper_strategy,       agents.rock_strategy, simulation_count=1000, silent=True) == (1, 0, 0),     "Simulation failed. Error in strategies";
          >>> assert Simulator.simulator(agents.scissors_strategy,    agents.rock_strategy, simulation_count=1000, silent=True) == (0, 1, 0),     "Simulation failed. Error in strategies";
          >>> assert Simulator.simulator(agents.rock_strategy,        agents.scissors_strategy, simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies";
          >>> assert Simulator.simulator(agents.paper_strategy,       agents.scissors_strategy, simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies";
          >>> assert Simulator.simulator(agents.scissors_strategy,    agents.paper_strategy, simulation_count=1000, silent=True) == (1, 0, 0),    "Simulation failed. Error in strategies";
          >>> a =    Simulator.simulator(agents.rock_strategy,        agents.rock_strategy, simulation_count=1000, silent=True);
          >>> b =    Simulator.simulator(agents.paper_strategy,       agents.paper_strategy, simulation_count=1000, silent=True);
          >>> c = Simulator.simulator(agents.scissors_strategy,       agents.scissors_strategy, simulation_count=1000, silent=True);
          >>> assert a == b == c, "Simulation failed -- when run against each other, the strategies did not completely tie";
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sr = [round(x, 2) for x in Simulator.simulator(agents.simple_strategy, agents.rock_strategy,      silent=True)];
          >>> sp = [round(x, 2) for x in Simulator.simulator(agents.simple_strategy, agents.paper_strategy,     silent=True)];
          >>> ss = [round(x, 2) for x in Simulator.simulator(agents.simple_strategy, agents.scissors_strategy,  silent=True)];
          >>> assert sr == sp == ss and sr[0] == sr[1] == sr[2] == .33, "Simulation failed. Error in strategies";
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
