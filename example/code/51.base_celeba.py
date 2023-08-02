import torch
import torch.nn as nn

# 定义模型
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        x = self.fc(x)
        return x

# 创建模型实例
model = MyModel()

# 定义损失函数
criterion = nn.BCEWithLogitsLoss()

# 定义优化器
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

# 模拟数据
data = torch.randn(4, 10)
target = torch.empty(4).random_(2).unsqueeze(1) # 调整目标张量的形状

# 计算损失
output = model(data)
loss = criterion(output, target)

# 反向传播和优化
optimizer.zero_grad()
loss.backward()
optimizer.step()