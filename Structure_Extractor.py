
def extractor(text):
    text = text.split(".")
    connector = {}
    liste_connecteur = ["is", "used in", "such as","for","comme","tel que","est","sont","pour","dans"]
    for i in text:
        sujet = None
        for connecteur in liste_connecteur:
            if connecteur in i:
                partie_gauche,partie_droite= i.split(connecteur,1)
                if sujet is None:
                    sujet = partie_gauche.strip()
                    if not sujet:
                            continue
                valeur = partie_droite.strip()
                for c in liste_connecteur:
                    if c in valeur:
                        valeur = valeur.split(c,1)[0].strip()
                if sujet is None:
                    continue
                if sujet not in connector:
                    connector[sujet] = {} 
                if connecteur not in connector[sujet]:
                    connector[sujet][connecteur] = []
                connector[sujet][connecteur].append(valeur)
    return connector

