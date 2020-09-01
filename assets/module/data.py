from os import environ as os_environ

def rss_data():
    dico = {
        'franceinfo' : {
            'name_media' : 'France Info',
            'urls' : {
                'https://www.francetvinfo.fr/politique.rss' : 'theme-politique',
                'https://www.francetvinfo.fr/societe/justice.rss' : 'theme-justice',
                'https://www.francetvinfo.fr/monde/europe.rss' : 'theme-monde',
                'https://www.francetvinfo.fr/economie/bourse/marches.rss' : 'theme-economique',
                'https://www.francetvinfo.fr/sciences.rss' : 'theme-sciences',
                'https://www.francetvinfo.fr/sante.rss' : 'theme-santé',
                'https://www.francetvinfo.fr/culture/cinema.rss' : 'theme-culture'
            }
        },
        'bfmtv' : {
            'name_media' : 'BFMTV',
            'urls' : {
                'https://www.bfmtv.com/rss/international/' : 'theme-monde',
                'https://www.bfmtv.com/rss/politique/' : 'theme-politique',
                'https://www.bfmtv.com/rss/economie/actualite/' : 'theme-economique',
                'https://hightech.bfmtv.com/rss/internet/' : 'theme-numérique',
                'https://hightech.bfmtv.com/rss/logiciel/' : 'theme-numérique'
            }
        },
        'lemonde' : {
            'name_media' : 'le Monde',
            'urls' : {
                'https://www.lemonde.fr/international/rss_full.xml' : 'theme-monde',
                'https://www.lemonde.fr/politique/rss_full.xml' : 'theme-politique',
                'https://www.lemonde.fr/justice/rss_full.xml' : 'theme-justice',
                'https://www.lemonde.fr/education/rss_full.xml' : 'theme-education',
                'https://www.lemonde.fr/argent/rss_full.xml' : 'theme-economique',
                'https://www.lemonde.fr/cinema/rss_full.xml' : 'theme-culturel',
                'https://www.lemonde.fr/arts/rss_full.xml' : 'theme-culturel',
                'https://www.lemonde.fr/medecine/rss_full.xml' : 'theme-santé',
                'https://www.lemonde.fr/physique/rss_full.xml' : 'theme-sciences'
            }
        },
        'lefigaro' : {
            'name_media' : 'le Figaro',
            'urls' : {
                'https://www.lefigaro.fr/rss/figaro_politique.xml' : 'theme-politique',
                'https://www.lefigaro.fr/rss/figaro_international.xml' : 'theme-monde',
                'https://www.lefigaro.fr/rss/figaro_sante.xml' : 'theme-santé',
                'https://www.lefigaro.fr/rss/figaro_bourse.xml' : 'theme-economique',
                'https://www.lefigaro.fr/rss/figaro_emploi.xml' : 'theme-economique',
                'https://www.lefigaro.fr/rss/figaro_cinema.xml' : 'theme-culturel',
                'https://www.lefigaro.fr/rss/figaro_arts-expositions.xml' : 'theme-culturel'
            }
        },
        'afp' : {
            'name_media' : 'AFP',
            'urls' : {
                'https://news.google.com/rss/search?q=source:AFP&um=1&ie=UTF-8&num=100&hl=fr&gl=FR&ceid=FR:fr' : None
            }
        }
    }
    return dico

def dictReactionEvent():
    dico = {
        750038972063023215 : {
            710426812878028800 : 712707532484902973
        },
        750038974395056257 : {
            710426857618800641 : 712703925303771239
        },
        750038976122978416 : {
            710426899951648821 : 712713065279520808
        },
        750038977582596147 : {
            '🇦' : 715209808977985537
        },
        750038992396746783 : {
            '🇧' : 715209890490220675
        },
        750038994385109052 : {
            '🇨' : 715209935734046761
        },
        750038996331003964 : {
            '🇩' : 715209966402666558
        },
        750038998029697136 : {
            '🇫' : 715573301182988288
        },
        750039000164859954 : {
            '🇬' : 715573350998474854
        },
        750039014484082810 : {
            '🇭' : 715573666884222976
        },
        750039016531034133 : {
            '🇮' : 715573706545692703
        },
        750039018506289316 : {
            '🇯' : 715573762103443456
        },
        750039020553371762 : {
            '🇰' : 715573815035428874
        },
        750039022646067280 : {
            '🇱' : 715573866608459787
        },
        750039036906831983 : {
            '🇲' : 715573913408634992
        },
        750039038462787665 : {
            '🇳' : 715573967636660265
        },
        750039040610402455 : {
            '👩‍💼' : 750041489458856037
        },
        750039042392981504 : {
            '🆒' : 712704072884682773
        }
    }
    return dico

async def get_a_role_messages():
    # for cogs/get_a_role.py
    l = [   "Pour voir la partie tri par média réagissez avec :salameche:",
            "Pour voir la partie tri par thème réagissez avec :salameche_2:",
            "Pour voir en plus l'AFP (ceux qui choisisse que par thème, l'AFP n'y sera pas dans ce pack) réagissez avec :salameche_3:",
            "Vous pouvez aussi choisir par médias :\n:regional_indicator_a:  pour #franceinfo",
            ":regional_indicator_b:  pour #bfmtv",
            ":regional_indicator_c:  pour #lemonde",
            ":regional_indicator_d:  pour #lefigaro",
            "Ou par thèmes :\n:regional_indicator_f:  pour le #theme-politique",
            ":regional_indicator_g:  pour le #theme-economique",
            ":regional_indicator_h:  pour le #theme-monde",
            ":regional_indicator_i:  pour le #theme-culture",
            ":regional_indicator_j:  pour le #theme-justice",
            ":regional_indicator_k:  pour le #theme-santé",
            ":regional_indicator_l:  pour le #theme-sciences",
            ":regional_indicator_m:  pour le #theme-numérique",
            ":regional_indicator_n:  pour le #theme-education",
            "If you come for professional purpose : 👩‍💼",
            "If you come for fun purpose : 🆒"]
    e = [   ':salameche:', ':salameche_2:', ':salameche_3:',
            '🇦', '🇧', '🇨', '🇩', '🇫', '🇬', '🇭',
            '🇮', '🇯', '🇰', '🇱', '🇲', '🇳', '👩‍💼', '🆒']

    return l, e

def rdbRss():
    return os_environ["ATLAS_TOKKEN"]

def discord_tokken():
    return os_environ["DISCORD_TOKKEN"]
