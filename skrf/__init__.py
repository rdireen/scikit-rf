'''
skrf is an object-oriented approach to microwave engineering,
implemented in Python. 
'''
# Python 3 compatibility
from __future__ import absolute_import, print_function, division
from six.moves import xrange

# Global functions for setting alternative Network overloaded operators switch
# this will change the behavior of *, +, and | so that they work with two-port
# Network algebra
import sys
this = sys.modules[__name__]
this.skrf_alt_ops = False
def alternative_ops(value = True):
    this.skrf_alt_ops = value

def is_alt_ops():
    return this.skrf_alt_ops


__version__ = '0.15.4'
## Import all  module names for coherent reference of name-space
#import io



from . import frequency
from . import network
from . import noisyNetwork
from . import networkSet
from . import media
from . import circuit
from . import multiNoisyNetworkSystem

from . import calibration
# from . import plotting
from . import mathFunctions
from . import tlineFunctions
from . import taper
from . import constants
from . import util
from . import io
from . import instances
from . import noisyComponents


# Import contents into current namespace for ease of calling
from .frequency import *
from .network import *
from .noisyNetwork import *
from .networkSet import *
from .multiNoisyNetworkSystem import *
from .calibration import *
from .util import *
from .circuit import *
# from .plotting import  *
from .mathFunctions import *
from .tlineFunctions import *
from .io import * 
from .constants import * 
from .taper import * 
from .instances import * 

# Try to import vi, but if except if pyvisa not installed
try:
    import vi
    from vi import *
except(ImportError):
    pass

# try to import data but if it fails whatever. it fails if some pickles 
# dont unpickle. but its not important
try:
    from . import data
except:
    pass 



## built-in imports
from copy import deepcopy as copy


## Shorthand Names
F = Frequency
N = Network
NS = NetworkSet
C = Circuit
lat = load_all_touchstones
# saf  = save_all_figs
saf = None
stylely = None





def setup_pylab():
    try:
        import matplotlib
    except ImportError:
        print("matplotlib not found while setting up plotting")
        return False

    from . import plotting
    plotting.setup_matplotlib_plotting()

    global saf, stylely
    saf = plotting.save_all_figs
    stylely = plotting.stylely
    return True


def setup_plotting():
    plotting_environment = os.environ.get('SKRF_PLOT_ENV', "pylab").lower()

    if plotting_environment == "pylab":
        setup_pylab()
    elif plotting_environment == "pylab-skrf-style":
        if setup_pylab():
            stylely()
    # elif some different plotting environment
        # set that up

setup_plotting()
