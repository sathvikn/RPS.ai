test = {
	'name': 'deterministic strategy',
	'suites': [
	{ 
	'cases' : [
	{
		'code': r"""
        >>> agents.history = History.History(agents.rock_strategy, agents.predictive_strategy)
        >>> assert round(Simulator.simulator(agents.rock_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
        """
      },]
  'cases' : [{
    'code': r"""
        agents.history = History.History(agents.paper_strategy, agents.predictive_strategy)
        assert round(Simulator.simulator(agents.paper_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
    """
  }],
  'cases' : [{
    'code' : r"""
        >>> agents.history = History.History(agents.scissors_strategy, agents.predictive_strategy)
        >>> assert round(Simulator.simulator(agents.paper_strategy, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)[1]) == 1
    """
  }]
      'cases': [
      {
      'code' : r"""
      	>>> trials = 1000
        >>> wins = 0
        >>> for _ in range(trials):
            ... test_length = random.randint(2, 10)
            ... test_list = [random.randint(0, 2) for _ in range(test_length)]
            ... deterministic = deterministic_list(test_list)
            ... agents.history = History.History(deterministic, agents.predictive_strategy)
            ... result = Simulator.simulator(deterministic, agents.predictive_strategy, history_storage = agents.history, simulation_count = 1000, silent = True)
            ... if result[0] < result[1]:
                ... wins += 1
        >>> assert wins / trials >= 0.8, "Your strategy does not win enough"
        """
      }]
	}
	]
}