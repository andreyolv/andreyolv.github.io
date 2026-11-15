---
status: active
environment: local
kind: project
---

# AI-Native Development with OpenCode as an AI IDE

## Problem

- Development Speed Bottleneck: Writing boilerplate, navigating unfamiliar codebases, and wiring up tools manually consume a large share of engineering time, slowing down feature delivery and refactoring.
- Context Switching Cost: Moving between editor, terminal, browser, and AI chat breaks focus. Asking an AI about code requires copying snippets out, switching tabs, and pasting answers back — friction that discourages frequent use.
- Inconsistent AI Assistance: Each developer uses a different AI workflow, with different prompts and context, so code quality and architectural decisions vary across the team.
- Tooling Fragmentation: Documentation lookup, code generation, refactoring, test writing, and CLI operations happen in separate tools without shared context about the repository.
- No Reusable AI Workflows: Common tasks (adding a skill, creating a worktree, reviewing a diff, diagnosing a failed build) are re-invented ad hoc instead of being codified as repeatable AI-assisted procedures.

## Solution

- OpenCode as the AI IDE: Adopted OpenCode as the primary AI-powered development environment, running directly in the terminal with full access to the filesystem, git, shell, and the model's tool-calling abilities.
- Codebase-Aware Chat and Editing: OpenCode reads the repository, understands file structure and symbols, and can open, edit, create, and delete files through natural language — no context copying required.
- Subagent Delegation: Complex work is split into parallel subagents (explore for codebase research, general for multi-step tasks), each with fresh context, so large refactors and investigations proceed without losing focus.
- Skill System for Reusable AI Workflows: Installed and authored skills (OpenCode, Report) that encapsulate prompt templates, tool permissions, and procedure, turning ad hoc AI assistance into repeatable, team-shared workflows.
- MCP Tool Integration: Connected OpenCode to MCP servers so the AI can read local documentation, query project resources, and act on external systems without leaving the IDE.
- Session Management for Long-Running Work: Used session move, rename, and worktree commands to keep long-running AI-assisted projects organized across branches and directories without losing conversation context.
- Provider and Model Flexibility: Configured OpenCode against multiple providers and models, selecting the best model per task (fast models for edits, capable models for architecture) while keeping a single consistent interface.
- Local-First and Scriptable: All interactions run through a CLI and JavaScript runtime, so AI-assisted work can be scripted, reviewed in git, and integrated into CI without a proprietary GUI lock-in.

## Skills

- AI Engineering
- Platform Engineering
- Developer Experience
- DevOps

## Tools

- OpenCode
- Git
- Model Context Protocol (MCP)
- Large Language Models (LLM)
- Terminal / Shell

## Why This Matters

Treating the IDE as an AI agent rather than a chat sidebar changes the development loop: the AI can execute commands, run tests, navigate git history, and edit across multiple files autonomously under developer supervision. The result is faster delivery, more consistent code quality, and AI assistance that scales from individual tasks to team-wide skills.
