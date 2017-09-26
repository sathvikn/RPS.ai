test = {
  'name': 'predictive_strategy',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> agents.history = History.History(agents.rock_strategy, agents.predictive_strategy)
          >>> assert round(Simulator.simulator(agents.rock_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> agents.history = History.History(agents.paper_strategy, agents.predictive_strategy)
          >>> assert round(Simulator.simulator(agents.paper_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> agents.history = History.History(agents.scissors_strategy, agents.predictive_strategy)
          >>> assert round(Simulator.simulator(agents.paper_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> trials = 100
          >>> wins = 0
          >>> def deterministic_list(lst):
          ...     deterministic_order = lst
          ...     length_of_sequence = len(deterministic_order)
          ...     index = 0
          ...     def generate_deterministic_move():
          ...         nonlocal index
          ...         value = deterministic_order[index % length_of_sequence]
          ...         index += 1
          ...         return value
          ...     return generate_deterministic_move
          >>> for _ in range(trials):
          ...    test_length = random.randint(2, 10)
          ...    test_list = [random.randint(0, 2) for _ in range(test_length)]
          ...    deterministic = deterministic_list(test_list)
          ...    agents.history = History.History(deterministic, agents.predictive_strategy)
          ...    result = Simulator.simulator(deterministic, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)
          ...    if result[0] < result[1]:
          ...        wins += 1
          >>> assert wins / trials >= 0.8, "Your strategy does not win enough"
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
      >>> import random
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
