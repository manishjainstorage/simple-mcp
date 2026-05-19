from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
import uvicorn

# Create FastAPI app
app = FastAPI()

# Create MCP server
mcp = FastMCP("SimpleMCP")


# MCP Tool
@mcp.tool()
def hello(name: str) -> str:
    """
    Simple hello tool
    """

    return f"Hello {name}"


# Mount MCP endpoint
app.mount("/mcp", mcp.sse_app())


# Root route
@app.get("/")
def home():

    return {
        "message": "MCP Server Running"
    }


# Run locally
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
