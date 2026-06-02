from generation_graphe import *
from pyvis.network import Network
import os

def display_graphe():
    if len(st.session_state.graph.nodes) > 0:
        net = Network()
        net.from_nx(st.session_state.graph)
        net.toggle_physics(False)
        html_file = net.generate_html()
        components.html(html_file, height=600)
    else:
        st.info("Le graphe est vide. Veuillez utiliser le panneau latérale à gauche pour ajouter des noeuds et des liens")