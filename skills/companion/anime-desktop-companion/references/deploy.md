# 本地部署 / 记忆 / 操控 详细步骤

> 定调（2026-08-24 自检后）：本技能为**自研 Harness + Loop 引擎**，AIRI / Open-LLM-VTuber 仅作参考模块（借集成方式/范式，不安装为底座）。下文据此重写。

## A. 搭自研 Harness 骨架（主，不是"装 AIRI"）

1. 装运行环境：Node / pnpm。
2. 按 `references/方案总成.md` §0.5 / §7 搭**自研 Orchestrator + 状态机 + conf.yaml** 最小骨架（我们 own 编排权）。
3. 形象渲染**借 AIRI 的 Live2D/VRM 集成方式**：克隆 `moeru-ai/airi` 仅作集成方式查阅（或借其渲染库），**不安装运行 AIRI 为底座**。
4. 导入 Live2D / VRM 模型（官方示例或自选）。
5. 配 LLM：Ollama 本地优先（qwen2.5，见 §1.5 资源档），过载/显存不足回落 API。

## B. 记忆层（自主管控，范式取自 Open-LLM-VTuber）

- 采用 **Letta / Mem0 范式**（取自 Open-LLM-VTuber v1.2），但**由我们 own**，不依赖 OLVT 托管。
- 每轮对话后把结构化摘要写入本地 `memory/<date>.md` 或 SQLite；启动时注入 system prompt。
- 记录三类（同 方案总成 §5）：指令、状态、偏好；冲突/去重/真值来源见 §5.1。

## C. 操控电脑（我们实现 MCP，范式取自 Open-LLM-VTuber）

- **自行实现 MCP Tool Server**（范式参考 Open-LLM-VTuber，不由其托管）；`cwd` 参数限工作目录。
- 暴露工具：打开应用、读/写文件、截图读屏、执行安全命令。
- 过权限闸门（L0~L3，见 §2.4）+ 沙箱 + 确认 + 可撤销；**绝不自动发消息 / 转账**。

## D. 语音唤醒

- VAD（silero）做常开麦克风检测；
- 本地 STT（FunASR / sherpa-onnx）转写；
- 命中唤醒词 → 唤醒；对话中支持 barge-in 随时打断（见 §3.2）。

## E. 桌宠模式

- 自绘透明背景、全局置顶、鼠标穿透；常驻桌面角落（参考 AIRI/OLVT Electron 的置顶实现，我们自绘）。
