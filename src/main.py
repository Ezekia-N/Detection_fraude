from generation_graphe import *
from coloration import * 
from detection_clique import *
from affichage import *

if __name__ == '__main__':
    st.set_page_config(layout='wide')
    st.title("Detection fraude")
    st.sidebar.title("Configuration")
    graphe_init()
    node_construction()
    edge_construction()

    st.subheader("Coloration de graphe")
    if st.button("Colorier le graphe"):
        coloration_graph()

    st.subheader("Recherche des cliques de ce graphe")
    if st.button("Trouver les cliques dans le graphe"):
        cliques = find_clique()
        
        if cliques:
            st.subheader("Classification des cliques détéctés")
            st.success(f"Nombre de cliques trouvées : {len(cliques)}")
            for index, clique in enumerate(cliques, 1):
                st.write(f"Clique {index} : {', '.join(clique)}")
        else:
            st.info("Aucune clique trouvée.")
    
    display_graphe()