# the parameters for rabbit and fox growth and interactions
alpha, delta = 1, .25
beta, gamma = .2, .05

def derivs(state, t):
    """
    Return the derivatives of R and F, stored in the *state* vector::

       state = [R, F]

    The return data should be [dR, dF] which are the derivatives of R
    and F at position state and time *t*.
    """
    R, F = state
    dR = alpha*R - beta*R*F
    dF = gamma*R*F - delta*F
    return dR, dF
