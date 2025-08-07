#### 背景
![alt text](image-36.png)

#### 解决的问题
![alt text](image-37.png)

#### 详细方法设计
- 基础模型ACML
![alt text](image-39.png)
![alt text](image-38.png)
- Gated-ACML
![alt text](image-40.png)
![alt text](image-41.png)
- 门控训练
![alt text](image-42.png)
- 阈值T的设定
![alt text](image-43.png)

#### 模型训练
- Critic训练
![alt text](image-44.png)
- Actor和通信部分训练
![alt text](image-45.png)
- 辅助任务
![alt text](image-46.png)
- 训练Gated
    - 训练Gated的核心依据就是判断，采用通信和不采用通信的Q值的差
![alt text](image-47.png)