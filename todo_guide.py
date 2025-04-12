import json
import os

FILENAME = "todolist.json"

# Charger les tâches depuis le fichier JSON
def charger_taches():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

# Sauvegarder les tâches dans le fichier JSON
def sauvegarder_taches(taches):
    with open(FILENAME, "w") as f:
        json.dump(taches, f, indent=4)

# Afficher les tâches
def afficher_taches(taches):
    if not taches:
        print("📭 Aucune tâche pour l’instant.")
        return
    for i, tache in enumerate(taches):
        statut = "✅" if tache["faite"] else "🕐"
        print(f"{i + 1}. {statut} {tache['titre']}")

# Ajouter une tâche
def ajouter_tache(taches):
    titre = input("Que veux-tu ajouter ? ")
    taches.append({"titre": titre, "faite": False})
    print("➕ Tâche ajoutée.")

# Marquer une tâche comme faite
def marquer_tache_faite(taches):
    afficher_taches(taches)
    try:
        index = int(input("Numéro de la tâche à cocher : ")) - 1
        if 0 <= index < len(taches):
            taches[index]["faite"] = True
            print("☑️ Tâche marquée comme faite.")
    except ValueError:
        print("⛔ Numéro invalide.")

# Supprimer une tâche
def supprimer_tache(taches):
    afficher_taches(taches)
    try:
        index = int(input("Numéro de la tâche à supprimer : ")) - 1
        if 0 <= index < len(taches):
            taches.pop(index)
            print("🗑️ Tâche supprimée.")
    except ValueError:
        print("⛔ Numéro invalide.")

# Menu principal
def menu():
    taches = charger_taches()
    while True:
        print("\n📋 Menu Todo List")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Marquer une tâche comme faite")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        choix = input("👉 Choisis une option : ")

        if choix == "1":
            afficher_taches(taches)
        elif choix == "2":
            ajouter_tache(taches)
        elif choix == "3":
            marquer_tache_faite(taches)
        elif choix == "4":
            supprimer_tache(taches)
        elif choix == "5":
            sauvegarder_taches(taches)
            print("💾 Liste sauvegardée. À bientôt ! 👋")
            break
        else:
            print("❗ Choix invalide.")

if __name__ == "__main__":
    menu()
