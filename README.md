# Paper Humanizer Skill

中英文学术文本润色与人性化Skill，用于去除 AI 生成的痕迹，同时严格保持事实准确性。

## ✨ 主要功能

- 🎯 **去除 AI 痕迹**：识别并移除常见的 AI 写作模式
- 📚 **学术语气优化**：保持学术严谨性，提升文本自然度
- 🔒 **事实严格保护**：绝不编造数据、篡改数值或改变实验结论
- 🌍 **双语支持**：完整支持中文和英文学术写作
- ⚙️ **高度可配置**：多种参数配置，适应不同写作风格

## 🚀 快速开始

### 作为 Claude Code Skill 使用

#### 安装步骤

```bash
# 从 GitHub 克隆仓库
git clone https://github.com/crabin/paper-humanizer-skill.git /tmp/paper-humanizer-skill

# 创建 skills 目录（如果不存在）
mkdir -p ~/.claude/skills/

# 复制到 skills 目录
cp -r /tmp/paper-humanizer-skill ~/.claude/skills/paper-humanizer

# 验证安装
ls ~/.claude/skills/paper-humanizer/
```

#### 使用

在对话中直接使用，系统会自动应用相应的提示词。

### 命令行脚本使用

```bash
# 处理文本文件
python3 scripts/paper_humanizer.py --text-file input.txt --language auto

# 生成组合提示词供外部使用
python3 scripts/paper_humanizer.py --text-file input.txt --out prompt.md

# 从标准输入读取
cat input.txt | python3 scripts/paper_humanizer.py --language zh
```

## 📋 参数配置

### 基础参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--language` | auto/zh/en | auto | 文本语言（自动检测/中文/英文） |
| `--tone` | formal/semi-formal/concise/persuasive | formal | 写作语气风格 |
| `--field` | string | computer science | 研究领域（用于保持术语一致性） |
| `--audience` | string | academic | 目标读者群体 |

### 约束控制

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--strict-factuality` | flag | True | 严格保持事实性（不篡改数据） |
| `--no-strict-factuality` | flag | False | 允许适度调整表达 |
| `--keep-citations` | flag | True | 保留引用标记 [1], (Smith, 2023) |
| `--drop-citations` | flag | False | 移除引用标记 |
| `--blacklist-level` | low/medium/high | high | AI 痍迹短语过滤级别 |

## 📝 输出格式

系统始终输出 4 个部分：

```
1. 原文 AI 特征分析：
   - 识别 2-3 个主要 AI 模式问题

2. 核心优化策略：
   - 列出 3-5 个针对性优化策略

3. 优化亮点说明：
   - 突出 1-2 个代表性修改（可选）

4. 优化后的文章：
   <完整优化后的文本>
```

## 🎯 核心原则

### 不可协商的约束

- ❌ **绝不编造**新的事实、结果、指标或参考文献
- ❌ **绝不改变**任何数值、超参数、阈值或对比结果
- ✅ **保留所有**引用标记（如 [1]、(Smith, 2023)、\cite{...}）
- ✅ **保持术语**在目标领域的一致性

### 去除的 AI 痕迹

**中文常见 AI 痕迹：**
- "值得注意的是"、"不难发现"、"基于以上分析"
- "综上所述"、"首先/其次/最后"、"本文将"
- "在一定程度上"、"显著提升"（无量化支撑时）
- "具有重要意义"、"此外"、"同时"（过度使用时）

**英文常见 AI 痕迹：**
- "It is worth noting that"、"It can be seen that"
- "In summary"、"Firstly, Secondly, Finally"
- "This paper aims to"、"To some extent"
- "Significantly improves"（无证据时）

完整列表见 `references/phrase_blacklist.md`

## 📖 使用示例

### 中文示例

**输入：**
```
值得注意的是，本文将提出一种基于WGAN-GP的改进方法，
并在NSL-KDD数据集上进行了实验。实验结果表明，该方法
在准确率上有显著提升。综上所述，本方法具有重要意义。
```

**优化后：**
```
本研究提出了一种基于 WGAN-GP 的改进方法，并在 NSL-KDD
数据集上进行了验证。实验结果显示，该方法将准确率提升了
X%，表明该方法在网络安全入侵检测领域具有应用价值。
```

### 英文示例

**输入：**
```
It is worth noting that this paper aims to propose an improved
method based on WGAN-GP and conducts experiments on the NSL-KDD
dataset. The experimental results show that the method significantly
improves accuracy. In summary, the proposed method is of great significance.
```

**优化后：**
```
This study presents an improved WGAN-GP-based method, validated on
the NSL-KDD dataset. Results demonstrate a X% accuracy improvement,
indicating the method's practical value in network intrusion detection.
```

## 🧪 测试用例

以下两个测试用例可用于验证 skill 功能是否正常。

### 测试用例一：中文学术段落（含多种 AI 痕迹）

**输入文本**（来自 `examples/zh_input_rich.txt`）：
```
在当今人工智能技术迅猛发展的背景下，网络安全问题愈发凸显其重要性。值得注意的是，传统的入侵
检测系统在面对不断演变的网络攻击时，往往表现出明显的局限性。不难发现，现有方法在处理类别不
平衡数据集时存在诸多不足，严重制约了模型的泛化能力。

为了解决上述问题，本文旨在提出一种基于改进WGAN-GP的入侵检测方法。本文将深度学习与生成对抗
网络有机结合，充分发挥二者各自的优势，有效地、全面地解决了传统方法存在的不足之处。

综上所述，本文提出的方法不仅在技术层面实现了重要突破，更为入侵检测领域的发展提供了新的思路
和方向，具有重要的理论意义和实践价值。
```

**预期 AI 特征分析**：
- ❌ 模式词：「值得注意的是」「不难发现」「本文旨在」「综上所述」「有效地、全面地」「具有重要意义」
- ❌ 空洞套话：「充分发挥」「有机结合」「具有重要的理论意义和实践价值」
- ❌ 无量化支撑的「显著提升」「重要突破」

**预期优化结果示例**：
```
传统入侵检测系统难以应对持续演变的网络攻击，在类别不平衡数据集上的泛化能力尤为薄弱。
本研究提出一种基于改进 WGAN-GP 的入侵检测方法，将生成对抗网络与深度学习相结合，针对
类别不平衡问题进行专项优化。实验结果表明，该方法在 NSL-KDD 数据集上的准确率、召回率
和 F1 值均有提升，具体改进幅度见表2。
```

---

### 测试用例二：英文学术段落（含多种 AI 痕迹）

**输入文本**（来自 `examples/en_input_rich.txt`）：
```
In today's rapidly evolving digital landscape, cybersecurity threats are becoming increasingly
sophisticated. It is worth noting that traditional intrusion detection systems often struggle
to keep pace with the ever-changing nature of network attacks.

To address this issue, this paper aims to propose an innovative framework based on an improved
WGAN-GP architecture. Furthermore, the method holistically addresses the multifaceted challenges
of intrusion detection in a comprehensive and robust manner.

In conclusion, the proposed method represents a significant advancement in the field. Based on
the above analysis, it can be concluded that this work has far-reaching implications for
cybersecurity research and practice.
```

**预期 AI 特征分析**：
- ❌ 模式词：`It is worth noting that`、`this paper aims to`、`In conclusion`、`Based on the above analysis`
- ❌ 空洞修饰：`rapidly evolving landscape`、`holistically addresses the multifaceted challenges`、`comprehensive and robust`
- ❌ 无量化支撑的 `significant advancement`、`far-reaching implications`

**预期优化结果示例**：
```
Traditional intrusion detection systems struggle to adapt to evolving network attacks, particularly
under class-imbalanced conditions. This work proposes an improved WGAN-GP framework that directly
targets class imbalance in intrusion detection. On the NSL-KDD dataset, the method achieves
improvements in accuracy, recall, and F1 score over existing baselines (see Table 2), suggesting
practical applicability in real-world cybersecurity deployments.
```

---

## 📂 项目结构

```
paper-humanizer/
├── README.md                      # 本文档
├── SKILL.md                       # Skill 元数据定义
├── references/                    # 参考文档
│   ├── system_prompt.md           # 系统提示词（核心编辑原则）
│   ├── user_template.md           # 用户提示词模板
│   └── phrase_blacklist.md        # AI 痕迹短语黑名单
├── scripts/                       # 脚本工具
│   ├── paper_humanizer.py         # Python CLI 工具
│   └── paper_humanizer.sh         # Bash 包装脚本
└── examples/                      # 使用示例
    ├── zh_input.txt               # 中文简单示例输入
    ├── zh_input_rich.txt          # 中文完整段落示例（含 6+ AI 痕迹）
    ├── en_input.txt               # 英文简单示例输入
    ├── en_input_rich.txt          # 英文完整段落示例（含 8+ AI 痕迹）
    └── run_demo.sh                # 演示脚本
```

## ⚠️ 注意事项

1. **事实性保护**：如检测到原文存在矛盾或歧义，会在"核心优化策略"部分提出中性建议，而非直接修改文本
2. **技术术语**：保持技术术语原样（如 GAN、WGAN-GP、NSL-KDD），除非上下文要求标准翻译
3. **语言保持**：输出语言与输入保持一致，除非用户明确要求翻译
4. **引用标记**：默认保留所有引用标记，可通过 `--drop-citations` 参数移除

## 🔧 高级配置

### 领域特定术语

通过 `--field` 参数指定研究领域，系统会：
- 保持该领域的术语一致性
- 使用符合领域惯例的表达方式
- 保留特定缩写和专业词汇

### 语气风格选择

- `formal`：正式学术写作（论文、期刊投稿）
- `semi-formal`：半正式（技术报告、博客）
- `concise`：简洁风格（摘要、总结）
- `persuasive`：说服性风格（申请材料、项目书）

## 📚 相关文档

- `references/system_prompt.md` - 完整编辑原则和约束条件
- `references/phrase_blacklist.md` - AI 痕迹短语完整列表
- `references/user_template.md` - 参数化提示词模板
- `SKILL.md` - Skill 元数据和快速参考

## 🤝 贡献

欢迎提交问题和改进建议！

## 📄 许可

本 skill 为学术辅助工具，请负责任地使用。优化后的文本仍需作者仔细校对。
