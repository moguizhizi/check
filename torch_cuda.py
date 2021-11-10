import torch
print(torch.cuda.is_available())
# 返回True 接着用下列代码进一步测试
print(torch.zeros(1).cuda())
print(torch.cuda.get_arch_list())
