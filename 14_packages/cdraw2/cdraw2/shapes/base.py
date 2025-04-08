import time
from tqdm import tqdm

class Shape:
    def __init__(self):
        pass

    def draw(self, printer=print):
        raise NotImplementedError

    def do_loading(self):
        messages = [
            'loading hashes...          ',
            'configuring angles...      ',
            'queuing euclidean axioms...',
            'defragging edges...        ',
            'Done!                      ',
        ]
        loading_bar = tqdm(range(1, 101))
        for i in loading_bar:
            m = messages[int(i / 25)]
            loading_bar.set_description(m)
            time.sleep(0.02)
