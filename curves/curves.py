from dataclasses import dataclass
from typing import Any

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Curve:
    x: np.ndarray
    y: Any
    x_label: str
    y_label: str
    title: str
    filename: str

    def save_plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y(self.x))
        ax.set_xlabel(self.x_label)
        ax.set_ylabel(self.y_label)
        ax.set_title(self.title)
        plt.savefig(self.filename)


curves = [
    Curve(
        np.arange(0, 2 * np.pi, 0.01 * np.pi),
        lambda t: np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12) ** 5,
        r'$\theta$',
        r'$r(\theta) = \exp{(\cos{\theta})} - 2\cos{(4\theta)} + \sin^5{(\theta/12)}$',
        "Fey's butterfly curve",
        'fey.png'
    )
]

for curve in curves:
    curve.save_plot()
