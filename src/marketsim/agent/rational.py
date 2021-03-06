from math import *

from marketsim.agent import Agent

class RationalAgent(Agent):
    def _predict_price(self, p: float, d: float):
        return self.parent.rho*(self.parent.fair_price + d) + (1 - self.parent.rho)*floor((1 + self.parent.f)*self.parent.d+self.parent.g)
