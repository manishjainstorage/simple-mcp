from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
import uvicorn
import os

# FastAPI App
app = FastAPI()

# MCP Server
mcp = FastMCP("SimpleMCP")


# MCP Tool
@mcp.tool()
def hello(name: str) -> str:

    return f"Hello {name}"


# MCP Endpoint
app.mount("/mcp", mcp.sse_app())


# Root Endpoint
@app.get("/")
def home():

    return {
        "message": "MCP Running Successfully"
    }


# Railway Startup
if __name__ == "__main__":

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )
