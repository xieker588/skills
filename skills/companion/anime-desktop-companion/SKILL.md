---
name: anime-desktop-companion
description: 本地动漫桌面 AI 搭子——语音唤醒 + 操控电脑 + 跨会话长期记忆，自研 Harness/Loop 引擎（AIRI/Open-LLM-VTuber 作参考模块）的工程化搭建/运行流程。
disable-model-invocation: true
---

# 本地动漫桌面 AI 搭子

帮你从零搭建并长期运营一个**本地运行的二次元形象桌面 AI 伴侣**：

- 常驻桌面，动漫形象（Live2D / VRM）；
- 麦克风语音唤醒、能随时打断的自然对话；
- 通过工具调用**操控电脑**（开软件、整理文件、读屏幕）；
- **跨会话长期记忆**：记得你让它干过什么、当前项目状态、你的偏好。

定位：自己用，不是做产品。隐私优先，核心链路尽量本地跑。

## 工程底座（自建优先，AIRI/OLVT 作参考模块）

> 决策记录（2026-08-24 自检后修订）：用户指令「自建」——**自研 Harness + Loop 引擎为唯一真值**，拥有编排/状态机/权限/自检/恢复。
> Project AIRI、Open-LLM-VTuber 均**降级为参考模块**（borrow，不 base）：借 AIRI 的 Live2D/VRM 渲染与桌宠 UI 集成方式，借 Open-LLM-VTuber 的 Letta 记忆与 MCP 操控范式。二者以可替换子模块接入 Orchestrator，不绑定。
> 原「AIRI 记忆+操控弱」的矛盾因此消解：记忆与操控改为自主管控（见「记忆」「操控电脑」）。

- Project AIRI 仓库（**仅参考其 Live2D/VRM 渲染与桌宠集成方式**，不自建时为底座）：https://github.com/moeru-ai/airi
- 其预编译包 / 源码（`git clone ... && pnpm dev`，默认 http://localhost:5173）仅作集成方式查阅；自建下我们自绘桌宠层，不安装运行 AIRI 为底座（见 §0.5）。

备选底座（按需替换/混用）：

- **Open-LLM-VTuber**：Live2D 动漫 + 全链路语音可打断 + 完全本地；**v1.2 已带 Letta 长期记忆 + MCP 工具调用（操控电脑）+ B站弹幕**。记忆与操控的最强参考。https://github.com/Open-LLM-VTuber/Open-LLM-VTuber
- **Aivo**：Unity 3D 虚拟人，自带长期记忆 + 工作目录感知 + 对话式文件操作。非 Live2D 动漫风。https://github.com/WilliamPockey/Aivo
- 轻量皮：Live2DPet / DyberPet / BongoCat

## 学习对象（B站同类）

- **爱弥斯桌宠**：B站 @-fugu- 原作，Windows 桌宠 + AI聊天 + 番茄钟 + 划词翻译，开源（ameath_DesktopPet）。
- **B站官方「猫娘计划 / N.E.K.O.」**（2026 WAIC）：全模态本地化 AI 数字生命，独立记忆服务 + 屏幕捕获 + 声音克隆，本地优先。
- 豆包桌宠（零代码生成 exe）、DyberPet、BongoCat：轻量互动 / 皮参考。

## 标准搭建流程

1. 定人设：用 `references/persona-template.md` 写角色卡（名字、性格、口头禅、禁忌、唤醒词）。
2. 搭骨架：自研 Harness 最小骨架（Orchestrator+状态机+配置）；形象渲染借 AIRI 的 Live2D/VRM 集成方式导入模型（详见 `references/方案总成.md` §0.5 / §7）。
3. 接语音：ASR（sherpa-onnx / FunASR）+ TTS（Edge TTS / GPT-SoVITS 克隆音色）。
4. 接记忆：见「记忆」。
5. 接操控：见「操控电脑」。
6. 桌宠模式：透明背景、置顶、鼠标穿透，常驻桌面。

## 记忆（你最在意的点）

- **记忆层自主管控**（方案总成 §5）：采用 **Letta / Mem0 范式**（取自 Open-LLM-VTuber v1.2）但由我们 own——每轮把"指令 + 结果 + 当前状态"结构化写入本地（SQLite + Markdown），跨 Session 持久化；**不依赖 OLVT 托管**。
- 记录三类：(1) 你下过的指令；(2) 电脑当前状态 / 项目进度；(3) 你的偏好与禁忌。详见 `references/deploy.md`。

## 操控电脑

- 我们实现 **MCP Tool Server**（范式取自 Open-LLM-VTuber，不由其托管）：让模型通过 MCP 执行打开应用、文件整理、截图读屏；cwd 与命令白名单受权限闸门约束。
- 危险动作加确认 / 沙箱 / 可撤销，避免误删或误发。
- 唤醒词 + VAD 做常开麦克风；本地 STT 保隐私。

## 参考文件

- `references/projects.md` — 底座横向对比 + B站链接
- `references/persona-template.md` — 动漫角色人设模板
- `references/deploy.md` — 本地部署 / 记忆 / 操控详细步骤
- `references/方案总成.md` — 总体方案（harness engineering + loop engineering 两根支柱）
- `references/自检报告.md` — 方案质量审计（含「自建」转向结论）
- `references/local-llm-options.md` — 桌宠本地 AI 大脑选型（Qwen/DeepSeek/MiniCPM 等 + 显存档位）
- `references/model-resources.md` — 桌宠形象（Live2D/VRM）模型资源清单（官方免费模型 + VRoid 自建；角色名「折纸」已定稿）
- `references/vroid-persona-design.md` — **VRoid 捏人方案：原创「折纸」**（粉毛绿眼小女孩，阿尼亚气质×原创×纸艺意象；含配色/步骤/导出接入）
- `runtime/p0/` — **P0 已实施**：自研 Harness 最小骨架代码（Orchestrator + 状态机 + conf.yaml + 对话 loop；2026-08-25 沙箱验证通过，含 mock 降级）
