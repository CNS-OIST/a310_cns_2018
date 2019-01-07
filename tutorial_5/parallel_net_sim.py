import numpy as np
from neuron import h

# Variable step controller to speed up simulation
cvode = h.CVode()
cvode.active(1)

from cell_template import Cell
class MorrisLecar(Cell):

    def __init__(self, i):
        super().__init__()

        self.stim = []
        self.stim.append(h.NetStimFD(self.soma(0.5)))
        self.stim[-1].interval = 3
        self.stim[-1].noise = 1
        self.stim[-1].start = 0
        self.stim[-1].duration = 7
        self.stim[-1].seed(i+1223)

        self.stim.append(h.NetCon(self.stim[0], self.synlist[0]))
        self.stim[-1].weight[0] = 5e-3

    def create_sections(self):
        """create a soma"""
        self.soma = h.Section(name="soma", cell=self)

    def build_topology(self):
        pass # single compartment

    def build_subsets(self):
        pass # single compartment

    def define_geometry(self):
        self.soma.L = 15
        self.soma.diam = 15

    def define_biophysics(self):
        h.v_init = -65
        self.soma.insert('ml')

    def create_synapses(self):
        self.synlist.append(h.Exp2Syn(self.soma(0.5))) # Excitatory
        self.synlist[-1].tau2 = 0.1
        self.synlist[-1].tau2 = 2.0
        self.synlist[-1].e = 0

        self.synlist.append(h.Exp2Syn(self.soma(0.5))) # Inhibitory
        self.synlist[-1].e = -75
        self.synlist[-1].tau1 = 0.1
        self.synlist[-1].tau2 = 2.0


Ncells = 2000                    # Number of cells
Nexc = int((Ncells/5)*4)         # Excitatory cells = 80%
Ninh = int(Ncells/5)             # Inhibitory cells = 20%
nexcpre = int(Nexc*0.1)
ninhpre = int(Ninh*0.1)

print(Nexc, Ninh, nexcpre, ninhpre)

from net_manager import ParallelNetManager
pnm = ParallelNetManager(Ncells)

for i in range(Ncells):
    if pnm.gid_exists(i):
        pnm.register_cell(i, MorrisLecar(i))

# gexc = 2e-3   # g_exc = 1.5 nS
# # ginh = 2.5*gexc   # g_inh = 6.2 g_exc
# ginh = 2.3*gexc   # g_inh = 6.2 g_exc

gexc = 30e-3/2   # g_exc = 1.5 nS
# ginh = 2.5*gexc   # g_inh = 6.2 g_exc
ginh = 23*gexc/2   # g_inh = 6.2 g_exc

for i in pnm.gidlist:
    exc_pre = np.random.randint(0, Nexc, nexcpre)     # Randomly choose 10% of the exc cells
    inh_pre = np.random.randint(Nexc, Ncells, ninhpre) # Randomly choose 10% of the inh cells

    for k in exc_pre:
        if i!=k:  # No self-connection
            pnm.nc_append(k, i, 0, gexc, 0.1, thresh=0)

    for k in inh_pre:
        if i!=k:  # No self-connection
            pnm.nc_append(k, i, 1, ginh, 0.1, thresh=0)

pnm.set_maxstep(100)
pnm.want_all_spikes()
pnm.set_output_filename('spikes.dat')

h.tstop = 400
h.init()
pnm.run()

h.quit()