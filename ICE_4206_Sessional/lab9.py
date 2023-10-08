import numpy as np
import time

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X_input = np.array([[0, 0, 1],[0, 1, 1],[1, 0, 1],[1, 1, 1]])

D_target = np.array([[0],[0],[1],[1]])

input_layer_size = 3
output_layer_size = 1
learning_rate = 0.1
max_epochs = 10000


np.random.seed(42)
weights_sgd = np.random.randn(input_layer_size, output_layer_size)
weights_batch = np.random.randn(input_layer_size, output_layer_size)

start_time_sgd = time.time()
for epoch in range(max_epochs):
    error_sum = 0

    for i in range(len(X_input)):

        input_data = X_input[i]
        target_data = D_target[i]

        net_input = np.dot(input_data, weights_sgd)
        predicted_output = sigmoid(net_input)

        error = target_data - predicted_output
        error_sum += np.abs(error)

        weight_update = learning_rate * error * sigmoid_derivative(predicted_output) * input_data
        weights_sgd += weight_update[:, np.newaxis]  # Update weights for each input separately

    if error_sum < 0.01:
        break
end_time_sgd = time.time()

start_time_batch = time.time()
for epoch in range(max_epochs):
    # Forward pass
    net_input = np.dot(X_input, weights_batch)
    predicted_output = sigmoid(net_input)

    error = D_target - predicted_output
    error_sum = np.sum(np.abs(error))

    weight_update = learning_rate * np.dot(X_input.T, error * sigmoid_derivative(predicted_output))
    weights_batch += weight_update

    if error_sum < 0.01:
        break
end_time_batch = time.time()

test_data = X_input

def test_model(weights):
    predicted_output = sigmoid(np.dot(test_data, weights))
    return np.round(predicted_output).astype(int)

print("SGD Results: ")
print("Time taken: {:.6f} s". format(end_time_sgd - start_time_sgd))
print("Trained weights: ")
print(weights_sgd)
print("Predited binary outputs: ")
print(test_model(weights_sgd))

print("Batch Method result: ")
print("Time taken: {:.6f} s". format(end_time_batch - start_time_batch))
print("Trained weights: ")
print(weights_batch)
print("Predited binary outputs: ")
print(test_model(weights_batch))
