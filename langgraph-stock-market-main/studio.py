from agent import studio_entry, graph
# from langgraph.sdk import GraphSpec
# 
def run(question: str) -> str:
    return studio_entry(question)

# graph_spec = GraphSpec(
#     name="StockMarketRAG",
#     graph=graph,
#     entrypoint="llm"
# )
