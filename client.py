import asyncio
import sys
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters


async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["server.py"]
    )
    # start MCP server process
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            print("Initilizing session...")
            await session.initialize()
            print("Session initialized")
            print("Calling login user tool...")
            result = await session.call_tool(
                "login_user",
                {
                    "email": "sanjay@stellarglobal.co",
                    "password": "Admin@123"
                }
            )
            print("Tool returned response:")
            print(result)

if __name__ == "__main__":
    print("Starting automation MCP client...")
    asyncio.run(main())
    print("Automation MCP client stopped")