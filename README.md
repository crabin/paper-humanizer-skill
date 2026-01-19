# Paper Humanizer

中英文学术文本润色与人性化工具，用于去除 AI 生成的痕迹，同时严格保持事实准确性。

## ✨ 主要功能

- 🎯 **去除 AI 痕迹**：识别并移除常见的 AI 写作模式
- 📚 **学术语气优化**：保持学术严谨性，提升文本自然度
- 🔒 **事实严格保护**：绝不编造数据、篡改数值或改变实验结论
- 🌍 **双语支持**：完整支持中文和英文学术写作
- ⚙️ **高度可配置**：多种参数配置，适应不同写作风格

## 🚀 快速开始

### 作为 Claude Code Skill 使用

1. 确保 skill 已安装在 `~/.claude/skills/paper-humanizer/`
2. 在对话中直接使用，系统会自动应用相应的提示词

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
    ├── zh_input.txt               # 中文示例输入
    ├── en_input.txt               # 英文示例输入
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
