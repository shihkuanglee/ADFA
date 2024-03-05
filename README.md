## Introduction

#### This repository provides the software implementation of developed ADFA, MDFA and CQA methods in this study:

[Arbitrary Discrete Fourier Analysis and Its Application in Replayed Speech Detection](https://arxiv.org/abs/2403.01130)

## Dependencies
```
pip install -r requirements.txt
```

## Usage

Add submodule to your repository:
```
git submodule add https://github.com/shihkuanglee/ADFA.git
```

Then the library is now able to be import:
```
from ADFA.adfa import adfa_arb, mdfa_arb, cqa_arb
```

## Example

https://github.com/shihkuanglee/RD-LCNN/

## Citation Information

Shih-Kuang Lee, “Arbitrary Discrete Fourier Analysis and Its Application in Replayed Speech Detection,” arXiv preprint arXiv:2403.01130, 2024.
```bibtex
@article{lee2024arbitrary,
  title={{Arbitrary Discrete Fourier Analysis and Its Application in Replayed Speech Detection}},
  author={Shih-Kuang Lee},
  journal={arXiv preprint arXiv:2403.01130},
  year={2024}}
```

## Licensing

This repository is licensed under the [ISC License](https://github.com/shihkuanglee/ADFA/blob/main/LICENSE.md).

This repository includes modified codes from [SciPy](https://github.com/scipy/scipy).
