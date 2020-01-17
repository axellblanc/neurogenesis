def train_cycle_growing(inp,W, nb_active_neurons):
    """
    For a growing network W:
    Finds the BMU correponding to the input
    updates W and h accordingly
    """
    bmu = np.argmin(distance(inp, W, nb_active_neurons))
    activity = np.exp(-np.min(distance(inp, W, max_output_neurons)))
    if(h[bmu] < hT and activity < aT and nb_active_neurons < max_output_neurons and np.all(h[:nb_active_neurons] != 1)):
        W[nb_active_neurons] = (W[bmu] + inp)/2
        nb_active_neurons += 1
    else:
        W[bmu] += h[bmu] * epsilon[bmu] * (inp - W[bmu])
        h[bmu] = 0.95*h[bmu]
    return nb_active_neurons




aT = 0.05
hT = 0.01


W = np.random.rand(2, size_data)
W = np.r_[W, np.zeros((max_output_neurons - 2, size_data))]

epsilon = np.array([0.6 for j in range(max_output_neurons)])
h = np.array([1. for j in range(max_output_neurons)])

print('randomly initialized weights matrix, with only two active output neurons: \n\n', W)

train_network_growing(W,data,True)