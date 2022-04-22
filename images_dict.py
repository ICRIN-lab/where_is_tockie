# diocq est un variable qui contient un dictionnaire structuré comme suit :
# les clés correspondent au numéro des images
# les valeurs sont des listes qui contiennent 3 éléments ou plus :
# - integer : le type d'image (0 : image simple avec question(s), 1: 5 images d'affilés, 2: images pour les 7 différences)
# - integer ou float : le nombre de seconde où l'image apparait
# - Une ou plusieurs liste de string de 2 élements qui contiennent la question et la touche de la bonne réponse.
dic = {

    0: [3,
        [["Combien y a-t-il de personnes sur cette photo ? \n\n 9 / 15",
          ['a', '0']],

         ["Combien y a-t-il de cafetières sur la photo ? \n\n 7 / 2",
          ['p', '6']]]
        ],

    1: [3,
        [["Combien y a-t-il de personnes sur cette photo ? \n\n 4 / 8",
          ['a', '0']]]
        ],

    2: [6,
        [["Combien y a-t-il de personnes assises sur cette photo ? \n\n 2 / 4",
          ['a', '0']],

         ["Combien y a-t-il de personnes sur cette photo ? \n\n 12 / 22",
          ['a', '0']],

         ["Avez-vous vu une personne habillée d'une robe blanche ? \n\n Non / Oui",
          ['a', '0']]]
        ],

    3: [3,
        [["Combien y a-t-il de personnes sur cette photo ? \n\n 4 / 3",
          ['p', '6']],

         ["Avez-vous vu une corde à sauter ? \n\n Non / Oui",
          ['p', '6']]]
        ],

    4: [2,
        [["Combien y a-t-il de personnes sur cette photo ? \n\n 4 / 3",
          ['a', '0']],

         ["Avez-vous vu une balle sur cette photo ? \n\n Non / Oui",
          ['p', '6']],

         ["Avez-vous vu une corde à sauter ? \n\n Non / Oui",
          ['p', '6']]]
        ],

    5: [3,
        [["Toutes les personnes sont-elles habillées en blanc ? \n\n Non / Oui",
          ['a', '0']],

         ["Combien y a-t-il de personnes sur cette photo ? \n\n 20 / 40",
          ['a', '0']]]

        ],

    6: [6,
        [["Combien y a-t-il de personnes diplomées sur la photo ? \n\n 39 / 82",
          ['a', '0']],

         ["Avez-vous vu une personne habillée d'une robe blanche ? \n\n Non / Oui",
          ['a', '0']]]
        ],

    7: [3,
        [["Combien y a-t-il de drapeaux sur cette photo ? \n\n 4 / 5",
          ['a', '0']],

         ["Le nom inscrit sur la première tombe est : \n\n JACKSON / JOHNSON",
          ['a', '0']]]

        ],

    8: [5,
        [["De quelle couleur est le téléphone ? \n\n bleu / rose",
          ['a', '0']]]

        ],

    9: [4,
        [["Combien y a-t-il de femmes en bas à gauche de l'image ? \n\n 2 / 4",
          ['p', '6']],

         ["Avez-vous vu un point rouge sur cette photo ? \n\n Non / Oui",
          ['a', '0']]]

        ],

    10: [3,
         [["Tous les personnages ont-ils un casque ? \n\n Non / Oui",
           ['p', '6']],

          ["Combien y a-t-il de personnages sur cette photo ? \n\n 55 / 100",
           ['a', '0']]]

         ],

    11: [4,
         [["Combien y a-t-il de personnages sur cette photo ? \n\n 1 / 2",
           ['a', '0']],

          ["Avez-vous vu des tâches de peinture sur le véhicule ? \n\n Non / Oui ",
           ['p', '6']],

          ["Avez-vous vu des pots de peinture sur le capot du véhicule ? \n\n Non / Oui",
           ['p', '6']]]
         ],

    12: [2,
         [["Combien y a-t-il de personnages sur cette photo ? \n\n  2 / 4",
           ['a', '0']]]

         ],

    13: [8,
         [["Combien y a-t-il de personnages sur cette photo ? \n\n 2 / 3",
           ['p', '6']],

          ["La pièce est-elle rangée ? \n\n Non / Oui ",
           ['a', '0']],

          ["Combien y a-t-il de posters sur les murs ? \n\n 9 / 21",
           ['a', '0']],

          ["Avez-vous remarqué des vêtements qui ne sont pas pliés ? \n\n Non / Oui",
           ['p', '6']]]
         ],

    14: [8,
         [["Avez-vous vu des mouchoirs usagés ? \n\n Non / Oui",
           ['p', '6']],

          ["Avez-vous vu une éponge ?\n\n Non / Oui",
           ['p', '6']],

          ["Avez-vous vu des serviettes usagées ?\n\n Non / Oui",
           ['p', '6']],

          ["Les rebords de la fenêtre sont-ils propres ? \n\n Non / Oui",
           ['a', '0']]]
         ],

    15: [8,
         [["Avez-vous vu une pile de livres sur la droite de l'image ? \n\n Non / Oui",
           ['p', '6']],

          ["Avez-vous vu un ceintre sur la gauche de l'image ? \n\n Non / Oui ",
           ['p', '6']]]

         ],

    16: [8,
         [["Combien y a-t-il de tasses sur cette photo ? \n\n 21 / 4",
           ['p', '6']],

          ["Avez-vous vu du linge sale sur cette photo ? \n\n Non / Oui ",
           ['p', '6']],

          ["Avez-vous vu des restes alimentaires sur cette photo ? \n\n Non / Oui",
           ['a', '0']]]
         ],

    17: [4,
         [["Combien avez-vous vu de pinguins sur cette photo ? \n\n  24 / 12",
           ['p', '6']]],
         ],

    18: [5,
         [["Combien avez-vous vu d'humains sur cette photo ? \n\n  2 / 4",
           ['a', '0']],

          ["Il y a moins de trente moutons sur l'image. \n\n Faux / Vrai",
           ['a', '0']]]
         ],

    19: [5,
         [["Il y a plus de 7 tentacules visibles. \n\n  Faux / Vrai", ['p', '6']],
          ["Il y a autant de tentacules de part et d'autre du clocher. \n\n  Faux / Vrai", ['p', '6']]]
         ],

    20: [6,
         [["Il y a autant de grands arbres à gauche qu'à droite. \n\n  Faux / Vrai", ['a', '0']],
          ["La calèche est tirée par deux chevaux. \n\n  Faux / Vrai", ['a', '0']],
          ["On peut apercevoir un clocher. \n\n  Faux / Vrai ", ['a', '0']]]
         ],

    21: [4,
         [["Les toits sont bleus. \n\n  Faux / Vrai", ['p', '6']]]
         ],

    22: [7,
         [["Il y a 5 bateaux. \n\n  Faux / Vrai", ['p', '6']],
          ["Il y a  des bateaux a 2 voiles. \n\n  Faux / Vrai", ['p', '6']],
          ["On peut voir un chien. \n\n  Faux / Vrai", ['a', '0']]]
         ],

    23: [4,
         [["Toutes les lunes sont dans le même sens. \n\n  Faux / Vrai", ['a', '0']]]
         ],

    24: [8,
         [["Les tapis sont alignés. \n\n  Faux / Vrai", ['a', '0']],
          ["Il y a une brosse à dent près du lit. \n\n  Faux / Vrai", ['a', '0']],
          ["L'armoire est ouverte. \n\n Faux / Vrai", ['a', '0']]]
         ],

    25: [4,
         [["Il y a plus de 10 pommes.\n\n Faux / Vrai", ['a', '0']]]
         ],

    26: [4,
         [["Les costumes sont identiques. \n\n  Faux / Vrai", ['p', '6']]]
         ],

    27: [4,
         [["Les éléphants sont parfaitement symétriques. \n\n  Faux / Vrai", ['a', '0']]]
         ],

    28: [4, [["Les toits sont à la même hauteur. \n\n  Faux / Vrai", ['a', '0']]]
         ],

    29: [4, [["Le deuxième éléphant porte une pyramide.  \n\n  Faux / Vrai", ['p', '6']]]
         ],

    30: [6, [["Il y a plus de 30 papillons.  \n\n  Faux / Vrai ", ['a', '0']]]
         ],

    31: [6, [["Il y a du maïs sur l'image. \n\n Faux / Vrai", ['p', '6']],
             ["Au moins deux poires figurent sur l'image. \n\n Faux / Vrai", ['p', '6']]]
         ]
}
