#include <pybind11/pybind11.h>
#include "../include/LFMF.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;

PYBIND11_MODULE(PyLFMF, m)
{

	m.doc()  = R"V0G0N(
Low Frequency / Medium Frequency (LF/MF) Propagation Model
==========================================================

INPUTS:

Variable	Type	Units	Limits			Description
--------------|--------|-------|-----------------------|--------------------------------|
h_tx__meter	double	meter	0 <= h_tx__meter <= UB	Height of the transmitter	|
h_rx__meter	double	meter	0 <= h_rx__meter <= UB	Height of the receiver		|
f__mhz		double	MHz	0.01 <= f__mhz <= 30	Frequency			|
P_tx__watt	double	Watt	0 < P_tx__watt		Transmitter power		|
N_s		double	N-Units	250 <= N_s <= 400	Surface refractivity		|
d__km		double	km	0 < d__km		Path distance			|
epsilon		double		1 <= epsilon		Relative permittivity		|
sigma		double	S/m	0 < sigma		Conductivity			|
pol		int					Polarization			|
								0 = Horizontal		|
								1 = Vertical		|
----------------------------------------------------------------------------------------|
UB - upper bound is calculated according to the Handbook on Ground Wave Propagation	|
     published by The International Telecommunication Union (ITU):			|
     For epsilon << 60 * sigma * lambda: UB = 1.2 * sigma^{1/2} * lambda^{3/2}          |
----------------------------------------------------------------------------------------|




OUTPUTS:

Variable	Type	Units		Description
---------------|-------|---------------|------------------------------------------------|
A		double	dB		Basic transmission loss				|
E		double	dB(uV/m)	Electrice field strength			|
P		double	dBm		Received power					|
method		int			Solution method					|
					0 = Flat earth with curve correction		|
					1 = Residue series				|
status		int			0 = SUCCESS					|
					2000 = Upper bound for h_tx__meter is used	|
					2001 = Upper bound for h_rx__meter is used	|
					2002 = Upper bound for h_tx__meter is used	|
					1000 = TX terminal height is out of range	|
					1001 = RX terminal height is out of range	|
					1002 = Frequency is out of range		|
					1003 = Transmit power is out of range		|
					1004 = Surface refractivity is out of range	|
					1005 = Path distance is out of range		|		
					1006 = Epsilon is out of range			|
					1007 = Sigma is out of range			|
					1008 = Invalid value for polarization		|
----------------------------------------------------------------------------------------|)V0G0N";

		
	m.def("run", &LFMF);

	py::class_<Result>(m, "Result")
		.def_readwrite("A", &Result::A_btl__db)
		.def_readwrite("E", &Result::E_dBuVm)
		.def_readwrite("P", &Result::P_rx__dbm)
		.def_readwrite("method", &Result::method)
		.def_readwrite("status", &Result::validation);
        m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);

}


