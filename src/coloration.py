import streamlit as st
import networkx
from generation_graphe import *

colors_dict = {
                "rouge_vif": "#FF0000", "vert_vif": "#00FF00", "bleu_vif": "#0000FF",
                "jaune": "#FFFF00", "orange": "#FFA500", "violet": "#800080",
                "rose": "#FFC0CB", "marron": "#800000", "noir": "#000000", "blanc": "#FFFFFF",
                "bleu_clair": "#ADD8E6", "vert_clair": "#90EE90", "rose_clair": "#FFB6C1",
                "kaki": "#F0E68C", "lavande": "#E6E6FA", "beige": "#F5F5DC",
                "cyan": "#00FFFF", "magenta": "#FF00FF", "bleu_fonce": "#00008B",
                "vert_fonce": "#006400", "rouge_fonce": "#8B0000", "marine": "#000080",
                "bordeaux": "#800000", "indigo": "#4B0082", "olive": "#808000",
                "sarcelle": "#008080", "or": "#FFD700", "corail": "#FF7F50",
                "cramoisi": "#DC143C", "turquoise": "#40E0D0"
            }

def coloration_graph():
    colors = list(colors_dict.values())
    length = len(colors)
    
    if len(st.session_state.graph.nodes) == 0:
        st.error("Entrez le nombre n des noeuds dans la panneau latérale gauche")
        return 

    if nx.is_connected(st.session_state.graph):
        for node in st.session_state.graph.nodes:
            index = 0

            voisin_couleur = [st.session_state.graph.nodes[voisin].get("color") for voisin in st.session_state.graph.neighbors(node)]

            while colors[index % length] in voisin_couleur:
                index += 1 
            st.session_state.graph.nodes[node]["color"] = colors[index % length]