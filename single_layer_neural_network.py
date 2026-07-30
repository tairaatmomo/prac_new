import numpy as np
np.random.seed(1)
class NeuralNetwork:
  def __init__(self):
    self.weight_matrix = 2 * np.random.random((3,1)) -1
  def tanh(self, x):
    return np.tanh(x)
  def tanh_derivative(self, a):
    return 1.0 - a**2
def forward_propagation(self, inputs):
  inputs = np.atleast_2d(inputs)
  return self.tanh(np.dot(inputs, self.weight_matrix))
def train(self, train_inputs, train_outputs, num_train_iterations, learning_rate = 0.1, verbose=False):
  m = train_inputs.shape[0]
  for iteration in range(num_train_iterations):
    output = self.forward_propagation(train_inputs)
    error = train_outputs - output
    delta = error * self.tanh_derivative(output)
    adjustment = np.dot(train_inputs.T, delta) / m
    self.weight_matrix += learning_rate * adjustment

    if verbose and (iteration % max(1, num_train_iterations // 10) == 0):
      loss = np.mean(error ** 2)
      print(f'Iteration {iteration:6d}  loss ={loss:6d}')

if __name__ == "__main__":
    nn = NeuralNetwork()
    print("Initial weights:\n", nn.weight_matrix)

    X = np.array([[0, 0, 1],
                  [1, 1, 1],
                  [1, 0, 1],
                  [0, 1, 1]])
    y = np.array([[0, 1, 1, 0]]).T

    nn.train(X, y, num_train_iterations=10000, learning_rate=0.1, verbose=True)

    print("\nTrained weights:\n", nn.weight_matrix)

    print("\nTest [1, 0, 0] ->", nn.forward_propagation(np.array([1, 0, 0])))
