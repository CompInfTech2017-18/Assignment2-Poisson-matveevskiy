

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

pi = np.pi

class landscap:
    def __init__(self,Ox,Oy,meth):
        self.eps = 0.01
        self.XX=Ox
        self.YY=Oy
        'self.Uin = np.random.rand(Ox,Oy)'
        self.Uin = np.zeros((Ox,Oy))
        
        X=np.linspace(0,self.XX,self.XX)
        Y=np.linspace(0,self.YY,self.YY)
        self.xgrid, self.ygrid = np.meshgrid(X,Y)
        self.ex(meth)
    
    def plotter(self,U):
        dx, dy = 1., 1.
        y, x = np.mgrid[slice(1, self.YY + dy, dy),
                slice(1, self.XX + dx, dx)]
        z = U
        
        levels = MaxNLocator(nbins=100).tick_values(z.min(), z.max())
        cmap = plt.get_cmap('PiYG')
        norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

        fig, (ax0) = plt.subplots(nrows=1)

        im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
        fig.colorbar(im, ax=ax0)
       
    def ex(self,meth):
        if meth == 'an':
            self.plotter(self.an())
    
    def an(self):
        
        x=self.xgrid
        y=self.ygrid
        U = self.Uin
        a = self.XX + 0.0
        im = 100
        V = 100.
        for i in range(im):
             U += np.sin(pi*(i+0.0)*x/a)*(np.sinh(pi*(i+0.0)*y/a))*16.0*V/(((2.0*(i+0.0)+1.0)*np.sinh((2.0*(i+0.0)+1.0)*pi)))
        return U
        np.c
        
        
        
a1 = landscap(100,100,'an')