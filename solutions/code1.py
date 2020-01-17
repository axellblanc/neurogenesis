tau = 0.01
kappa = 1


def distance(inp, W, nb_active_neurons):
    """
    Returns an array with the distance between the input and the weights of each one of the 'output layer' neurons
    """    
    return [sum(np.square(inp - W[j])) for j in range(nb_active_neurons)]


W_static = np.random.rand(max_output_neurons, size_data)
epsilon_static = np.array([0.6 for j in range(max_output_neurons)])
h_static = np.array([1. for j in range(max_output_neurons)])

train_network_static(data, W_static)