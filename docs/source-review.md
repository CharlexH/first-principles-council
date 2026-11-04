# 八个现有技能：吸收什么，实际带来了什么

审阅日期：2026-11-04。这里是一次设计取舍记录，不是技能排行榜，也不是上游方法的效果认证。

我们读了八个技能的正文及部分相关参考文件，并让它们分别回答同一道合成经营题：一位有小型琴房、有限时间和预算的兼职音乐老师，怎样找到第二条收入线？另设无技能和旧版技能两份答卷。各次运行使用独立上下文、相同材料与输出长度建议，不联网、不联系客户、不发生交易。

**共同结果：无技能 agent 已经识别了核心问题。** 它保留已付费的一对一教学，将“填满房间”改为“获得额外净收入”，提出老师排练、有限范围音频剪辑、脱离小房间的合唱诊断，并区分组织者和付款者。因此，外部技能提到这些同样的方向，不能算它们带来了新增能力。

## 逐项比较

| 技能 | 同题实际产出 | 值得吸收 | 不带入新版 |
|---|---|---|---|
| **jobs-to-be-done** | 比较了调课、借场、在家分练、取消等替代；补充切换阻力。主要经营方向与基线重合。也要求访谈十人，并给框架打了 5/10 分。 | 从具体事件重建客户想取得的进展，比较现有替代与不切换的原因。 | 固定访谈数量；为凑完整框架而补情绪与社交猜测；无实证含义的完成度评分。 |
| **blue-ocean-strategy** | 将合唱服务具体化为一次诊断、分声部音频和远程复核，提出同曲录音比较。也添加了 3/10 评分、价值曲线和试报价。 | 换购买者、交付环节或服务范围，检验删掉哪些成本仍能保留客户价值。录音前后比较是局部可操作细节。 | 把差异化或独特曲线当成市场成立；机械打分、追求十倍创新。基线也已提出合唱诊断，不能把该路线说成此技能独创。 |
| **continuous-discovery** | 将收入目标、客户问题、候选服务和试验连起来；提醒样本不足不能推断没市场。也增加每周访谈、更新机会树和 3/10 评分。 | 分开目标、机会、解法和实验；找最可能推翻推荐的假设，规定无法判定的情形。 | 周期与组织流程一刀切；每条路线统一“两笔付费”门槛；把点击或发起结账当成已验证付款。 |
| **mom-test** | 提出最近一次排练怎样解决、花了多少、谁批准收费等问题；明确三位老生付款不能支持团课。也附带 2/7 评分和固定讲话比例。 | 追问实际经历；分开原话、解释、答应下一步与兑现下一步；保留反例。 | 把访谈形式分数当商业证据；通用百分比、固定反例数量、每次谈话必须成交。核心路线与基线相近。 |
| **create-business** | 提供了相近的优先级和风险判断，但将定价、套餐等留到确认之后，要求五次访谈、三项承诺。 | 先复用已有证据；明确推断与已验证状态；保留停止或改题出口。 | 为本次咨询引入十阶段流程和多个审批门槛；把固定承诺数量作为市场验证。它的流程约束在这道题上推迟了可直接给出的建议。 |
| **feynman-principles** | 用白话、反证、必要条件、失败情形组织建议；提醒低价场租会被沟通清洁耗时吞掉。主要路线仍与基线重合。 | 检查因果解释、不可缺少的环节，以及会削弱自己判断的事实。 | 名人本人模拟；把四个检查项称为费曼亲授的商业框架；复制未确认授权的文本。 |
| **startup-idea-validator** | 明确离线材料不足以估算 TAM、CAC；同时输出 30/40/30 加权分，并因固定的十二个月万美元 MRR 门槛无法确认候选。 | 标明来源和时间窗；分别检查产品、商业与反证，保留实质分歧。 | 将适合某类创业项目的收入门槛套到本地兼职生意；主观加权分、来源乘数与风险分自动否决。 |
| **startup-idea** | 识别时间冲突、组织者不等于付款者、返工吞噬利润；明确不需先开发产品。路线与基线相近。 | 按业务阶段和可达资源缩小下一步；把手工流程、现有供应方也视为替代。 | 固定时间表和成交数量；借“像某位创业名人审项目”的人设增加权威感。 |

旧版 `1.2.0-rc1` 已经能区分“无人接受明确报价”与“尚未接触付款者”，也没有强制评分。这意味着新版不能仅靠重写这些原则宣称升级有效；其价值必须到未见案例的实际建议中找。

## 新版据此采用的设计

只保留少量会改变选择的动作：还原一次真实事件及替代方案；检查购买链与作用机制；在有线索时改变交付边界；把最危险假设变成能区分不同解释的测试。回答仍须给明确倾向，允许保留原路，不以新奇、方法数量或篇幅为目标。

上述是设计理由，**不是效果结论**。未见案例的对照材料和结论见本仓库评测文档；本题是开发题，不计作未见题成功。

## 公平性与边界

- 这八个技能用途不同：有的做访谈，有的做全流程创业编排，有的本来需要联网搜集。共同题只说明它们对这一次请求的适配与输出成本。
- 各技能使用正文及已取得的部分参考文件，未完整安装所有被推荐技能或依赖链。`mom-test`、`continuous-discovery` 答卷也报告了所需参考文件不全。这可能影响产出，不能据此否定完整安装的效果。
- 限制联网使来源型技能无法完成外部竞争研究；不得把它们诚实报告缺证据视为能力不足。
- 每种条件只运行一次，同一默认模型，非统计独立模型样本；宿主环境和指令隔离也不等于完全隔离。建议长度不是严格截断，实际篇幅有差异。
- 材料为合成情境。没有真实客户、收入或投资回报验证。

## 固定来源与许可

| 项目 | 本次读取的固定版本 | 许可状态 |
|---|---|---|
| wondelai / jobs-to-be-done | [v1.5.0 · SKILL](https://github.com/wondelai/skills/blob/d8d5d75f83da9f16d8aad5bab5f5b341a4770a30/jobs-to-be-done/SKILL.md) | MIT |
| wondelai / blue-ocean-strategy | [v1.4.1 · SKILL](https://github.com/wondelai/skills/blob/d8d5d75f83da9f16d8aad5bab5f5b341a4770a30/blue-ocean-strategy/SKILL.md) | MIT |
| wondelai / continuous-discovery | [v1.4.0 · SKILL](https://github.com/wondelai/skills/blob/d8d5d75f83da9f16d8aad5bab5f5b341a4770a30/continuous-discovery/SKILL.md) | MIT |
| wondelai / mom-test | [v1.4.0 · SKILL](https://github.com/wondelai/skills/blob/d8d5d75f83da9f16d8aad5bab5f5b341a4770a30/mom-test/SKILL.md) | MIT |
| wondelai / create-business | [v1.0.1 · SKILL](https://github.com/wondelai/skills/blob/d8d5d75f83da9f16d8aad5bab5f5b341a4770a30/create-business/SKILL.md) | MIT |
| VittorioRossi / feynman-principles | [b0264b3 · SKILL](https://github.com/VittorioRossi/feynman-skills/blob/b0264b3a1854d40e83dac0bb71f9c399912f16ad/skills/feynman-principles/SKILL.md) | 未确认；不复制或分发原文 |
| gabrieldejesusrodrigues / startup-idea-validator | [c892a63 · SKILL](https://github.com/gabrieldejesusrodrigues/agent-skills/blob/c892a63efdb0f8740a5b4fa126f9788460eb1680/skills/startup-idea-validator/SKILL.md) | Apache-2.0 |
| fabricioctelles / startup-idea | [ec4099f · SKILL](https://github.com/fabricioctelles/skills/blob/ec4099f92fdeadcf1771c2a3f64efa4970733c89/skills/startup-idea/SKILL.md) | Apache-2.0 |

正文采用本项目自己的表述。方法来源与上游实现的许可证不是一回事；参见 [方法来源](method-sources.md) 与 [第三方说明](../THIRD_PARTY_NOTICES.md)。
