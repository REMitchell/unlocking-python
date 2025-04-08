import logging

logger = logging.getLogger(__name__)


class TreeStatus:
    STANDING = 'standing'
    CUT = 'cut'


class TreeSpecies:
    DOUGLAS_FIR = 'Douglas Fir'
    WESTERN_HEMLOCK = 'Western Hemlock'
    SITKA_SPRUCE = 'Sitka Spruce'


class Tree:
    def __init__(self, species: str, height: int = 1):
        self.species = species
        if self.species not in [
            TreeSpecies.DOUGLAS_FIR,
            TreeSpecies.WESTERN_HEMLOCK,
            TreeSpecies.SITKA_SPRUCE,
        ]:
            logger.warning(f'Unknown tree species: {self.species}')

        self.status: str = TreeStatus.STANDING
        self.height = height

    def cut(self):
        self.status = TreeStatus.CUT
        self.height = 0

    def grow(self):
        if self.status == TreeStatus.STANDING:
            self.height += 1
