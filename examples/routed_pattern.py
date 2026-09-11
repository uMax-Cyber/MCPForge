#!/usr/bin/env python3
"""Example: correct routed-tool call pattern for large MCP servers."""
import json

# WRONG: calling 200+ tools directly exhausts context
# RIGHT: use routed pattern

# Step 1: Route to find the right tool
route_result = call_tool("route_tools", {
    "query": "list all virtual machines on node"
})
# Returns: ["list_vms", "get_vm_status", ...]

# Step 2: Call the routed tool with exact name from result
vm_list = call_tool("call_routed_tool", {
    "name": "list_vms",  # exact name from route_tools result
    "arguments": {"node": "node1"}
})

# Step 3: Read the FULL result (don't count from truncated output)
for vm in vm_list["data"]:
    print(f"VM {vm['vmid']}: {vm['name']} ({vm['status']})")

# NEVER:
# - Call call_routed_tool with a name you guessed
# - Skip route_tools and call proxmox_api_raw directly
# - Use the wrong server instance (node1 tools for node2 questions)
