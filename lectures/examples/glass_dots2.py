import numpy as np

class Transformer:
    def __init__(self, axes):

        # initial scaling and rotation
        self.sx, self.sy, self.theta = 1., 1., 0.
        self.dx = 0.001     # scaling increment on mouse move
        self.dtheta = 0.01  # rotation increment on mouse move
        self.axes = axes
        self.canvas = axes.figure.canvas

        # set up the matplotlib event handling callbacks
        self.canvas.mpl_connect('button_press_event', self.press)
        self.canvas.mpl_connect('button_release_event', self.release)
        self.canvas.mpl_connect('motion_notify_event', self.move)

        # the initial X data -- the "paper copy"
        X1 = self.X1 = np.random.rand(2,2000)-0.5

        # the matplotlib Line2D objects; we'll update line2 on mouse
        # moves
        self.line1, self.line2 = ax.plot(X1[0], X1[1], 'go', 
                                         X1[0], X1[1], 'ro', markersize=2)
        # the x and y locations when the mouse button is pressed or
        # mouse is moved
        self.xlast, self.ylast = None, None

        self.title = ax.set_title('drag the left or right mouse to stretch and rotate', fontweight='bold')

    def press(self, event):
        'mouse press, save the x and y locations'
        self.xlast, self.ylast = event.xdata, event.ydata

    def release(self, event):
        'release the mouse'
        self.xlast, self.ylast = None, None
        self.draw()

    def draw(self):
        sx, sy, theta = self.sx, self.sy, self.theta
        # the new rotate then scale matrix
        M =  np.array([[sx*np.cos(theta), -sx*np.sin(theta)],
                       [sy*np.sin(theta), sy*np.cos(theta)]])

        X2 = np.dot(M, self.X1)
        # update the data in line2, then redraw.  line1 is unchanged
        self.line2.set_data(X2[0], X2[1])
        self.canvas.draw()

    def move(self, event):

        if not event.inaxes: return    # not over axes
        if self.xlast is None: return  # no initial data
        if not event.button: return    # no button press

        # compute the distance moved since last mouse press
        dx = event.xdata - self.xlast
        dy = event.ydata - self.ylast

        if event.button==1:    # update the scale
            self.theta += dx
        elif event.button==3:  # update the rotation
            self.sx += dx
            self.sy += dy

        self.title.set_text('sx=%1.2f, sy=%1.2f, theta=%1.2f'%(self.sx, self.sy, self.theta))
        self.draw()
        # update the last x and y locations
        self.xlast, self.ylast = event.xdata, event.ydata


if __name__=='__main__':
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    t = Transformer(ax)
    plt.show()
