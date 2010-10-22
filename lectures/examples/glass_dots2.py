import numpy as np
import numpy.linalg as linalg


class Transformer:
    def __init__(self, axes):
        self.theta = 0
        self.dtheta = 0.01
        self.sx = 1.
        self.sy = 1.
        self.dx = 0.001
        self.axes = axes
        self.canvas = axes.figure.canvas
        self.canvas.mpl_connect('button_press_event', self.press)
        self.canvas.mpl_connect('button_release_event', self.release)
        self.canvas.mpl_connect('motion_notify_event', self.move)

        X1 = self.X1 = np.random.rand(2,2000)-0.5

        self.line1, self.line2 = ax.plot(X1[0], X1[1], 'go', 
                                         X2[0], X2[1], 'ro', markersize=2)
        self.xlast = None
        self.ylast = None
        self.title = ax.set_title('drag the left or right mouse to stretch and rotate', fontweight='bold')

    def press(self, event):
        'mouse press, save the x and y locations'
        self.xlast = event.xdata
        self.ylast = event.ydata


    def release(self, event):
        'release the mouse'
        self.xlast = None
        self.ylast = None
        self.draw()

    def draw(self):
        sx, sy, theta = self.sx, self.sy, self.theta
        a =  sx*np.cos(theta)
        b = -sx*np.sin(theta)
        c =  sy*np.sin(theta)
        d =  sy*np.cos(theta)
        M =  np.array([[a,b],[c,d]])

        X2 = np.dot(M, self.X1)
        self.line2.set_data(X2[0], X2[1])

        self.canvas.draw()

    def move(self, event):

        if not event.inaxes: return    # not over axes
        if self.xlast is None: return  # no initial data
        if not event.button: return    # no button press

        dx = event.xdata - self.xlast
        dy = event.ydata - self.ylast

        if event.button==1:
            self.theta += dx
        elif event.button==3:
            self.sx += dx
            self.sy += dy

        self.title.set_text('sx=%1.2f, sy=%1.2f, theta=%1.2f'%(self.sx, self.sy, self.theta))
        self.draw()
        self.xlast = event.xdata
        self.ylast = event.ydata




import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
t = Transformer(ax)
plt.show()
