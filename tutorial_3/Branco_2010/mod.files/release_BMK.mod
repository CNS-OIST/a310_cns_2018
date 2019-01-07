TITLE transmitter release

COMMENT
-----------------------------------------------------------------------------

 
   References:

   Destexhe, A., Mainen, Z.F. and Sejnowski, T.J. Synthesis of models for
   excitable membranes, synaptic transmission and neuromodulation using a 
   common kinetic formalism, Journal of Computational Neuroscience 1: 
   195-230, 1994.

   Destexhe, A., Mainen, Z.F. and Sejnowski, T.J.  Kinetic models of 
   synaptic transmission.  In: Methods in Neuronal Modeling (2nd edition; 
   edited by Koch, C. and Segev, I.), MIT press, Cambridge, 1996.

  Written by Bjoern Kampa, 2004

-----------------------------------------------------------------------------
ENDCOMMENT


INDEPENDENT {t FROM 0 TO 1 WITH 1 (ms)}

NEURON {
	SUFFIX rel
	RANGE T, del, dur, amp
}

UNITS {
	(mM) = (milli/liter)
}

PARAMETER {
	del (ms)
	dur (ms)	<0,1e9>
	amp (mM)
}

ASSIGNED { T (mM)
}


INITIAL {
	T = 0
}

BREAKPOINT {
	at_time(del)
	at_time(del+dur)

	if (t < del + dur && t > del) {
		T = amp
	}else{
		T = 0
	}
}


