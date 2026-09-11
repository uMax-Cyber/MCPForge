[English](README.md) | [Русский](README.ru.md)

# MCP Infrastructure Toolkit
[![CI](https://github.com/uMax-Cyber/MCPForge/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/MCPForge/actions/workflows/ci.yml)

Architecture patterns and safety frameworks for running Model Context Protocol (MCP) servers against production infrastructure (firewalls, network controllers, hypervisors). Built from real deployments: 6 MCP servers, 312 tools, full-access mode with guardrails.

## The Problem

MCP servers give AI agents direct access to production infrastructure. Without structure, weak LLMs hallucinate parameters, mix data from different sources, and can't distinguish errors from data. This toolkit provides the patterns that make it safe.

## Key Patterns

### 1. Routed-Tool Pattern (for large tool catalogs)
When a server has 200+ tools, don't show them all to the LLM. Instead:
```
route_tools(query="list VMs") → returns relevant tool names
call_routed_tool(name="list_vms", arguments={...})
```
This collapses 200 tools into 3 visible ones, saving context window.

### 2. Safety Tiers (autonomy levels)
```
🟢 GREEN — read/list/status: do freely
🟡 YELLOW — delete/rollback/resize: confirm with user first
🔴 RED — critical infrastructure (agent's own host): NEVER
```

### 3. Dual-Fallback Memory
Primary: RAG server (semantic search)
Fallback: File-based markdown vault (grep search)
Interface: single script that handles both, always writes to both.

### 4. Anti-Hallucination Rules for MCP
- Data only from actual tool results
- Error ≠ data (report error, don't invent plausible numbers)
- Truncated output ≠ complete data
- Don't mix facts from different VLANs/sources without verification
- Tool result > model's "knowledge"

## Architecture

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   AI Agent  │────▶│  MCP Servers ×6  │────▶│  Infrastructure │
│  (Hermes)   │◀────│  (312 tools)      │◀────│  (Proxmox/UniFi/ │
└─────────────┘     └──────────────────┘     │   Sophos/LightRAG)│
                           │                 └─────────────────┘
                           ▼
                    ┌──────────────┐
                    │ Safety Layer │
                    │ (tiers+rules)│
                    └──────────────┘
```

## Config Examples

- `config/mcp_servers.yaml` — multi-server configuration with env vars
- `config/safety_rules.yaml` — per-tier action classification
- `examples/routed_pattern.py` — routed-tool call sequence

## Real Metrics

| Metric | Value |
|--------|-------|
| MCP servers | 6 (unifi, proxmox×3, sophos×2) |
| Total tools | 312 |
| Tools per server (routed) | 3 visible |
| Safety violations after training | 0/8 tests |
| Hallucination rate after training | 0% (8/8 tests passed) |

## License
MIT
