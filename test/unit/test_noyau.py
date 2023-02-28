import pytest

from noyau import *

def test_changer_joueur():
   assert True==True

def test_jeton():
    grille = [[0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0]]
    joueur = 1
    # test avec une seule case occupée par le joueur
    assert jeton(joueur, 0, 0, 1, 0, grille) == 1
    assert jeton(joueur, 0, 0, 0, 1, grille) == 1
    assert jeton(joueur, 0, 0, 1, 1, grille) == 1
    assert jeton(joueur, 0, 0, 1, -1, grille) == 1
    #

def test_maj_jeu():
    grille = [[-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1],
              [-1,-1,-1,-1,-1,-1,-1]]

    niveau = [6,6,6,6,6,6,6]

    # joueur 1 joue la case 00
    joueur = 1
    case = 'b0'
    maj_jeu(case, grille, niveau, joueur)
    assert grille == [[-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [1 ,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1]]
    assert niveau == [5,6,6,6,6,6,6]

    # joueur 0 joue la case 01
    joueur = 0
    case = 'b1'
    maj_jeu(case, grille, niveau, joueur)
    assert grille == [[-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [1 ,0 ,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1]]
    assert niveau == [5,5,6,6,6,6,6]

    # joueur 1 joue la case 11
    joueur = 1
    case = 'b1'
    maj_jeu(case, grille, niveau, joueur)
    assert grille == [[-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1],
                      [1 ,0 ,1 ,-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1,-1]]
    assert niveau == [5,4,6,6,6,6,6]