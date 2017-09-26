test = {
  'name': 'reflexive_strategy',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> agents.history = History.History(agents.rock_strategy, agents.reflexive_strategy)
          >>> assert round(Simulator.simulator(agents.rock_strategy, agents.reflexive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
          >>> agents.history = History.History(agents.scissors_strategy, agents.reflexive_strategy)
          >>> assert round(Simulator.simulator(agents.scissors_strategy, agents.reflexive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> trials = 1000
          >>> wins = 0
          >>> for _ in range(trials):
          ...    rates = np.random.random(3)
          ...    rates /= rates.sum()
          ...    strategy1 = agents.triple_biased_strategy(rates[0], rates[1], rates[2])
          ...    strategy2 = agents.reflexive_strategy
          ...    agents.history = History.History(strategy1, strategy2)
          ...    results = Simulator.simulator(strategy1, strategy2, history_storage = agents.history, simulation_count = 1000, silent = True)
          ...    if results[1] > results[0]:
          ...        wins += 1
          ...    if results[0] - results[1] > 0:
          ...        assert results[0] - results[1] < 0.1
          >>> assert wins/trials > 0.9, "Your strategy does not win often enough"
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
      >>> import numpy as np
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
