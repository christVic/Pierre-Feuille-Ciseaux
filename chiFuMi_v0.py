import random

nombre_manche = 3
manche = 1
score_ordinateur = 0
score_joueur = 0

while manche<=nombre_manche:
	# affichage du numéro de la manche
	print("Manche ",manche)

	# tour de l'ordinateur
	choix_ordinateur = int(random.random()*3)

	# tour du joueur
	choix_joueur = int(input("Que choisissez-vous(0=pierre, 1=feuille ou 2=ciseaux)\n>"))

	# verification du choix du joueur
	if choix_joueur>=3:
		choix_joueur = 2
	if choix_joueur<0:
		choix_joueur = 0

	# comparaison des choix du joueur et de l'ordinateur
	if choix_joueur==choix_ordinateur:
		print("EGALITE! Vous devez recommencer la manche")
	else:
		# on diminue le nombre de manche de 1
		manche=manche+1

		# cas où le joueur gagne la manche
		if (choix_joueur==0 and choix_ordinateur==2) or (choix_joueur==1 and choix_ordinateur==0) or (choix_joueur==2 and choix_ordinateur==1):
			print("Vous avez gagné la manche")
			score_joueur=score_joueur+1
		# cas où le joueur perd la manche
		else:
			print("Vous avez perdu la manche")
			score_ordinateur=score_ordinateur+1

	# on affiche les scores
	print("Score: joueur=",score_joueur," ordinateur=",score_ordinateur)

# on affiche le vainqueur de la partie
if score_joueur>=score_ordinateur:
	print("Vous etes le GRAND vainqueur du CHIFUMI!")
else:
	print("Vous avez perdu la partie! La prochaine sera peut-etre la bonne!")
