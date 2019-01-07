"""

thalamocortical_neuron.py

Adapted from:
[Thalamocortical Relay cell under current clamp in high-conductance state (Zeldenrust et al 2018)
](https://senselab.med.yale.edu/modeldb/ShowModel.cshtml?model=232876)

Reference: Zeldenrust F, Chameau P, Wadman WJ (2018) Spike and burst coding in thalamocortical relay cells. PLoS Comput Biol 14:e1005960.


Written by Sungho Hong, Computational Neuroscience Unit, OIST, Japan
April 1, 2017

"""


from cell_template import Cell
from neuron import h

h.celsius = 34
h.v_init = -74


class TCN(Cell):
    def create_sections(self):
        self.soma = h.Section(name='soma', cell=self)
        self.dend1 = [h.Section(name=('dend1[{}]'.format(i)), cell=self) for i in range(2)]

    def build_topology(self):
        self.dend1[0].connect(self.soma, 1)
        self.dend1[1].connect(self.dend1[0], 1)

    def build_subsets(self):
        self.allsec = h.SectionList()
        self.allsec.wholetree(self.soma)

    def define_geometry(self):
        self.soma.nseg = 1
        self.soma.L = 38.42
        self.soma.diam = 26
        h.pt3dclear(sec=self.soma)
        h.pt3dadd(0, 0, 0, 26, sec=self.soma)
        h.pt3dadd(0, 38.42, 0, 26, sec=self.soma)
        h.define_shape()

        self.dend1[0].nseg = 1
        h.pt3dclear(sec=self.dend1[0])
        h.pt3dadd(0, 38.42, 0, 10.28, sec=self.dend1[0])
        h.pt3dadd(0, 50.91, 0, 10.28, sec=self.dend1[0])
        h.define_shape()

        self.dend1[1].nseg = 1
        h.pt3dclear(sec=self.dend1[1])
        h.pt3dadd(0, 50.91, 0, 8.5, sec=self.dend1[1])
        h.pt3dadd(0, 135.58, 0, 8.5, sec=self.dend1[1])
        h.define_shape()

    def define_biophysics(self):
        corrD = 7.954       # dendritic surface correction (estimated by fitting voltage-clamp traces)
        corrR = 0.75        # make R 25% higher, so g=1/1.25=0.8, do also for C for correction RC time
        corrC = 0.9         # make RC time smaller

        G_pas = corrR*3.79e-5
        E_pas = -73         # to fit current-clamp data (was -71 to -73)
        E_pas = -76.5       # within 3 mV error
        C_m   = corrC*corrR*0.88

        for sec in self.allsec:
            sec.insert("pas")
            sec.g_pas = G_pas * corrD
            sec.e_pas = E_pas
            sec.cm = C_m * corrD
            sec.Ra = 173

        self.soma.g_pas = G_pas
        self.soma.cm = C_m

        self.soma.insert("hh2")         # insert fast spikes
        self.soma.ena = 50
        self.soma.ek = -100
        self.soma.vtraub_hh2 = -52
        self.soma.gnabar_hh2 = 0.1
        self.soma.gkbar_hh2 = 0.1

        self.soma.insert("iL")          # insert IL (high-threshold calcium)
        self.soma.pcabar_iL = 0.00005

        self.soma.insert("iC")          # IKC (calcium-dependent potassium)
        self.soma.gkbar_iC = 0.001

        for sec in self.allsec:

            # T-type calcium channel, correctly based on the GHK equation
            sec.insert("itGHK")         # T-current everywhere
            sec.cai = 2.4e-4
            sec.cao = 2
            sec.eca = 120
            sec.shift_itGHK = -1        # screening charge shift + 3 mV error
            sec.pcabar_itGHK = corrD * 0.0002 # will be overwritten by self.localize
            sec.qm_itGHK = 2.5
            sec.qh_itGHK = 2.5

            # Here we insert a non-functional "ohmic" T-type calcium channel
            sec.insert("itOhmic")
            sec.gcabar_itOhmic = 0.0

            # Calcium diffusion/buffering
            sec.insert("cad")           # calcium diffusion everywhere
            sec.depth_cad = 0.1 * corrD
            sec.kt_cad = 0              # no pump
            sec.kd_cad = 1e-4
            sec.taur_cad = 5
            sec.cainf_cad = 2.4e-4

            sec.insert("iar")           # Ih everywhere
            sec.ghbar_iar = 1.3e-04

        self.localize(1.7e-5, corrD*9.5e-5)

    def localize(self, x1, x2):
        self.soma.pcabar_itGHK = x1	     # soma
        self.dend1[0].pcabar_itGHK = x1  # proximal
        self.dend1[1].pcabar_itGHK = x2  # distal

    def create_synapses(self):
        # self.synlist
        self.synlist.append(h.Exp2Syn(self.dend1[0](0.5))) # An excitatory synapse
        self.synlist[-1].e = 0
        self.synlist[-1].tau1 = 0.25
        self.synlist[-1].tau2 = 3

        self.synlist.append(h.Exp2Syn(self.dend1[0](0.5))) # An inhibitory synapse
        self.synlist[-1].e = -80
        self.synlist[-1].tau1 = 2
        self.synlist[-1].tau2 = 10

