混合信道接入分配方法

在该部分中，我们将介绍NetCogAgents整体框架以及各个智能体的具体分工和协作。并且还会介绍NetCogAgents如何与网络进行交互和具体决策流程。

<!-- 基于DM-MDN的信道接入方法虽然在提高单个节点接入效率方面表现出色，但其在实际应用中面临一个关键的局限性：缺乏有效的节点间协调机制。当局域网内同时采用此方法的节点数量增加时，各节点基于预测结果独立做出发送决策，容易导致节点间的激烈竞争，从而引发信道拥塞和性能下降。因此在有限的资源下，应当建立一种混合信道接入策略：部分节点采用DM-MDN方法以获得更高的接入效率，其余节点则采用传统CSMA/CA方法以保证网络稳定性。这种混合策略能够有效平衡网络性能与稳定性，但同时也带来了一个新的挑战：如何确定哪些节点应采用DM-MDN方法，哪些节点应采用CSMA/CA方法？
这一挑战进一步复杂化的因素在于，实际网络环境中不同节点的数据包优先级存在显著差异。即使是需要保障传输时延的高优先级数据包，其重要程度也有层次之分。例如，安全关键型应用的告警信息明显优先于一般的周期性状态更新信息。因此，对于采用DM-MDN方法的节点，还需要考虑其分位数参数的差异化设置。
如前所述，DM-MDN方法中的分位数参数直接影响节点的信道接入行为：高分位数设置使节点倾向于预期更长的信道空闲时间，从而表现得更为积极；低分位数设置则使节点更为保守，降低发送冲突的可能性。值得注意的是，分位数参数的设置并非越高越好。我们的研究表明，在网络高负载条件下，适当降低分位数反而能获得更好的整体性能，因为这减少了因过度乐观预测导致的频繁碰撞。而在低负载条件下，较高的分位数能够提高信道利用率，获得更好的吞吐量。
因此，我们需要一种动态的分配算法，能够根据网络状态和节点需求，为每个节点分配最适合的接入方法（DM-MDN或CSMA/CA）及相应的参数设置（如DM-MDN的分位数）。这种算法需要综合考虑网络的整体负载状况、各节点的优先级需求以及历史性能表现，做出智能化的资源分配决策。

面对混合信道接入管理的复杂挑战，传统分配方法存在明显局限性：基于规则的方法虽可解释性强但缺乏灵活性，预设规则难以覆盖多变网络环境的所有场景；基于数据驱动的方法具有自适应能力但需要大量训练数据，且决策过程不透明，泛化能力不足。更为关键的是，这两类方法都未能充分利用历史信息构建有效的认知策略，通常仅关注当前网络状态或短期数据，缺乏对长期网络行为模式的深入理解和推理能力，难以实现真正智能化、前瞻性的资源分配决策。因此，我们需要一种能够兼具可解释性与自适应性，并能有效利用历史经验进行认知推理的新型决策框架。 -->

基于DM-MDN的信道接入方法在提升单节点接入效率方面表现优异，但当网络内采用该方法的节点数量增加时，由于其缺乏协调机制，会导致网络整体性能下降。因此需要构建混合信道接入策略：部分节点使用DM-MDN，其余节点使用CSMA/CA增加网络稳定性。
实际网络环境中，不同节点的数据包优先级存在显著差异，即使在高优先级数据包中其紧急程度也有区别。因此，对采用DM-MDN方法的节点，还需考虑分位数参数的差异化配置。值得注意的是，分位数参数设置并非越高越好。通过大量的不同分位数实验我们发现，在网络高负载条件下，适当降低分位数反而能获得更好的性能；而在低负载条件下，较高分位数能提高信道利用率。
面对这种复杂的分配场景，现有分配方法存在明显不足：基于规则的方法可解释性强但灵活性差，难以适应复杂网络环境；数据驱动方法虽具自适应性，但需要大量训练数据且泛化能力有限。两类方法均未能充分利用历史信息进行认知推理，缺乏对长期网络行为模式的深入理解。因此，需要一种能够兼具可解释性与自适应性，并能有效利用历史经验进行认知推理的新型决策框架。

##### LLM Agent多智能体框架
###### 框架整体架构与设计理念
<!-- 近年来，以ChatGPT为代表的大语言模型(LLM)展现出强大的知识表示、逻辑推理和上下文理解能力。不同于传统机器学习方法，LLM通过海量文本数据的预训练，已经内化了丰富的世界知识和逻辑推理能力，能够在特定领域知识的引导下进行复杂的推理和决策。这些特性使LLM成为解决混合信道接入管理问题的理想工具。
本研究构建的多智能体协同框架由三类功能互补的智能体组成：决策智能体、经验智能体和反思智能体。这三类智能体共同形成一个完整的认知循环系统，能够不断积累经验并优化决策策略。图X展示了该框架的整体架构和工作流程。
决策智能体作为框架的核心执行单元，直接参与网络运行时的实时决策过程。它接收当前网络各节点的需求特征（数据包优先级），综合经验库中的历史决策记录和规则，为每个节点动态确定最适合的信道接入算法（DM-MDN或CSMA/CA）及相应的参数设置（DM-MDN的分位数）。决策完成后，会将决策内容、决策时的网络状态以及网络仿真结果等信息记录到决策日志中，为后续的经验积累和策略优化提供原始数据。
经验智能体负责对决策日志进行分析，将原始决策记录转化为可供学习和推理的经验知识。具体而言，经验智能体对单轮的决策日志进行经验总结，并生成固定格式的结构化的经验。这些结构化的经验数据按照预设的知识组织结构存储到经验库中，形成一个不断扩充的知识库，为决策智能体提供历史经验支持。
反思智能体在系统运行一段时间后定期启动，对累积的经验数据进行更高层次的归纳和优化。它从经验库中提取全部经验数据，利用LLM强大的归纳推理能力，分析不同决策在不同场景下的效果模式，提炼出具有普适性的决策规则和策略模式。这些经过反思优化的决策规则会重新写回到经验库中，指导决策智能体做出更为合理的决策。需要特别注意的是，反思的经验会覆盖之前由经验智能体生成的单轮经验。
三类智能体之间形成了一个闭环的认知系统：决策智能体负责执行，产生原始决策数据；经验智能体负责组织，将原始数据转化为结构化经验；反思智能体负责优化，从经验中提炼规则并反馈指导。通过这种循环迭代的机制，系统能够不断积累经验、优化策略，实现在复杂网络环境中的智能适应性决策。 -->

当前，以ChatGPT为代表的LLMs通过海量文本数据的训练，内化了丰富的领域知识和推理能力，能够在特定的Prompt引导下进行复杂决策。这一特性使其成为解决混合信道接入管理问题的理想工具。因此，本研究设计了基于LLMs的NetCogAgents，如图X所示它由三类功能互补的智能体组成：决策智能体、经验智能体和反思智能体，共同形成一个完整的认知循环系统。
决策智能体作为核心执行单元，负责网络运行时的实时决策。它基于当前网络节点的需求特征（数据包优先级），结合经验区中的历史记录，为每个节点动态分配信道接入算法（DM-MDN或CSMA/CA）及相应参数（DM-MDN分位数）。决策完成后，会将决策内容、决策时的网络状态以及网络仿真结果等信息记录到决策日志中，为后续的经验积累和策略优化提供原始数据。
经验智能体负责对决策日志进行分析，将原始决策记录转化为可供学习和推理的经验知识。具体而言，经验智能体对单轮的决策日志进行总结，并生成固定格式的结构化的经验。这些结构化的经验数据按照预设的知识组织结构存储到经验区中，形成一个不断扩充的知识库，为决策智能体提供历史经验支持。经验智能体的输入除了单轮的决策日志以外还有历史经验，之所以在输入中添加历史经验是为避免经验智能体生成重复的经验。若当前的决策日志中的场景在历史经验中存在，并且本轮的决策结果未取得更好的结果时，经验智能体就可能选择不生成新的经验。
反思智能体在系统运行一段时间后定期启动，对累积的经验数据进行更高层次的归纳和优化。它从经验库中提取全部数据，利用LLM强大的归纳推理能力，分析不同决策在不同场景下的效果模式，提炼出具有普适性的决策规则和策略模式。这些经过反思优化的决策规则会重新写回到经验库中，指导决策智能体做出更为合理的决策。需要特别注意的是，反思的经验会覆盖之前由经验智能体生成的单轮经验。
三类智能体之间形成了一个闭环的认知系统：决策智能体负责执行，产生原始决策数据；经验智能体负责组织，将原始数据转化为结构化经验；反思智能体负责优化，从经验中提炼规则并反馈指导。通过这种循环迭代的机制，系统能够不断积累经验、优化策略，实现在复杂网络环境中的智能适应性决策。
###### 经验与经验区管理
<!-- 经验区（Experience Pool）是多智能体协同框架的核心知识库，存储了系统运行过程中积累的各类经验数据和决策规则。经验内容和经验区的组织和管理直接影响整个框架的学习效率和决策质量。
经验区主要包含两类数据：结构化经验记录和优化决策规则。
结构化经验记录由经验智能体从原始决策日志中提炼而来，每条记录包含以下核心要素： 场景描述（Scene）：记录决策时的各个节点的需求（节点数据包优先级）。决策内容（Decision）：记录为各节点分配的具体信道接入方法（DM-MDN或CSMA/CA）及相应参数设置（如DM-MDN的分位数值）。执行结果（Result）：记录决策执行后的网络性能表现，包括吞吐量、平均时延、丢包率等指标。效果评估（Evaluation）：基于执行结果对决策效果进行定性和定量评估，包括与预期目标的符合度、相比历史决策的改进程度等。
优化决策规则则是由反思智能体通过分析经验记录提炼而来，描述在特定条件下应采取的最优决策策略，每条规则包含条件部分（网络节点需求）和行动部分（推荐的接入方法和参数设置）。
随着系统持续运行，决策智能体不断产生新的决策记录，经验智能体将这些记录转化为结构化经验存入经验区，导致经验数据量迅速增长。然而，大语言模型在处理过长上下文时会面临注意力分散和性能下降的问题，过多且质量参差不齐的经验记录反而会干扰决策智能体的判断，降低决策质量。
这一挑战促使我们引入反思智能体作为系统的第三个核心组件。反思智能体通常在经验智能体运行固定轮次后启动，对已积累的单轮决策经验进行高层次归纳和抽象，提炼出具有普适性和指导价值的优化决策规则。这些精炼的规则比原始经验更为凝练和高效，能够为决策智能体提供更加清晰的指导。
经验区的管理也随系统运行阶段而演变：初始阶段，经验区主要包含单轮决策的结构化经验记录；第一轮反思后，这些原始经验被优化决策规则所替代，大幅提高了决策效率；在后续运行至下一轮反思之前，经验区同时包含新产生的结构化经验和上一轮反思生成的优化规则，两者协同为决策智能体提供全面的决策参考。这种动态管理机制确保了经验区既能不断吸收新知，又能保持高效精简的知识结构。 -->

经验区作为多智能体协同框架的核心知识库，存储系统运行过程中积累的各类经验数据，其组织管理方式直接影响框架的学习效率和决策质量。

经验区主要包含两类数据：结构化经验和反思经验。结构化经验由经验智能体从决策日志中提炼而成，每条记录包含场景描述（Scene）、决策内容（Decision）、执行结果（Result）和效果评估（Evaluation）等核心要素。场景描述记录决策时各节点的需求(节点数据包优先级)；决策内容记录为各节点分配的具体信道接入方法及相应参数配置；执行结果记录决策执行后的网络性能指标；效果评估则基于执行结果对决策内容进行评价。反思经验由反思智能体通过分析结构化经验提炼而来，描述特定条件下的最优决策策略，每条经验包含场景部分和决策部分。

随着系统持续运行，决策智能体不断产生新决策日志，经验智能体将这些日志转化为结构化经验存入经验区，这会导致经验数据量迅速增长。而过多且质量不一的经结构化经验会干扰决策智能体的判断，降低决策质量。为解决经验区经验冗长问题，本框架引入反思智能体作为第三个核心组件。反思智能体通常在经验智能体运行固定轮次后启动，对经验区的所有经验进行高层次归纳和抽象，提炼出具有普适性和指导价值的反思经验。这些精炼规则比原始经验更为凝练和高效，能为决策智能体提供更清晰的指导。

经验区的管理策略随系统运行阶段演变：初始阶段，经验区主要包含单轮决策的结构化经验；第一轮反思后，结构化经验被反思经验替代；后续运行阶段，经验区同时包含新产生的结构化经验和反思经验；当反思智能体再次启动时，经验区将只保留新生成的反思经验。这种动态管理机制确保经验区既能持续吸收新知识，又能维持高效精简的经验结构，有效支持多智能体系统的协同决策过程。
