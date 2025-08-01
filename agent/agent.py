"""Agent that leverages Perplexity tools for research."""
from agents import Agent
from prompts import Prompts
# from utils import file_tools, perplexity, ask_user, playstore
from tools import research, file_tools

# search_assistant = Agent('Search Assistant', Prompts.search, tools=[research.internet_search, research.internet_deep_search, research.internet_reasoned_search, file_tools.read_file, file_tools.write_file, file_tools.append_file, file_tools.delete_file, file_tools.list_files])
assistant = Agent('Rick', Prompts.assistant, tools=[research.internet_search, research.internet_deep_search, research.internet_reasoned_search, file_tools.read_file, file_tools.write_file, file_tools.append_file, file_tools.delete_file, file_tools.list_files])

# search_tool = search_assistant.as_tool(
#     tool_name="search",
#     tool_description="""# Search Tool
#     Use this tool to search the internet for information.""",
# )

# assistant = Agent('Assistant', Prompts.assistant, tools=[search_tool, file_tools.read_file, file_tools.write_file, file_tools.append_file, file_tools.delete_file, file_tools.list_files,])
