
# Test unitaire de la fonction jeton
def test_jeton():
    grille = [
        [1, -1, -1, -1, -1, -1, -1],
        [0,  1, -1, -1, -1, -1, -1],
        [0,  0,  1, -1, -1, -1, -1],
        [0,  0,  0,  1, -1, -1, -1],
        [0,  0,  0,  0,  0, -1, -1],
        [0,  0,  0,  0,  0,  0, -1]
    ]
    assert jeton(1, 3, 3, -1, -1, grille) == 3
    assert jeton(1, 2, 2, 1, 1, grille) == 3
    assert jeton(0, 0, 1, 1, 0, grille) == 0

# Test unitaire de la fonction coup_gagnant
def test_coup_gagnant():
    grille = [
        [1,  1,  1, -1, -1, -1, -1],
        [0,  0,  0, -1, -1, -1, -1],
        [0,  0,  0, -1, -1, -1, -1],
        [0,  0,  0,  0,  0, -1, -1],
        [0,  0,  0,  0,  0, -1, -1],
        [0,  0,  0,  0,  0,  0, -1]
    ]
    assert coup_gagnant(1, 0, 0, grille) == True
    assert coup_gagnant(0, 0, 0, grille) == False

# Test unitaire de la fonction changer_joueur
def test_changer_joueur():
    assert changer_joueur(0) == 1
    assert changer_joueur(1) == 0

# Test d'intégration du programme principal
def test_programme_principal():
    with patch.object(sys, 'argv', ['main.py']):
        construire_gui()
        # Tester l'interface graphique est difficile sans fenêtre graphique
        # On ne peut pas faire de test de bouton sans simulation de clics
