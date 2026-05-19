import streamlit as st
from mcp.server.fastmcp import FastMCP
import random
import datetime

# Create MCP Server
mcp = FastMCP("SimpleMCP")


# MCP Tool
@mcp.tool()
def hello(name: str) -> str:

    return f"Hello {name}"


@mcp.tool()
def generate_password(length: int = 8) -> str:

    chars = "abcdefghijklmnopqrstuvwxyz123456789"

    password = "".join(random.choice(chars) for _ in range(length))

    return password


@mcp.tool()
def current_time() -> str:

    return str(datetime.datetime.now())


# Streamlit UI
st.title("Simple MCP Demo")

st.subheader("Hello Tool")

name = st.text_input("Enter Name")

if st.button("Say Hello"):

    result = hello(name)

    st.success(result)


st.subheader("Password Generator")

length = st.slider("Password Length", 4, 20, 8)

if st.button("Generate Password"):

    password = generate_password(length)

    st.code(password)


st.subheader("Current Time")

if st.button("Get Time"):

    st.info(current_time())
