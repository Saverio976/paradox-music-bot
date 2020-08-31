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

def rdbRss():
    return os_environ["ATLAS_TOKKEN"]


def dictReactionEvent():
    dico = {
        712712646679461909 : {
            710426812878028800 : 712707532484902973,
            710426857618800641 : 712703925303771239,
            710426899951648821 : 712713065279520808
        },
        715179823420538901 : {
            '🇦' : 715209808977985537,
            '🇧' : 715209890490220675,
            '🇨' : 715209935734046761,
            '🇩' : 715209966402666558
        },
        715181000841494539 : {
            '🇫' : 715573301182988288,
            '🇬' : 715573350998474854,
            '🇭' : 715573666884222976,
            '🇮' : 715573706545692703,
            '🇯' : 715573762103443456,
            '🇰' : 715573815035428874,
            '🇱' : 715573866608459787,
            '🇲' : 715573913408634992,
            '🇳' : 715573967636660265
        }
    }
    return dico

def discord_tokken():
    return os_environ["DISCORD_TOKKEN"]
