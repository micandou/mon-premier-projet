import os

# Demande à l'utilisateur un message de commit
message = input("Entrez votre message de commit : ")

# Étapes Git
os.system("git add .")
os.system(f'git commit -m "{message}"')
os.system("git push origin main")
