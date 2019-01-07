from neuron import h, gui

#### Here we load the definition of a cell. Ignore this part...
import os
this_dir, this_filename = os.path.split(__file__)
load_model_hoc = lambda x: h.xopen(os.path.join(this_dir, x))
load_model_hoc('ri18geo.hoc')
load_model_hoc('ri18init_passive.hoc')
####


## We set the parameters with two different choices
h.init_params()
h.insert_pass()

### Here we use uniform Rm
h.init_pass1()

h.v_init = -76.0


def distance_from_soma(segname_or_pointprocess):
    """returns the distance of the segment from the center of the soma.
    segname_or_pointprocess should be either a string that follows
    the convention how the NEURON refers to a point in a segment, e.g.,
    'dend1[802](0.5)' or a point process"""
    if type(segname_or_pointprocess)==str:
        segname = segname_or_pointprocess
    elif 'loc' in segname_or_pointprocess.__dict__:
        segname = str(segname_or_pointprocess.get_segment())
    else:
        raise RuntimeError('Input should be a segment name or point process.')

    h.dend1[21].push() # dend1[21] is an actual center of the soma.
    h.distance()
    h.pop_section()
    secname, xstr = segname.split('(')
    x = float(xstr.replace(')', ''))
    sec = eval('h.' + secname)
    sec.push()
    d = h.distance(x)
    h.pop_section()
    return d

def move_electrode_to(electrode, segment):
    h.push_section(str(segment.sec))
    electrode.loc(segment.x)
    h.pop_section()
