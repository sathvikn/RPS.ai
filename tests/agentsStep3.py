test = {
  'name': 'deterministic_strategy',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> strat = agents.deterministic_strategy()
          >>> deterministic_order = [0, 1, 2, 1, 0]
          >>> simple_test_results = []
          >>> for _ in range(len(deterministic_order)):
          ...    simple_test_results.append(strat())
          >>> assert simple_test_results == deterministic_order, "Failed simple test"
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> deterministic_order = [0, 1, 2, 1, 0]
          >>> for _ in range(1000):
          ...    random_test_results = []
          ...    strategy = agents.deterministic_strategy()
          ...    turns = random.randint(1, 1000)
          ...    for _ in range(turns):
          ...        random_test_results.append(strategy())
          ...        answer = deterministic_order * (turns // len(deterministic_order))
          ...    for i in range(turns - len(answer)):
          ...        answer.append(deterministic_order[i])
          ...    assert answer == random_test_results, "Deterministic strategy does not match expected output"
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
