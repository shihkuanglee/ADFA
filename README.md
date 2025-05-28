## Introduction

#### This repository provides the software implementation in this study:

[Advanced Signal Analysis in Detecting Replay Attacks for Automatic Speaker Verification Systems](https://arxiv.org/abs/2403.01130)

## Dependencies
```
pip install -r requirements.txt
```

## Usage

Add submodule to your repository:
```
git clone git@github.com:shihkuanglee/ADFA.git
git submodule add https://github.com/shihkuanglee/ADFA.git
```

Then the library is now able to be import:
```
from ADFA.adfa import aa_arb, ma_arb, cqa_arb
```

## Example

https://github.com/shihkuanglee/RD-LCNN/

## Citation Information

Lee Shih Kuang, “Advanced Signal Analysis in Detecting Replay Attacks for Automatic Speaker Verification Systems,” arXiv preprint arXiv:2403.01130, 2025.
```bibtex
@misc{lee2025adfa,
      title={Advanced Signal Analysis in Detecting Replay Attacks for Automatic Speaker Verification Systems}, 
      author={Lee Shih Kuang},
      year={2025},
      eprint={2403.01130},
      archivePrefix={arXiv},
      primaryClass={eess.AS},
      url={https://arxiv.org/abs/2403.01130}}
```

## Licensing

This repository is licensed under the [ISC License](https://github.com/shihkuanglee/ADFA/blob/main/LICENSE.md).

This repository includes modified codes from [SciPy](https://github.com/scipy/scipy).
