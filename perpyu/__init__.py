name = "perpyu"

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    __version__ = f.read().strip()

from . import pytorch
from . import tensorflow 