在无线网络信道接入领域，CSMA/CA协议作为一种经典的分布式信道接入方法，在IEEE 802.11等标准中得到了广泛应用。随着深度学习技术的发展，越来越多的研究将深度学习和深度强化学习应用到无线网络信道接入领域[xxx]。这些方法利用神经网络的强大表达能力，学习环境状态与最优行为之间的映射关系，为接入决策提供支持。Wang等人[xxx]通过流量模型共享提高了多智能体强化学习的协调机制；Zhao等人[xxx]通过增强AP存储信息类别和改变ACK帧携带的信息促进节点间信息交流，并采用深度强化学习协调数据包发送。然而，这些方法主要关注整体网络性能优化，使所有节点获得近似相等的信道接入机会，难以满足不同节点的差异化需求，无法提供个性化的信道接入能力。

信道状态预测研究方面，已有大量工作致力于提高预测准确性。一些研究[xx]采用机器学习技术进行互联网流量分类；另一些研究[13,14]通过神经网络模型预测信道状态变化。然而，这些预测技术很少被有效地应用到实际的信道接入决策中，预测结果未能有效指导信道接入行为。尽管有研究[xxx]尝试将信道空闲时间预测用于辅助接入决策，但这些方法大多采用单一数据流量模型，无法有效模拟复杂的网络信道环境。

近年来，为提高LLMs对面复杂任务的能力，多种多智能体协作框架被提出，如MetaGPT[xx]、ChatEval[xx]、CAMEL[xx]和StrategyLLM[xx]。这些方法展现了LLMs智能体在多步骤任务规划和协作解决问题方面的潜力。目前也有众多研究[liullms]将LLMs应用在网络中，XXX等人[kan2024mobile]将LLMs运用于5G网络的数据分析；XXX等人[wang2024netconfeval]将LLMs应用在网络配置任务中。然而，这些研究大多停留在辅助分析层面，很少与网络环境进行实时交互，缺乏在动态网络场景中进行实时决策的能力。






@article{tang2014comparative,
  title={Comparative investigation on CSMA/CA-based opportunistic random access for Internet of Things},
  author={Tang, Chong and Song, Lixing and Balasubramani, Jagadeesh and Wu, Shaoen and Biaz, Sa{\^a}d and Yang, Qing and Wang, Honggang},
  journal={IEEE Internet of Things Journal},
  volume={1},
  number={2},
  pages={171--179},
  year={2014},
  publisher={IEEE}
}

@article{chen2019improved,
  title={Improved CSMA/CA algorithm based on alternative channel of power line and wireless and first-time idle first acquisition},
  author={Chen, Zhixiong and Liu, Yingchu and Liu, Ran and Yuan, Jinsha and Han, Dongsheng},
  journal={Ieee Access},
  volume={7},
  pages={41380--41394},
  year={2019},
  publisher={IEEE}
}

Multi-Agent Deep Reinforcement Learning Multiple Access for Heterogeneous Wireless Networks With Imperfect Channels

@article{kan2024mobile,
  title={Mobile-llama: Instruction fine-tuning open-source llm for network analysis in 5g networks},
  author={Kan, Khen Bo and Mun, Hyunsu and Cao, Guohong and Lee, Youngseok},
  journal={IEEE Network},
  year={2024},
  publisher={IEEE}
}

@article{wang2024netconfeval,
  title={Netconfeval: Can llms facilitate network configuration?},
  author={Wang, Changjie and Scazzariello, Mariano and Farshin, Alireza and Ferlin, Simone and Kosti{\'c}, Dejan and Chiesa, Marco},
  journal={Proceedings of the ACM on Networking},
  volume={2},
  number={CoNEXT2},
  pages={1--25},
  year={2024},
  publisher={ACM New York, NY, USA}
}

@article{liullms,
  title={Llms for Computer Networking Operations \& Management: A Survey on Applications, Key Techniques, and Opportunities},
  author={Liu, Fan and Farkiani, Behrooz and Crowley, Patrick},
  journal={Key Techniques, and Opportunities}
}