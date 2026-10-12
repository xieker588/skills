# 桌宠形象（Live2D / VRM 模型）资源清单

> 状态：角色名 **「折纸」已定稿（2026-08-25）**；人物模型（具体 Live2D/VRM 资源）**待挑**。
> 用户偏好：二次元属性的美少女形象。

## 先分清两条路线（决定你能拿到什么）

| 路线 | 文件格式 | 风格 | 能直接动吗 | 获取成本 | 适合谁 |
| --- | --- | --- | --- | --- | --- |
| **A. Live2D** | `.moc3` + `.model3.json` + 贴图 | 2D 动漫（最贴二次元） | ✅ 官方渲染库/借 AIRI 集成 | 免费（官方示例） | 要"2D 看板娘"质感 |
| **B. VRM** | `.vrm`（单文件） | 3D 动漫 | ✅ UniVRM/桌宠引擎 | 免费（自建或下载） | 想要**专属**角色、可换装/换发型 |

> ⚠️ **AI 生成立绘（如 ImageGen）产出的是静态 2D 图片，不是 Live2D/VRM 模型，无法直接动**。
> 只能当"定视觉方向"的概念图，最终形象仍要走 A 或 B。

---

## 路线 A：Live2D（推荐，2D 二次元美少女现成最多）

### A1. Live2D 官方示例模型（Free Material License，免费、授权清晰）
- 中文页：https://www.live2d.com/zh-CHS/learn/sample/
- 英文页（全量）：https://live2d.com/en/download/sample-data/
- **美少女候选**（按推荐度）：
  - **Hiyori Momose** —— 标准看板娘，Cubism 3.0 经典模型
  - **Niziiro Mao** —— 二次元感强，Blend Shapes 示例
  - **Hatsune Miku（初音未来）** —— 官方合作模型
  - **Shizuku** —— Shizuku Talk 经典角色
  - **Kei** —— 支持真实口型同步（lip-sync，P1 语音有用）
  - **Unity-chan / Izumi / Epsilon** —— 备选
- 下载后文件结构示例（以 haru 为例）：
  ```
  model/
  ├── <模型名>.moc3            # 模型数据
  ├── <模型名>.model3.json     # 模型索引（渲染入口）
  ├── <模型名>.physics3.json   # 物理效果
  ├── <模型名>.pose3.json      # 姿势
  ├── texture_00.png …         # 贴图
  └── motion/                  # 动作（idle 等）
  ```

### A2. GitHub 开源合集（官方模型打包，npm 一键装）
- **xiazeyu/live2d-widget-models** —— chitose / haru / hibiki / koharu / miku / nito / shizuku / unitychan 等
  （`npm install live2d-widget-model-haru` 即可，模型在 `node_modules/` 里）
- **imuncle/live2d** —— 模型收集站
- **Eikanya/Live2d-model** —— 模型收集站
- **guansss/pixi-live2d-display** —— 渲染库（自带官方示例模型，也是后续自绘桌宠层的可选渲染栈）

### A3. 版权提醒
- 官方示例模型须遵守 **Live2D Free Material License**（个人/商用均可，但不可直接分发模型文件本身）；
- GitHub 社区收集的模型质量参差，**下载前看 README 授权声明**，别拿来商用。

---

## 路线 B：VRM（想要专属"折纸"就选这条）

### B1. VRoid Studio（免费，Windows/Mac）—— 亲手捏"折纸"
- 官网：https://vroid.com/studio
- 免费捏人：脸型/发型/服装/瞳色全可调，二次元渲染，导出 `.vrm` 单文件
- **完全免费、可商用**；想要"独一无二的折纸"最佳路径

### B2. VRoid Hub —— 下载现成免费 VRM
- 官网：https://hub.vroid.com/
- 海量用户上传的二次元美少女 VRM，按"無料/無償利用可"筛选，一键下载 `.vrm`

### B3. 其他 3D 平台
- **Sketchfab**（https://sketchfab.com）—— 搜 `VRM` / `anime girl`，勾选 free downloadable
- **MateEngine 桌宠** —— 内置模型 + 支持加载自定义 VRM（可先拿来试效果）

---

## ⚠️ 版权角色（阿尼亚等热门动漫角色）获取说明

> 用户 2026-08-25 问"有没有阿尼亚（《间谍过家家》）的模型"——结论：**官方免费授权模型不存在**；
> 网上均为**同人自制**，个人自用可行但限制严格。

### 现状
- **无官方免费 Live2D/VRM 模型**：阿尼亚版权归《间谍过家家》官方（远藤达哉/集英社等），未发布官方可下载模型。
- **同人模型存在**，最靠谱的来源：
  1. **B站会员购**「阿尼亚免费 live2d 模型」（UP主"天才设计学家"制作，0 元）：https://mall.bilibili.com 搜索"阿尼亚 live2d"
     - 许可：**仅限个人研究/使用/观赏；禁止直播盈利、禁止二次配布**；须符合官方二创规定
     - 需本人 B站账号 0 元下单领取（我无法代操作）
  2. **模之屋**（https://www.aplaybox.com）—— 站内搜"阿尼亚"，免费模型，多为不可商用
  3. **B站搜索**"阿尼亚 live2d"—— UP 主分享，注意甄别来源

### 红线（务必遵守）
- 个人自用 OK；**不可直播盈利、不可二次配布、不可商用**；
- 同人模型打包来源复杂，**优先正规平台（B站会员购/模之屋），警惕网盘来路不明的 exe/压缩包**（可能带毒）；
- 下载后格式多为 Cubism 2.1（`.moc`+`.model.json`）：原版 `pixi-live2d-display` 兼容 2.1/4.x；**Open-LLM-VTuber 的 fork 只支持 Cubism 3–5，不支持 2.1**（OLVT 官方文档确认）。

### 替代建议
- 想要"阿尼亚气质"又不想碰版权：用 **VRoid Studio 捏一个粉发绿瞳小女孩**（原创形象，无风险）；
- 或者继续用已落地的官方免费模型（初音/Shizuku）。

---

## 落地步骤（拿到模型后接进 P0 骨架）

1. 选好模型（Live2D 选 `.model3.json` 所在目录 / VRM 选 `.vrm` 文件）；
2. 放入 `runtime/p0/avatar-models/<名字>/`（新建目录，不入库可 gitignore）；
3. `conf/conf.yaml` 改：
   ```yaml
   avatar:
     provider: live2d        # 或 vrm
     model_path: ./avatar-models/<名字>/      # 指向模型目录/文件
   ```
4. 渲染层：借 AIRI 的 Live2D/VRM 集成方式（deploy.md §A.3）或 `pixi-live2d-display` 自绘透明置顶窗口（§E）；
5. 形象动起来后，Avatar 占位实现替换为真实渲染调用（src/avatar.py 接口不变）。

> P0 阶段形象是控制台占位，接模型属于 P0 收尾 / 桌宠层（§E），不影响对话链路已验证的编排权。

## 一句话建议
- 想**立刻有形象**：下载 Live2D 官方 **Hiyori Momose**（2 分钟拿到，免费合法，直接进桌宠）；
- 想要**专属折纸**：用 **VRoid Studio** 捏一个（半小时，免费）；
- AI 生成立绘仅用于**定视觉方向**（需 5–10 积分/张，可另生成概念图参考发型/瞳色/服装再照着捏）。
