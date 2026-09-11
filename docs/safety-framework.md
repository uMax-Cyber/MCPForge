# MCP Safety Framework

## Autonomy Tiers

### 🟢 GREEN — Autonomous (no confirmation needed)
- Read/inspect: list, status, config, logs, statistics
- Start/resume a VM or service
- Create a snapshot
- Clone to a new ID (non-destructive)

### 🟡 YELLOW — Confirm First
- Delete/destroy a VM, disk, or snapshot
- Rollback/restore (discards current state)
- Resize (especially shrink = data loss)
- Any firewall rule change
- Any DHCP scope modification

### 🔴 RED — NEVER (no exceptions)
- Agent's own host VM (destroying it kills the agent)
- Wiping production data disks
- Force-push to main branch
- Any action that orphans the agent

## Anti-Hallucination Rules (the 9)

1. Data only from real tool results
2. Error ≠ data — report error, don't invent plausible numbers
3. Truncated/paginated output ≠ complete — read all pages or use summary endpoints
4. Don't mix facts from different sources/VLANs without verifying they belong together
5. Don't cache "facts" between tool calls — re-verify
6. Don't substitute plausible answers when tool fails
7. Don't infer topology from partial data
8. Tool result always beats model's internal "knowledge"
9. If capability doesn't exist, say so — don't substitute the task

## Validation Results (from 36-test suite)

| Domain | Tests | Pass Rate |
|--------|-------|-----------|
| Network (UniFi) | 15 | 100% |
| Sysadmin (Proxmox) | 6 | 100% |
| Safety guards | 2 | 100% (refused destructive) |
| Memory (RAG) | 2 | 100% |
| Anti-hallucination | 4 | 100% (no fabricated data) |
| Tool discovery | 2 | 100% |
| Delegation | 3 | 100% |
