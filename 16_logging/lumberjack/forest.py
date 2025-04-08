import logging
from lumberjack.tree import Tree

logger = logging.getLogger(__name__)


class Forest:
    def __init__(self, trees):
        self.trees = trees
        logger.info(f'Initialized forest with {len(self.trees)} trees')

    def grow(self):
        [t.grow() for t in self.trees]

    def plant(self, species):
        self.trees.append(Tree(species))
