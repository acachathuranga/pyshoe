import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def show3Dposition(data):
    """ Display 3D visualization of position data.
        
        :param data: Position data matrix with x,y,z positions as first 3 columns
    """
    px = data[:,0]
    py = data[:,1]
    pz = data[:,2]
    plt.figure()
    ax = plt.subplot(111, projection='3d')
    ax.scatter(px, py, pz, color='b')

    # Show best fit plane

    # do fit
    tmp_A = []
    tmp_b = []
    for i in range(len(px)):
        tmp_A.append([px[i], py[i], 1])
        tmp_b.append(pz[i])
    b = np.matrix(tmp_b).T
    A = np.matrix(tmp_A)
    fit = (A.T * A).I * A.T * b
    errors = b - A * fit
    residual = np.linalg.norm(errors)

    print ("Plane Solution:")
    print ("%f x + %f y + %f = z" % (fit[0], fit[1], fit[2]))
    # print ("errors:", errors)
    print ("residual:", residual)

    # plot plane
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    step = (xlim[1] - xlim[0]) / 10 + 1
    X,Y = np.meshgrid(np.arange(xlim[0], xlim[1], step),
                    np.arange(ylim[0], ylim[1], step))
    Z = np.zeros(X.shape)
    for r in range(X.shape[0]):
        for c in range(X.shape[1]):
            Z[r,c] = fit[0] * X[r,c] + fit[1] * Y[r,c] + fit[2]
    ax.plot_wireframe(X,Y,Z, color='k')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()

def show2Dposition(data, fileName=None):
    """ Display 2D visualization of position data.
        
        :param data: Position data matrix with x,y positions as first 2 columns
    """
    px = data[:,0]
    py = data[:,1]
    plt.plot(px, py)

    if (fileName != None):
        # Save plot to file
        plt.savefig(fileName+'.png')
        print ("Visualization plot saved to " + fileName + ".png")
        
    plt.show()

    