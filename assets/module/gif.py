from random import choice

async def random_hug():
    hugs = ['https://media.giphy.com/media/ZBQhoZC0nqknSviPqT/giphy.gif',
            'https://media.giphy.com/media/8tpiC1JAYVMFq/giphy.gif',
            'https://media.giphy.com/media/2GnS81AihShS8/giphy.gif',
            'https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif',
            'https://media.giphy.com/media/Bj9k1U69GZ8Iw/giphy.gif',
            'https://media.giphy.com/media/117o9BJASzmLNC/giphy.gif',
            'https://media.giphy.com/media/OiKAQbQEQItxK/giphy.gif',
            'https://media.giphy.com/media/l0MYLJKRmFCZbJyo0/giphy.gif',
            'https://media.giphy.com/media/EvYHHSntaIl5m/giphy.gif',
            'https://media.giphy.com/media/llmZp6fCVb4ju/giphy.gif',
            'https://media.giphy.com/media/QbkL9WuorOlgI/giphy.gif',
            'https://media.giphy.com/media/THmLt0Cf02EXcPGDV1/giphy.gif']
    return choice(hugs)

async def random_cooki():
    cookies =  ['https://media.giphy.com/media/CoWGqp7Q7mx8c/giphy.gif',
                'https://media.giphy.com/media/l3vRmjIZpfYp8MLwA/giphy.gif',
                'https://media.giphy.com/media/3o7aTqv1Cnk4OtIC52/giphy.gif',
                'https://media.giphy.com/media/l0HlyXQUez0jHop2g/giphy.gif',
                'https://media.giphy.com/media/54ZRhrb6hl15lK9nZk/giphy.gif',
                'https://media.giphy.com/media/Y09s2Frxp7wpBGXTyt/giphy.gif',
                'https://media.giphy.com/media/59Ve1fnBdol8c/giphy.gif',
                'https://media.giphy.com/media/4ji2aiquPipy0/giphy.gif']
    return choice(cookies)

async def random_punish():
    punishs =  ['https://media.giphy.com/media/3XlEk2RxPS1m8/giphy.gif',
                'https://media.giphy.com/media/1zgOyLCRxCmV5G3GFZ/giphy.gif',
                'https://media.giphy.com/media/w5FSoU86sXRFm/giphy.gif',
                'https://media.giphy.com/media/l2YOqzhYD066fAd56/giphy.gif',
                'https://media.giphy.com/media/jt38YxwGTevEkFWWoY/giphy.gif',
                'https://media.giphy.com/media/tV0HkQju9zHR6/giphy.gif']
    return choice(punishs)

async def random_award():
    medals =   ['https://media.giphy.com/media/BMt31oekjIG4V8jFhE/giphy.gif',
    			'https://media.giphy.com/media/iDJrIOR9kHTtfnEcHO/giphy.gif',
    			'https://media.giphy.com/media/26gseSequdPcy37l6/giphy.gif',
    			'https://media.giphy.com/media/WspL0mgECSKQOK6tTf/giphy.gif',
    			'https://media.giphy.com/media/ngyRZcPbJim4g/giphy.gif',
    			'https://media.giphy.com/media/pOcTaM6LgFOH45AvKL/giphy.gif']
    return choice(medals)
