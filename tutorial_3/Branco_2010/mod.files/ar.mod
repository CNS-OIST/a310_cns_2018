TITLE anomalous (inward) rectifying membrane

COMMENT
	Phenomenological model of a anomalous rectifying membrane using 
	a quadratic approximation of the subthreshold VI-relationship.
	
	Implemented by Fritjof Helmchen, MPI for Medical Research, Heidelberg
	Dec. 2004

ENDCOMMENT

UNITS {
         (mV) = (millivolt)
         (mA) = (milliamp)
	   (S)  = (siemens)
}

INDEPENDENT {v FROM -100 TO 50 WITH 50 (mV)}

NEURON {
         SUFFIX ar
         NONSPECIFIC_CURRENT i
         RANGE g, e, c
}

PARAMETER {
         g0 = .0001      (S/cm2)       <0,1e9>
         e = -75 	  	 (mV)
         c = 1000000 	 (cm4 ohm2/mV)
}
  
ASSIGNED { i (mA/cm2) g (S/cm2) }

BREAKPOINT {
	if (c==0) {
		g = g0
		i = g0*(v-e)
	} else {
		g = 1/sqrt(1/g0^2+4*c*(v-e)) 
		i = ( -1/g0 + 1/g)/(2*c)
	}
}
