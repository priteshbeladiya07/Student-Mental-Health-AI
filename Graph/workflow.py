from langgraph.graph import StateGraph, START, END

from Graph.state import StudentState
from Graph.nodes import (
    ml_prediction,
    classify_risk,
    generate_response,
    group_country_node
)

builder = StateGraph(StudentState)
builder.add_node("group_country", group_country_node)
builder.add_node("ml_prediction", ml_prediction)
builder.add_node("classify_risk", classify_risk)
builder.add_node("generate_response", generate_response)

builder.add_edge(START, "group_country")
builder.add_edge("group_country", "ml_prediction")
builder.add_edge("ml_prediction", "classify_risk")
builder.add_edge("classify_risk", "generate_response")
builder.add_edge("generate_response", END)

graph = builder.compile()