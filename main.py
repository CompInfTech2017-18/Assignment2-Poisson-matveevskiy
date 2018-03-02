

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

pi = np.pi

class landscap:
    def __init__(self,Ox,Oy,meth):
        self.eps = 0.06
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
            U = self.an()
            self.plotter(U)
            self.lines(U)
        if meth == 'jac':
            U = self.Jacoby()
            self.plotter(U)
            self.lines(U)
        if meth == 'gauss':
            U = self.Gauss()
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
    
    def Jacoby(self):
        Unew = self.Uin
        Unew[self.YY-1,:] = 100.0
        n = 50000
        for i in range(n):
            Uold = Unew
            Uold1 = Unew[1:self.XX-1,1:self.YY-1]
            Unew[1:self.XX-1,1:self.YY-1] =(Uold[0:-2,1:-1]+Uold[2:,1:-1]+Uold[1:-1,2:]+Uold[1:-1,0:-2])/4.0
            
            if np.abs(((np.trace(Unew))-(np.trace(Uold1)))/np.trace(Uold1)) < self.eps:
                break
            Unew[self.YY-1,:] = 100.0
        return Unew
    
    def Gauss(self):
        Unew = self.Uin
        Unew[self.YY-1,:] = 100.0
        n = 50000
        for i in range(n):
            Uold1 = Unew[1:self.XX-1,1:self.YY-1]
            Unew[1:self.XX-1,1:self.YY-1] =(Unew[0:-2,1:-1]+Unew[2:,1:-1]+Unew[1:-1,2:]+Unew[1:-1,0:-2])/4.0
            
            if np.abs(((np.trace(Unew))-(np.trace(Uold1)))/np.trace(Uold1)) < self.eps:
                break
            Unew[self.YY-1,:] = 100.0
        return Unew
        
           
a1 = landscap(100,100,'gauss')

