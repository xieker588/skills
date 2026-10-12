# 工程底座横向对比 + B站学习链接

## 一、底座对比

| 项目 | 形象 | 语音 | 本地 | 记忆 | 操控电脑 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| Open-LLM-VTuber | Live2D(Cubism5) | 全链路可打断 | ✅ 完全 | ✅ Letta(v1.2) | ✅ MCP | **记忆+操控最强参考模块**（范式取自它，不自建为底座） |
| Project AIRI | Live2D/VRM | ✅ | ✅ | ⚠️ 需外挂 | ⚠️ 弱 | 陪伴/陪玩感最强；**形象渲染参考模块**（不自建为底座） |
| Aivo | Unity 3D(VRM) | ✅ | 部分 | ✅ 长期记忆 | ✅ 文件操作 | 非动漫风 |
| Live2DPet | Live2D | ✅ VOICEVOX | ✅ | ❌ | ❌ | 轻量 Electron |
| DyberPet | GIF/PySide6 | ❌(可选AI) | ✅ | ❌ | ❌ | 养成系统 |
| BongoCat | Live2D/Tauri | ❌ | ✅ | ❌ | ❌ | 输入跟随互动 |

## 二、B站学习对象

- **爱弥斯桌宠**：B站 @-fugu- 原作；开源 ameath_DesktopPet（AI聊天 + 番茄钟 + 划词翻译 + 音乐）。
- **B站官方「猫娘计划 / N.E.K.O.」**（2026 WAIC）：全模态本地化 AI 数字生命，独立记忆服务 + 屏幕捕获 + 声音克隆，本地优先。
- **豆包桌宠**：零代码生成 exe（办公任务 Turbo + 本地电脑权限）。
- **DyberPet / BongoCat**：轻量桌宠互动参考。

## 三、关键决策（2026-08-24 自检后修订）

- **自研 Harness + Loop 引擎为唯一真值**（用户指令「自建」）；AIRI、Open-LLM-VTuber 均降级为**参考模块**（borrow，不 base）。
- 形象渲染**借 AIRI** 的 Live2D/VRM 集成方式；记忆+操控**借 Open-LLM-VTuber** 的 Letta + MCP 范式——二者均由我们 own，不托管于原项目。
- 仓库里只放"技能包"（人设 + 流程 + 配置要点）；底座范式按需查阅原仓库，不 clone/安装为运行底座。
