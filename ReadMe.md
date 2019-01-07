# A310 Computational Neuroscience - Okinawa Institute of Science and Technology, 2017/2018
This repository is for modeling practice materials and homework of Computational Neuroscience course at Okinawa Institute of Science and Technology in 2018.

In modeling classes, we focus on implementing physiological concepts about how neural systems function in computer simulations, which will help us understand how diverse phenomena in real neural systems arise from the underlying principles. We will mainly use the [NEURON](https://www.neuron.yale.edu/neuron/) simulation platform, which uses [Python](https://www.python.org) programming language for interface. We will also cover some basic analysis techniques for neural data, but most of our focus will be constructing models and running their simulations.


## Software
We use NEURON 7.5 with Python 3.6. **We recommend using our [Docker](https://en.wikipedia.org/wiki/Docker_(software)) container:** NEURON has non-trivial dependency on Python, the C++ compiler, and other libraries (e.g., MPI), which is quite challenging for fist-time users to configure correctly. **See the [installation guide](./docker/ReadMe.md) for how to install and use the Docker and container**. If you do not want to use this, we recommend compiling the source by following the [instruction](https://www.neuron.yale.edu/neuron/download/getstd) carefully. We discourage installation via binary installers, which has been a source of frustration in the past.


## Schedule of modeling classes and homework dues

### [Modeling class: introduction](https://github.com/CNS-OIST/a310_cns_2018/tree/master/tutorial_1) — Jan 18, 2018

In our first modeling session, we will cover the very basic of Python programming language and model/simulation construction by using NEURON.

#### [Homework #1](https://github.com/CNS-OIST/a310_cns_2018/tree/master/homework_1) — due: Feb 7, 2018 (extended)

Our first homework is about developing skills in basic Python and handling numerical data in Python and NEURON.

### [Modeling class #1](https://github.com/CNS-OIST/a310_cns_2018/tree/master/tutorial_2) — Feb 8, 2018

In the second modeling class, we will go through how to add synapses on neurons and how to activate them by connecting presynaptic neurons or artificial spike generators --- a neural network!

#### [Homework #2](https://github.com/CNS-OIST/a310_cns_2018/tree/master/homework_2) — due: Feb 28, 2018

The second homework is mainly about intergration and transfer of synaptic inputs.

### [Modeling class #2](https://github.com/CNS-OIST/a310_cns_2018/tree/master/tutorial_3) — Mar 1, 2018

The third modeling class will be about active membrane and intracellular mechanisms.

#### [Homework #3](https://github.com/CNS-OIST/a310_cns_2018/tree/master/homework_3) — due: March 26, 2018

The third homework is about active ion channels and their role in spike initiation.

### [Modeling class #3](https://github.com/CNS-OIST/a310_cns_2018/tree/master/tutorial_4) — Mar 22, 2018

The fourth modeling class will focus more on active mechanisms, and also building a network simulation.

### Modeling exercises feedback - March 29, 2018 (Cancelled)

~~In this feedback session, we will discuss about various issues and gotchas in model building.~~

### [Modeling class #4](https://github.com/CNS-OIST/a310_cns_2018/tree/master/tutorial_5) — April 5, 2018  

In our final session, we will work more on network simulations.

#### [Homework #4](https://github.com/CNS-OIST/a310_cns_2018/tree/master/homework_4) — due: April 23, 2018

The fourth homework is about modeling calcium mechanisms and network simulations.

---
_Written by Sungho Hong, Computational Neuroscience Unit, Okinawa Institutes of Science and Technology_

_January 2018_
