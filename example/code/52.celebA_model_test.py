import torch.optim
import torchvision
from torch import nn
from torch.utils.data import DataLoader, Subset
from torch.utils.tensorboard import SummaryWriter
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
import time
from PIL import Image
import numpy as np
import os
import pandas as pd

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.feature_process = Sequential(Conv2d(3, 30, kernel_size=50, stride=1, padding=0),
                                          MaxPool2d(2),
                                          Flatten(),
                                          Linear(30*84 * 64, 40)
                                          )

    def forward(self, x):
        x = self.feature_process(x)
        return x


cuda_available = torch.cuda.is_available()  # GPU是否可用
device = torch.device('cuda' if cuda_available else 'cpu')
# 属性名字转中文
chinese_name = """
5_o_Clock_Shadow：刚长出的双颊胡须
Arched_Eyebrows：柳叶眉
Attractive：吸引人的
Bags_Under_Eyes：眼袋
Bald：秃头
Bangs：刘海
Big_Lips：大嘴唇
Big_Nose：大鼻子
Black_Hair：黑发
Blond_Hair：金发
Blurry：模糊的
Brown_Hair：棕发
Bushy_Eyebrows：浓眉
Chubby：圆胖的
Double_Chin：双下巴
Eyeglasses：眼镜
Goatee：山羊胡子
Gray_Hair：灰发或白发
Heavy_Makeup：浓妆
High_Cheekbones：高颧骨
Male：男性
Mouth_Slightly_Open：微微张开嘴巴
Mustache：胡子，髭
Narrow_Eyes：细长的眼睛
No_Beard：无胡子
Oval_Face：椭圆形的脸
Pale_Skin：苍白的皮肤
Pointy_Nose：尖鼻子
Receding_Hairline：发际线后移
Rosy_Cheeks：红润的双颊
Sideburns：连鬓胡子
Smiling：微笑
Straight_Hair：直发
Wavy_Hair：卷发
Wearing_Earrings：戴耳环
Wearing_Hat：戴帽子
Wearing_Lipstick：涂口红
Wearing_Necklace：戴项链
Wearing_Necktie：戴领带
Young：年轻
"""
chinese_name_ls = chinese_name.replace('\n',',').strip(',').split(',')
chinese_name_dict = {i.split('：')[0]:i.split('：')[1] for i in chinese_name_ls}
attr_names = ['5_o_Clock_Shadow',
 'Arched_Eyebrows',
 'Attractive',
 'Bags_Under_Eyes',
 'Bald',
 'Bangs',
 'Big_Lips',
 'Big_Nose',
 'Black_Hair',
 'Blond_Hair',
 'Blurry',
 'Brown_Hair',
 'Bushy_Eyebrows',
 'Chubby',
 'Double_Chin',
 'Eyeglasses',
 'Goatee',
 'Gray_Hair',
 'Heavy_Makeup',
 'High_Cheekbones',
 'Male',
 'Mouth_Slightly_Open',
 'Mustache',
 'Narrow_Eyes',
 'No_Beard',
 'Oval_Face',
 'Pale_Skin',
 'Pointy_Nose',
 'Receding_Hairline',
 'Rosy_Cheeks',
 'Sideburns',
 'Smiling',
 'Straight_Hair',
 'Wavy_Hair',
 'Wearing_Earrings',
 'Wearing_Hat',
 'Wearing_Lipstick',
 'Wearing_Necklace',
 'Wearing_Necktie',
 'Young',
 '']
attr_names = np.array(attr_names)

# 实例化模型
demo = Model()
demo.to(device)
# 再加载
demo.load_state_dict(torch.load('..\\data\\51.base_celeba\\CelebA_module_epoch10', map_location=torch.device('cuda')))

# 加载验证图片的目录
img_path = '..\\..\\dataset\\51.datasets\\test'
all_result = []
for img_name in os.listdir(img_path):
    img = Image.open(os.path.join(img_path, img_name))
    img = img.convert("RGB")
    transform = torchvision.transforms.Compose([torchvision.transforms.Resize((218, 178)),torchvision.transforms.ToTensor()])
    img = transform(img)
    demo.eval()
    img = torch.reshape(img, (1,  3, 218, 178))
    with torch.no_grad():
        img = img.to(device)
        output = demo(img)

    # 处理输出数据，对应到特征
    output = torch.sigmoid(output)
    output = torch.round(output)
    output = output.cpu()
    output = output.int()
    output = np.array(output)[0]
    output_english = attr_names[np.where(output == 1)[0]]

    output_list = [img_name.replace('.png', '')] + [chinese_name_dict.get(i) for i in output_english]
    all_result.append(output_list)

pd.DataFrame(all_result).to_excel('..\\data\\51.base_celeba\\test_data.xlsx')