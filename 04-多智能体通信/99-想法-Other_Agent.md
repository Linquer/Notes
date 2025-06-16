同时考虑：可通信信道、距离(链路质量)、是否使用一个Proxy/AP作为中央控制器


训练一个Other_Agent，这个的输入是(ot_i, i, at_i)，输出是(ot+1_i)。

这个Other_Agent用来学习其他智能体的局部观测

在集中式调度的时候，需要输入每个Agent的局部观测时，直接采用Other_Agent的输出


如果ot_i向量太大，可以用一个Auto-Encoder的机制来实现缩小