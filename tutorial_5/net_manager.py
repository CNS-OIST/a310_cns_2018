from neuron import h


class NetManager:
    def __init__(self, N):
        self._N = N
        self.gidlist = []
        self.gid2cell = {}
        self.netcons = {}

    def register_cell(self, gid, cellobject):
        self.gid2cell[gid] = cellobject

    def gid_exists(self, gid):
        return (gid in self.gidlist)

    def nc_reset(self):
        self.netcons = {}

    def spike_record(self, gid, thresh=0):
        raise NotImplementedError("spike_record is not implemented.")

    def nc_append(self, src_gid, target_gid, synapse_id, weight, delay, thresh):
        raise NotImplementedError("nc_append is not implemented.")

    def run(self):
        raise NotImplementedError("run is not implemented.")

    def want_all_spikes(self, thresh=0):
        for gid in self.gidlist:
            self.spike_record(gid, thresh=thresh)

    def set_output_filename(self, outputfilename):
        self.output_file_name = outputfilename

    def write_spikes(self):
        raise NotImplementedError("write_spikes is not implemented.")


class SerialNetManager(NetManager):

    def __init__(self, N):
        super().__init__(N)
        self.nc_reset()
        self.gidlist = range(N)
        self.spikes = {}

    def spike_record(self, gid, thresh=0):
        self.spikes[gid] = (h.APCount(self.gid2cell[gid].soma(0.5)), h.Vector())
        self.spikes[gid][0].thresh = thresh
        self.spikes[gid][0].record(self.spikes[gid][1])

    def nc_append(self, src_gid, target_gid, synapse_id, weight, delay, thresh=0):
        self.netcons[(src_gid, target_gid, synapse_id)] = self.gid2cell[src_gid].connect2target(self.gid2cell[target_gid].synlist[synapse_id], thresh=thresh)
        self.netcons[(src_gid, target_gid, synapse_id)].weight[0] = weight
        self.netcons[(src_gid, target_gid, synapse_id)].delay = delay

    def run(self):
        h.run()
        self.gatherspikes()

    def gatherspikes(self):
        self.spikevec = []
        self.idvec = []
        for gid in self.spikes:
            sp1 = self.spikes[gid][1].to_python()
            self.idvec.extend([gid]*len(sp1))
            self.spikevec.extend(sp1)

    def write_spikes(self):
        with open(self.output_file_name, "w") as spk_file:
            for (t, i) in zip(self.spikevec, self.idvec):
                spk_file.write("{:.12f}, {:g}\n".format(t, i))  # timestamp, id



class ParallelNetManager(NetManager):
    def __init__(self, N):

        super().__init__(N)

        self.pc = h.ParallelContext()

        #### Round-robin counting.
        #### Each host as an id from 0 to pc.nhost() - 1.
        for i in range(int(self.pc.id()), self._N, int(self.pc.nhost())):
            self.gidlist.append(i)

        self.spikevec = h.Vector()
        self.idvec = h.Vector()

    def register_cell(self, gid, cellobject):
        if self.gid_exists(gid):
            super().register_cell(gid, cellobject)
            self.pc.set_gid2node(gid, int(self.pc.id()))
            nc = self.gid2cell[gid].connect2target(None)
            # nc.threshold = thresh
            self.pc.cell(gid, nc)

    def spike_record(self, gid, thresh=0):
        if self.pc.gid_exists(gid):
            self.pc.spike_record(gid, self.spikevec, self.idvec)
        else:
            raise RuntimeError("Cell {} does not exist in the node {}.".format(gid, self.pc.id()))

    def set_maxstep(self, n):
        self.pc.set_maxstep(n)

    def nc_append(self, src_gid, target_gid, synapse_id, weight, delay, thresh=0):
        if self.pc.gid_exists(target_gid):
            target = self.pc.gid2cell(target_gid)
            syn = target.synlist[synapse_id]
            self.netcons[(src_gid, target_gid, synapse_id)] = self.pc.gid_connect(src_gid, syn)
            self.netcons[(src_gid, target_gid, synapse_id)].weight[0] = weight
            self.netcons[(src_gid, target_gid, synapse_id)].delay = delay
            self.netcons[(src_gid, target_gid, synapse_id)].threshold = thresh
        else:
            raise RuntimeError("Cell {} does not exist in the node {}.".format(target_gid, self.pc.id()))

    def run(self):
        self.pc.psolve(h.tstop)
        self.write_spikes()
        self.pc.runworker()
        self.pc.done()

    def write_spikes(self):
        for i in range(int(self.pc.nhost())):
            self.pc.barrier()     # Sync all processes at this point
            if i==int(self.pc.id()):
                if i==0:
                    mode = 'w' # write
                else:
                    mode = 'a' # append
                with open(self.output_file_name, mode) as spk_file: # Append
                    for (t, i) in zip(self.spikevec, self.idvec):
                        spk_file.write("{:.12f}, {:g}\n".format(t, i)) # timestamp, id
        self.pc.barrier()
