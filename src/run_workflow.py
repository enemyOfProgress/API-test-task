import networkx as nx
import requests
from matplotlib import pyplot as plt

main_url = "http://127.0.0.1:8000/"


def run_workflow(workflow_id: int):
    all_nodes_url = main_url + "node/v1/all"
    response = requests.get(all_nodes_url)
    nodes = response.json()

    # Create direction graph
    G = nx.DiGraph()

    # Create node in direction graph with links
    for node in nodes:
        if node["workflow_id"] == workflow_id:
            G.add_node(node["node_name"], text=node["text"], status=node["status"], condition=node["condition"])
            if node["source"] is not None:
                G.add_edge(u_of_edge=node["source"], v_of_edge=node["target"])


run_workflow(3)
