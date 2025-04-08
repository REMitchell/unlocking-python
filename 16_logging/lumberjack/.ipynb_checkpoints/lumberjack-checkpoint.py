import logging
import sys

logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(asctime)s - Lumberjack %(ljname)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


class Lumberjack:
    def __init__(self, name, forest):
        self.name = name
        self.forest = forest
        self.logger = logging.LoggerAdapter(logger, {'ljname': self.name})
        self.logger.info('Initialized')

    def cut_trees(self, min_height=30, num_trees=5):
        self.logger.info(f'Cutting {num_trees} of height {min_height}')
        trees_cut = 0
        for t in self.forest.trees:
            if trees_cut >= num_trees:
                break
            if t.height >= min_height:
                t.cut()
                trees_cut += 1
        self.logger.info(f'Cut {trees_cut} trees')
