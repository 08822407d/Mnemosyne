# Delivery Package Workflow / 交付包流程

这是 Mnemosyne 当前阶段用于向具体目标项目交付记忆系统设计和运行文件的流程草案。

## 1) 双层仓库原则

- Mnemosyne 仓库：设计工厂与设计档案。
- 目标项目仓库或目录：运行真相源。
- 交付前后主副本关系不同：
  - 交付前以 Mnemosyne 设计为主；
  - 交付后以目标项目运行文件为主。

## 2) 交付包组成

1. Memory System Design Spec
2. Target Project Memory Package
3. Delivery Manifest
4. Handoff Package
5. Unsupported Assumptions
6. Post-Delivery Drift Review TODO

## 3) 交付流程（手工/半自动）

1. Intake
2. Design
3. Review
4. Package
5. Deliver
6. Activate
7. Monitor
8. Iterate

## 4) Delivery Manifest 建议字段（草案）

- `delivery_id`
- `target_project`
- `target_project_type`
- `delivery_version`
- `source_design_refs`
- `generated_at`
- `target_paths`
- `included_files`
- `excluded_items`
- `unsupported_assumptions`
- `manual_steps_required`
- `review_required`
- `post_delivery_notes`

## 5) Drift / 漂移说明

交付后，目标项目实际运行文件可能与 Mnemosyne 设计档案发生差异。
当前仅记录未来 drift review 需求，不实现自动检查。

## 6) 目标项目类型示例

- 软件开发项目
- 语言学习项目
- 源码学习项目
- 长期研究项目
- 普通长期对话 / 个人知识管理项目

## 7) 当前阶段边界

当前不实现：
- 自动交付；
- 自动同步；
- 自动 drift 检查；
- 自动生成 AGENTS.md / CLAUDE.md / GitHub Actions。
