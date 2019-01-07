COMMENT

Written by Sungo Hong, CNS Unit, OIST, Japan
March 2017

ENDCOMMENT

NEURON {
	POINT_PROCESS CCSTDPSyn
	NONSPECIFIC_CURRENT i
	RANGE u1, u2, u3
	RANGE tau1, tau2, taux, A1, A2, theta1, theta2, spikewidth, wEmin, wEmax
	GLOBAL factor
}

UNITS {
      (nA) = (nanoamp)
      (mV) = (millivolt)
      (uS) = (microsiemens)
}

PARAMETER {
	e = 0	(mV)
	tau_open = 0.1 (ms) <1e-9,1e9>
	tau_close = 1.5 (ms) <1e-9,1e9>

	tau1 = 14 (ms)      : time constant for filtering membrane potential
	tau2 = 4 (ms)       : time constant for post filter for potentiation
	taux = 10 (ms)      : time constant for low-pass r
	A1 = 1e-7 (/mV)     : amplitude for depression
	A2 = 3e-9 (/mV/mV)  : amplitude for potentiation
	theta1 = -64.9 (mV) : threshold for depression
	theta2 = -35 (mV)   : threshold for potentiation

	spikewidth = 7 (ms) : how long an AP will shunt an EPSP

	wEmin = 0
	wEmax = 0.1
}

ASSIGNED {
	v (mV)
	i (nA)
	g (uS)

	factor
}

STATE {
	A (uS)
	B (uS)

	u1 (mV)
	u2 (mV)
	u3
}

INITIAL {
	LOCAL tp
	if (tau_open/tau_close > 0.9999) {
		tau_open = 0.9999*tau_close
	}
	if (tau_open/tau_close < 1e-9) {
		tau_open = tau_close*1e-9
	}

	tp = (tau_open*tau_close)/(tau_close - tau_open) * log(tau_close/tau_open)
	factor = -exp(-tp/tau_open) + exp(-tp/tau_close)
	factor = 1/factor


	A = 0
	B = 0
	g = 0

	u1 = v
	u2 = v
	u3 = 0

	: Start monitoring a postsynaptic spike
	net_send(0, 1)
}

BREAKPOINT {
	SOLVE state METHOD cnexp

	g = B - A
	i = g*(v - e)
}

DERIVATIVE state {
	A' = -A/tau_open
	B' = -B/tau_close

	u1' = (v-u1)/tau1   : u_- low-pass filtered v
	u2' = (v-u2)/tau2   : u_+ low-pass filtered v
	u3' = A2*rectified(v-theta2)*rectified(u2-theta1) : potentiation eligibility
}

NET_RECEIVE(w (uS), wE (uS), x, tpre (ms)) {
	INITIAL { wE=w x=0 tpre=-1e9}

	if (flag==0) { : Presynaptic spike
		printf("entry flag=%g t=%g wE=%g x=%g tpre=%g\n", flag, t, wE, x, tpre)

		: Activate the synapse
		A = A + wE*factor
		B = B + wE*factor
		:printf("entry flag=%g t=%g A=%g B=%g\n", flag, t, A, B)

		: Presynaptic spike induces depression
		printf("DEP t=%g wE=%g dwE=%g x=%g tpre=%g\n", t, wE, -A1*rectified(u1-theta1), x, tpre)
		wE = wE - A1*rectified(u1-theta1)
		: But not below wEmin
		if (wE<wEmin) { wE = wEmin }

		: Accumulate presynaptic spike count
		x = exp(-(t-tpre)/taux)*x + 1
		tpre = t
		: printf("Spike count update t=%g wE=%g x=%g tpre=%g\n", t, wE, x, tpre)
	} else if (flag==2) { : Postsynaptic spike begin
		:printf("entry flag=%g t=%g\n", flag, t)
		: Wait until the spike ends
		WATCH (v<theta2) 3

	} else if (flag==3) { : Postsynaptic spike end

		:printf("entry flag=%g t=%g\n", flag, t)

		: Potentiate all netcons now
		FOR_NETCONS(wi, wEi, xi, tprei) {
			if (t-tprei > spikewidth) { : An EPSP shunted by an AP has no effect
				: Otherwise potentiate synapses
				printf("POT t=%g wE=%g dwE=%g, x=%g tpre=%g\n", t, wEi, u3*xi*exp(-(t-tprei-spikewidth)/taux), xi, tprei)
				wEi = wEi + u3*xi*exp(-(t-tprei-spikewidth)/taux)
			}
			: unless they are not too stong
			if (wEi>wEmax) { wEi = wEmax}
		}

		: Reset acculumated potentiation
		u3 = 0

		: Everything back to normal
		net_send(0, 1)

	} else {
		: watch for a postsynaptic spike
		WATCH (v>theta2)  2
	}
}

UNITSOFF
FUNCTION rectified (v (mV)) {
	if (v>0) {
		rectified = v
	} else {
		rectified = 0
	}
}

UNITSON
