import random

manche = 1
score_ordinateur = 0
score_joueur = 0

# saisie du nom du joueur
print("le nom par défaut est Joueur. Si vous voulez le nom par défaut: laissez vide et taper sur Entrer")
nom_joueur = input("Saisissez votre nom\n>")
if not nom_joueur:
	nom_joueur = "Joueur"

# saisie du nombre de Manche
nombre_manche = int(input("Combien de manche voulez-vous jouer?(le nombre doit etre superieur à 0)\n>"))
while nombre_manche<1:
	print("Le nombre de manches est incorrect: doit etre superieur à 0")
	nombre_manche = int(input("Combien de manche voulez-vous jouer?(le nombre doit etre superieur à 0)\n>"))

while manche<=nombre_manche:
	# numéro de la manche
	print("Manche ",manche)

	# tour de l'ordinateur
	choix_ordinateur = int(random.random()*3)

	# tour du joueur
	choix_joueur = int(input("Que choisissez-vous([0]Pierre [1]Feuille [2]Ciseaux [3]Quitter)\n>"))
	while choix_joueur<0 or choix_joueur>3:
		print("Le choix du joueur doit etre compris entre 0 et 3 inclus")
		choix_joueur = int(input("Que choisissez-vous([0]Pierre [1]Feuille [2]Ciseaux [3]Quitter)\n>"))

	if choix_joueur==3:
		print("Au revoir!")
		exit()
	# comparaison des choix du joueur et de l'ordinateur
	if choix_joueur==choix_ordinateur:
		print("EGALITE! Vous devez recommencer la manche")
	else:
		# on incremente le nombre de manche
		manche=manche+1
		# cas où le joueur gagne la manche
		if choix_joueur==0 and choix_ordinateur==2:
			print("La Pierre casse les ciseaux!Vous avez gagné la manche")
			score_joueur=score_joueur+1
		elif choix_joueur==1 and choix_ordinateur==0:
			print("La feuille recouvre la pierre!Vous avez gagné la manche")
			score_joueur=score_joueur+1
		elif choix_joueur==2 and choix_ordinateur==1:
			print("Les ciseaux coupent la feuille!Vous avez gagné la manche")
			score_joueur=score_joueur+1
		# cas où le joueur perd la manche
		else:
			if choix_joueur==2 and choix_ordinateur==0:
				print("La Pierre casse les ciseaux!L'ordinateur a gagné la manche")
			elif choix_joueur==0 and choix_ordinateur==1:
				print("La feuille recouvre la pierre!L'ordinateur a gagné la manche")
			elif choix_joueur==1 and choix_ordinateur==2:
				print("Les ciseaux coupent la feuille!L'ordinateur a gagné la manche")
			score_ordinateur=score_ordinateur+1

	# on affiche les scores
	print("Score:",nom_joueur,"=",score_joueur," ordinateur=",score_ordinateur)

# on affiche le vainqueur de la partie
if score_joueur>=score_ordinateur:
	print("Vous etes le GRAND vainqueur du CHIFUMI!")
else:
	print("Vous avez perdu la partie! La prochaine sera peut-etre la bonne!")
