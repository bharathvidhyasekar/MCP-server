import sys
from mcp.server.fastmcp import FastMCP
from service.auth_service import user_login
from service.summary_service import get_summary

# logging to stderr (important for MCP stdio servers)
def log(msg):
    print(msg, file=sys.stderr, flush=True)

log("Starting automation MCP server...")

mcp = FastMCP("automation-mcp")

@mcp.tool()
def login(email: str, password: str):
    return user_login(email, password)

log("User login tool registered")

@mcp.tool()
def get_campaign_summary():
    return get_summary()

log("Campaign summary tool registered")

if __name__ == "__main__":
    log("Starting automation MCP server...")
    mcp.run()
    log("Automation MCP server stopped")