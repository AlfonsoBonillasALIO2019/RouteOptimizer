""" This file is a test script """

import itertools as it
from core_search.entities import *
from core_search.state import *
from core_search.search import *

# First build the locations
shovel1 = Location("S1", 2)
shovel2 = Location("S2", 2)
loader1 = Location("L1", 2)
loader2 = Location("L2", 2)
waste_dump = Location("W", 2)
crusher = Location("C", 2)
garage = Location("garage", 21)

# Build the mine configuration
connections = [
    (garage, loader1),
    (garage, loader2),
    #(loader1, garage), Once per shift, only applicable if truck doesn't have load
    #(loader2, garage), Once per shift, only applicable if truck doesn't have load
    #(waste_dump, garage), Once per shift
    (garage, shovel1),
    (garage, shovel2),
    (waste_dump, loader1),
    (loader1, waste_dump),
    (waste_dump, shovel1),
    (shovel1, waste_dump),
    (waste_dump, shovel2),
    (shovel2, waste_dump),
    (crusher, shovel1),
    (shovel1, crusher),
    (crusher, shovel2),
    (shovel2, crusher),
    (crusher, loader2),
    (loader2, crusher)
]

config = MineConfiguration(connections)

# Generate the trucks
trucks = [Truck("truck_%i" % i, c) for i, c in zip(range(1, 22), it.cycle([100]))]


# Build some fake demands
demands = {
    (shovel1, crusher): 8000,
    (shovel2, crusher): 12000,
    (loader1, crusher): 4000,
    (shovel1, waste_dump): 16000,
    (shovel2, waste_dump): 20000,
    (loader1, waste_dump): 10000,
}

num_segments = 48

# Create the initial state
initial_state = FleetState(config, trucks, demands, num_segments)

# Let it run!
searcher = UniformCostSearch(initial_state)

solution = searcher.solve()

pass
