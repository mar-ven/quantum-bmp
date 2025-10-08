# A Grover-meets-Simon Approach to Match Vector Boolean Functions

Repository for the Grover-meets-Simon (GMS) algorithm for the Vector Boolean Matching Problem, which combines Grover's search algorithm with Simon's problem to match vector Boolean functions. Work published to the IEEE Transactions on Quantum Engineering 2025.

### Installation

To install the required packages, run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -U --no-deps -r requirements.txt
```

### Structure of this repo

The benchmarks folder contains the implementation of quantum oracles for Boolean circuits belonging to the [ISCAS 74X-Series]( 
https://tumbleweed.nu/r/iscas.restore/doc/trunk/index.html).

The code folder contains the source code for the Simon's and Grover-meets-Simon solvers for the Vector Boolean Matching Problem.

The test folder contains the Python scripts to run the experiments and collect results.

### How to run experiments

To run the experiments, you can use the provided scripts in the `test` directory. For example, to run the Simon algorithm tests, execute from the root directory:

for _n=4_:
```bash
PYTHONPATH=./ python test/test_simon_4.py
```

for _n=8_:
```bash
PYTHONPATH=./ python test/test_simon_8.py
```

To run the Grover-meets-Simon tests, execute from the root directory:

```bash
PYTHONPATH=./ python test/test_gms.py
```

Please notice: to compile against ibm_brisbane, you need to set the environment variable `qiskit_token` with your IBM Quantum API token. You can obtain this token from your IBM Quantum account.

### Credits

If you wish to use this work or our benchmark/source code, please cite the following paper(s):

```
@INPROCEEDINGS{10818143,
  author={Venere, Marco and Barenghi, Alessandro and Pelosi, Gerardo},
  booktitle={2024 IEEE 42nd International Conference on Computer Design (ICCD)}, 
  title={A Quantum Method to Match Vector Boolean Functions using Simon's Solver}, 
  year={2024},
  volume={},
  number={},
  pages={542-549},
  keywords={Computers;Boolean functions;Costs;Qubit;Logic gates;Vectors;Complexity theory;Proposals;Quantum circuit;Standards;Boolean Matching;NPN Equivalence;Electronic Design Automation;Quantum Computing},
  doi={10.1109/ICCD63220.2024.00089}}

@ARTICLE{11108706,
  author={Venere, Marco and Barenghi, Alessandro and Pelosi, Gerardo},
  journal={IEEE Transactions on Quantum Engineering}, 
  title={A Grover-Meets-Simon Approach to Match Vector Boolean Functions}, 
  year={2025},
  volume={6},
  number={},
  pages={1-14},
  keywords={Boolean functions;Vectors;Libraries;Logic gates;Time complexity;Quantum algorithm;Digital circuits;Benchmark testing;Polynomials;Integrated circuit interconnections;Electronic design automation (EDA);negation–permutation–negation equivalence (NPN-equivalence);quantum-aided Boolean matching},
  doi={10.1109/TQE.2025.3595275}}
```


