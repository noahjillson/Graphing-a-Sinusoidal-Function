# Graphing-and-Translating-Sinusoidal-Function
## Description
A sinusoidal function graphed using pythin 3.8 and the matplotlib library. The amplitude and period of the sine function can be manipulated by two sliders at the bottom of the graph window.

## Instalation
Use the package manager pip to install Matplotlib by typing the bash commands bellow into the terminal
```bash
python -m pip install -U pip
python -m pip install -U matplotlib
```
You can also install Matplotlib through your IDE depending on which one you are using.


## Usage
```python
import matplotlib.pyplot as plt

x_values, y_values = [x in range(10)], [y in range(10)]

p, = plt.plot(x_values, y_values)
plt.show()
```
