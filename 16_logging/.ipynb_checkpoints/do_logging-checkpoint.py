from lumberjack.forest import Forest
from lumberjack.tree import Tree, TreeSpecies
from lumberjack.lumberjack import Lumberjack

forest = Forest(
    [
        Tree(TreeSpecies.DOUGLAS_FIR),
        Tree(TreeSpecies.SITKA_SPRUCE),
        Tree(TreeSpecies.WESTERN_HEMLOCK),
        Tree("Horse Chestnut"),
    ]
)

alice = Lumberjack("Alice", forest)
bob = Lumberjack("Bob", forest)
# Grow the forest before cutting
[forest.grow() for _ in range(0, 30)]
alice.cut_trees(num_trees=2, min_height=20)
bob.cut_trees(num_trees=2, min_height=40)
