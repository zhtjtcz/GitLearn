import torch
import torch.nn.functional as F
from collections import OrderedDict

if __name__ == '__main__':
    rnn = torch.nn.RNN(1, 1, 2, batch_first=True)
    # input_size hidden_size num_layers
    data = torch.rand(1, 1, 1)
    # Todo find
    print(rnn(data))
