import torchvision
from torch.utils.data import DataLoader

dataset_path = r'E:\file\python\MyCode\dataset\51.datasets'
train_data = torchvision.datasets.CelebA(root=dataset_path, split='train',target_type='attr',transform=torchvision.transforms.ToTensor(), download=False)
test_data = torchvision.datasets.CelebA(root=dataset_path, split='test',target_type='attr',transform=torchvision.transforms.ToTensor(), download=False)

train_loader = DataLoader(dataset=train_data, batch_size=100, shuffle=False)
test_loader = DataLoader(dataset=test_data,  batch_size=100, shuffle=False)