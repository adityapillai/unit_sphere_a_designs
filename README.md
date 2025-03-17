# Unit Sphere A Designs

A package for computing A Designs over the unit sphere.

## Installation

You can install the package using pip:

```bash
pip install .
```

## Usage

Here is an example of how to use the package:

```python
from unit_sphere_a_designs.local import local_search
import numpy as np

# Example Run
d = 40
k = 2 * d + 1

S_LS = local_search(d, k, fixed_points=[0, 1])
alg_val = np.trace(np.linalg.inv(S_LS @ S_LS.T))

print(f'Finished with a value of {float(alg_val):.5f}')
```

## Running Tests

You can run the tests using pytest:

```bash
pytest tests/
```
