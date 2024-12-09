
MINED_OBJECTS = [
    "Iron Ore",
    "Copper Ore",
    "Coal",
    "Sulfur",
    "Bauxite",
    "Crude Oil"
]


class ProductionObject:
    name = None
    per_min = None
    mined = False

    def __init__(self, i_name, i_per_min):
        self.name = i_name
        self.per_min = i_per_min
        if i_name in MINED_OBJECTS:
            self.mined = True


class BaseProducer:
    outputs = None
    inputs = None

    def __init__(self, i_outputs, i_inputs):
        self.outputs = i_outputs
        self.inputs = i_inputs


class Producer:
    base = None
    multiplier = None

    def __init__(self, i_base, i_multiplier):
        self.base = i_base
        self.multiplier = i_multiplier

