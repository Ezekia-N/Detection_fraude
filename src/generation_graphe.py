import streamlit as st
import networkx as nx
import streamlit.components.v1 as components
import random

def graphe_init():
    if "graph" not in st.session_state:
        st.session_state.graph = nx.Graph()

    # Initialiser le numéro de noeud
    if "node_number" not in st.session_state:
        st.session_state.node_number = 1

def node_construction():
    st.sidebar.subheader("Génération des noeuds")
    node_number = st.sidebar.text_input("Entrez le nombre de noeud : ")

    if not node_number.isdigit():
        st.sidebar.error("Veuillez entrer un nombre entier")
        return 
    
    node_number = int(node_number)

    if st.sidebar.button("Créer les noeuds"):
        st.session_state.graph.clear()
        st.session_state.node_number = 1
        for i in range(1, node_number + 1):
            st.session_state.graph.add_node(f"{st.session_state.node_number}")
            st.session_state.node_number += 1
        st.toast(f"{node_number} noeuds créés avec succès !")

    # Initialisation de couleur
    for node in st.session_state.graph.nodes:
        st.session_state.graph.nodes[node]["color"] = ""

def edge_construction():
    st.sidebar.subheader("Ajout de liens selon la probabilité")
    proba_link = st.sidebar.text_input("Entrez la probabilité de lien : ")

    try:
        proba_link = float(proba_link)
        if not (0 <= proba_link <= 1):
            st.sidebar.error("La probabilité doit être compris entre 0 et 1")
            return 
    except ValueError:
        st.sidebar.error("Veuillez entrer un nombre décimale entre 0 et 1")
        return

    if st.sidebar.button("Générer les liens"):
        st.session_state.graph.clear_edges()
        node  = list(st.session_state.graph.nodes)
        node_number = len(node)

        if node_number < 2:
            st.sidebar.warning("Il faut au moins 2 noeuds pour créer des liens")
            return 
        
        graph_connexe = False
        tentative = 0

        while not graph_connexe and tentative < 10:
            tentative += 1
            for i in range(node_number-1):
                for j in range(i+1, node_number):
                    node1 = node[i]
                    node2 = node[j]
                    if not st.session_state.graph.has_edge(node1, node2):
                        if random.random() < proba_link:
                            st.session_state.graph.add_edge(node1, node2)

            if nx.is_connected(st.session_state.graph):
                graph_connexe = True
                st.toast(f"C'est un graphe connexe avec {tentative} tentative")

        if tentative == 10:
            st.info("Veuillez accroître le lien probabiliste pour établir un graphe connexe") 
            return   