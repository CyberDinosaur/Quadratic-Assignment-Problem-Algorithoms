## Quadratic Assignment Problem

> by yitong - 2023.07

Implementations of iterated local search (ILS), improved hybrid genetic algorithm (IHGA), tabu search (TS) to solve quadratic assignment problem (QAP).

### File Structure:

- classes: modeling classed.
- paqdata: QAP test data downloaded from [QAPLIB](https://www.opt.math.tugraz.at/qaplib/inst.html).
- utils: Some basic scripts.
- pic: Saved convergence figures.
- main.py

### Requirements:

* Python: 3.10.6
* altair: 5.0.1
* pandas: 2.0.2
* numpy: 1.25.0
* plotly: 5.15.0

### To run this project:

* `make clean`: Clean all the results from last run.
* `make run`: Directly run the main.py according to its default settings.
* `make ils/ts/ga`: You can modify the MAKEFIlE to change the test file you want to perform on. By doing this and executing this command, the according algorithm will be performed on the specified test file.
* or...you can choose to compile the scripts manually.

### Ref:

https://github.com/wzieba/QAP-Genetic-Algorithm

https://github.com/BlackMooth/Quadratic-Assignment-Problem

https://github.com/sidneyrachel/quadratic-assignment-problem#iterated-local-search

https://github.com/jjosenaldo/QAP-algorithms
