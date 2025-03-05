input_data = [[0.05, 0.10]]
weights = [0.15, 0.20, 0.25, 0.30, 0.40, 0.45, 0.50, 0.55]
target_output = [[0.01, 0.99]]
learning_rate = 0.5


def sigmoid(x):
    return 1 / (1 + pow(2.71828, -x))

def sigmoid_derivative(output):
    return output * (1 - output)


hidden_input = [
    input_data[0][0] * weights[0] + input_data[0][1] * weights[2],
    input_data[0][0] * weights[1] + input_data[0][1] * weights[3]
]
hidden_output = [sigmoid(x) for x in hidden_input]

output_input = [
    hidden_output[0] * weights[4] + hidden_output[1] * weights[6],
    hidden_output[0] * weights[5] + hidden_output[1] * weights[7]
]
final_output = [sigmoid(x) for x in output_input]

output_error = [final_output[0] - target_output[0][0], final_output[1] - target_output[0][1]]
output_delta = [output_error[0] * sigmoid_derivative(final_output[0]), output_error[1] * sigmoid_derivative(final_output[1])]

hidden_error = [
    output_delta[0] * weights[4] + output_delta[1] * weights[5],
    output_delta[0] * weights[6] + output_delta[1] * weights[7]
]
hidden_delta = [hidden_error[0] * sigmoid_derivative(hidden_output[0]), hidden_error[1] * sigmoid_derivative(hidden_output[1])]

weights[4] -= learning_rate * output_delta[0] * hidden_output[0]
weights[5] -= learning_rate * output_delta[1] * hidden_output[0]
weights[6] -= learning_rate * output_delta[0] * hidden_output[1]
weights[7] -= learning_rate * output_delta[1] * hidden_output[1]

weights[0] -= learning_rate * hidden_delta[0] * input_data[0][0]
weights[1] -= learning_rate * hidden_delta[1] * input_data[0][0]
weights[2] -= learning_rate * hidden_delta[0] * input_data[0][1]
weights[3] -= learning_rate * hidden_delta[1] * input_data[0][1]


for i, weight in enumerate(weights):
    print(f"Updated weight {i + 1}: {weight}")