import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import math
import numpy

if __name__ == "__main__":
    fig, ax = plt.subplots()
    values_y, values_y2, values_x = [], [], []
    amp, period = [5], [1]
    plt.subplots_adjust(left=0.05, bottom=0.35)

    def calculateY():
        while len(values_x) != 0:
            values_y.pop()
            values_y2.pop()
            values_x.pop()
        print(values_y)
        for x in numpy.arange(0, 6.3006413, 0.0174533):
            values_y.append(amp[0] * math.sin(period[0] * x))
            values_y2.append(amp[0] * math.cos(period[0] * x + math.pi))
            values_x.append(x)
        print(values_y)

    calculateY()
    p, = plt.plot(values_x, values_y)
    # p2, = plt.plot(values_x, values_y2)

    slider_amp_axes = plt.axes([0.1, 0.2, 0.8, 0.05])
    slider_amp = Slider(slider_amp_axes,
                        label='Amp',
                        valmin=1,
                        valmax=10,
                        valinit=3,
                        valfmt='%1.2f')

    slider_period_axes = plt.axes([0.1, 0.1, 0.8, 0.05])
    slider_period = Slider(slider_period_axes,
                           label='period',
                           valmin=1/10,
                           valmax=10,
                           valinit=1,
                           valfmt='%1.2f',
                           valstep=.1)

    def update(val):
        amp[0] = slider_amp.val
        period[0] = slider_period.val
        calculateY()
        p.set_ydata(values_y)
        # p2.set_ydata(values_y2)
        fig.canvas.draw_idle()


    slider_amp.on_changed(update)
    slider_period.on_changed(update)

    plt.show()
