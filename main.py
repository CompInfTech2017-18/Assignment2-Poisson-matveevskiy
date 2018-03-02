

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
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
        self.run(meth)
    
    def plotter(self,U):
        dx, dy = 1., 1.
        y, x = np.mgrid[slice(1, self.YY + dy, dy),
                slice(1, self.XX + dx, dx)]
        z = U
        
        levels = MaxNLocator(nbins=100).tick_values(0.0, z.max())
        cmap = plt.get_cmap('PiYG')
        norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

        fig, (ax0) = plt.subplots(nrows=1)

        im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
        fig.colorbar(im, ax=ax0)
        
    
       
    def run(self,meth):
        if meth == 'an':
            U=self.an()
            self.plotter(U)
            self.lines(U)
    
    def lines(self, U):
        dx, dy = 1., 1.
        y, x = np.mgrid[slice(1, self.YY + dy, dy),
                slice(1, self.XX + dx, dx)]
        z = U
        plt.figure()
        CS = plt.contour(x, y, z, 5)
        plt.clabel(CS, inline=1, fontsize=10)
        
    
    def an(self):
        
        x=self.xgrid
        y=self.ygrid
        U = self.Uin
        a = self.XX
        im = 99
        V = 100
        for i in range(im):
            U += 4*V/pi*np.sinh(pi*(y)/a*(2*i + 1)) * np.sin((pi*x)/a*(2*i + 1)) /( (2*i+1) * np.sinh(pi*(2*i + 1)) )
        return U
        
        
        
        
a1 = landscap(100,100,'an')