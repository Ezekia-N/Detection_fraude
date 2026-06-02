from generation_graphe import *

def find_clique():
    graphe = st.session_state.graph
    cliques = []

    for node_init in graphe.nodes:
        current_clique = [node_init]

        colors_init = graphe.nodes[node_init].get("color")
        colors_in_clique = [colors_init]
        
        for other_node in graphe.nodes:
            color_other = graphe.nodes[other_node].get("color")
            if other_node == node_init or color_other in colors_in_clique:
                continue 
                
            connect_to_all = True
            for node_clique in current_clique:
                if not graphe.has_edge(other_node, node_clique):
                    connect_to_all = False
                    break
            
            if connect_to_all:
                current_clique.append(other_node)
                colors_in_clique.append(color_other)

        current_clique.sort()
        
        if len(current_clique) >= 3 and current_clique not in cliques:
            cliques.append(current_clique)

    return cliques