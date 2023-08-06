import torch

# 使用模型对输入数据进行预测
outputs = torch.Tensor([[1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 0]])

# 假设我们有一些真实标签
labels =  torch.Tensor([[1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1]])
# 计算正确预测的样本数
correct = (outputs == labels).sum().item()
# 预测结果为正例中真实为正例的比例（预测正例对的比例）(TP/TP+FP)
zl = (outputs == 1)
zzl = (outputs == 1) & (labels == 1)
rate = zzl.sum() / zl.sum()
print(rate)