import torch 
from torch import nn
from torch import optim
from torch.nn import functional as F 

class FactorizationMachine(nn.Module): 
    def __init__(self, n, k=8, **kwargs): 
        super().__init__() 
        # n = data.shape[1] (데이터 개수, column)
        self.V = nn.Parameter(torch.randn(n, k), requires_grad=True)
        self.linear = nn.Linear(n, 1)
        self.linear.weight.data.normal_(mean = 0, std = 0.001)
        
    def forward(self, x):
        # x = (batch_size, n) 
        # V = (n, k) 
        out_1pow = torch.matmul(x, self.V).pow(2).sum(1, keepdim=True) 
        out_2pow = torch.matmul(x.pow(2), self.V.pow(2)).sum(1, keepdim=True) 
        inner_product = out_1pow - out_2pow 
        inner_product = torch.sum(inner_product, dim=1, keepdim=True)
        out_linear = self.linear(x) 
        result = out_linear + 0.5 * inner_product
        # return result 
        return torch.sigmoid(result)
