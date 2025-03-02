# Problem

Given a list of tuples like this:

	[
		('a', 'b'),
		('a', 'c'),
	]

In which ('a', 'b') means node a depends on node b. Resolve the
dependencies and output a list of build order. In the case above, the output can be either one of the following lists:

    ['b', 'c', 'a']
    ['c', 'b', 'a']

# Solution 1: Using networkx

No interviewer will accept this solution because it is too easy. However, it demonstrate the right tool for the job. In this solution, we build a directed graph where as the above list becomes:

    [b] -> [a] <- [c]

Once we have this graph, we can call `topological_sort` to get the correct answer.

# Solution 2: Homemade, Using dict

In this solution, we create a dictionary `dependency` whose keys are the nodes and values are the set of nodes which must be built before building the key node. For the above list, our dictionary looks like:

    {
        'a': set(['b', 'c']),  # a depends on b and c
        'b': set(),            # b has no dependency
        'c': set (),           # c has no dependency
    }

To create a build order list, we look in the dictionary for those nodes that has no dependency (in this case, b and c). For those nodes, we remove them from the dictionary and put them into the `build_order` list. After that, we remove them from the values of the dictionary.

# Installation

For `networkx`:

    pip install networkx

or

    pip install -r requirements.txt

