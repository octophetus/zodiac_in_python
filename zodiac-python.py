#Get the user's birthday:

birth_month = input("What is your month of birth? Please use numbers:  ")
try:
    birth_month = int(birth_month)
    assert birth_month >= 1 and birth_month <= 12
except:
    print("Please enter a valid number!")
    exit()

birth_day = int(input("What is the date of your birth?:  "))
try:
    birth_day = int(birth_day)
    assert birth_day >= 1 and birth_day <= 31
except:
    print("Please enter a valid number!")
    exit()

birth_year = input("What is your birth year? Please use 4 numbers e.g. 1989:  ")
try:
    birth_year = int(birth_year)
    assert birth_year >= 1920
except:
    print("Please enter a valid number!")
    exit()

print(f"Your date of birth is: {birth_month}/{birth_day}/{birth_year}")



#What kind of reading do they want?:

reading_type = input("What would you like to know? \nFor Western Zodiac, enter 1 \nFor Chinese Zodiac, enter 2 \nTo know your gemstone, enter 3:    ")
try:
    assert reading_type == "1" or reading_type == "2" or reading_type == "3"
    reading_type = int(reading_type)

except:
    print("Please enter a valid number!")
    exit()



#Western Zodiac Option:
def get_western_sign(month, day):
    western_sign = ""
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 22) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 22):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"



western_readings = {
    "Aries": "You are an Aries ♈ 🐏\nAries people are creative, adaptive, and insightful. They can also be strong-willed and spontaneous (sometimes to a fault). Aries people can be driven and are very ambitious often making them over-achievers in anything they set their mind to tackle. Aries are fire signs, and so too is their personality. They may be quick to anger, but don’t take it personally, it’s just their fiery, passionate personalities showing through. Aries signs have excellent sense of humor and they get along with almost everyone at the party (and they DO know how to party). Aries can be impatient, but we love them anyway because they are devoted friends, lovers and family members – they are loyal to then end and will fight for their causes (usually supporting the underdog).\n",
    "Taurus": "You are a Taurus ♉ 🐂\nTaurus zodiac signs and meanings, like the animal that represents them, is all about strength, stamina and will. Stubborn by nature, the Taurus will stand his/her ground to the bitter end (sometimes even irrationally so). But that’s okay because the Taurus is also a loving, sympathetic and appreciative sign. The Taurus is very understanding and when we need someone to unburden ourselves to, we often share our deepest fears with the Taurians of the zodiac. Taurians are very patient, practical and efficient, they are excellent in matters of business and are also wonderful instructors/teachers. Although initially they may have their own best interest at heart, they are ultimately and endlessly generous with their time, possessions and love.\n",
    "Gemini": "You are a Gemini ♊ 👬\nFlexibility, balance and adaptability are the keywords for the Gemini. They are quick to grasp the meaning of a situation and act on it, often with positive effects. They tend to have a duality to their nature, and can sometimes be tough to predict how they will react. They can turn from hot to cold and may be prone to noticeable mood swings. However, they are generous signs with tendencies of being affectionate, and imaginative. They also inspire others easily as they seem to naturally motivate themselves – their charisma and accomplishments are infectious. Geminians are very supportive, and are especially good at promotions, sales, and driving hard bargains.\n",
    "Cancer": "You are a Cancer ♋ 🦀\nCancerians love home-life, family and domestic settings. They are traditionalists, and enjoy operating on a fundamental level. They love history, and are fascinated with the beginnings of things (heraldry, ancestry, etc.). The moon is their ruler, so they can be a bit of a contradiction and sometimes moody. However, they are conservative, so they’ll be apt to hide their moods from others altogether. They have a reputation for being fickle, but they’ll tell you that isn’t true, and it’s not. Cancerians make loyal, sympathetic friends. However Cancerians need alone time, and when they retreat, let them do so on their terms.\n",
    "Leo": "You are a Leo ♌ 🦁\nThe zodiac signs and meanings of Leo is about expanse, power and exuberance. Leos are natural born leaders, and they will let you know it as they have a tendency to be high-minded and vocal about their opinions. That’s okay because if you observe, the Leo is usually correct in his/her statements. Leos have a savvy way of analyzing a situation and executing swift judgment with a beneficial outcome. It comes from being a leader. They are brave, intuitive, and also head-strong and willful. Beneath their dynamic persona lies a generous, loving, sensitive nature that they do not easily share with others. They might be a bit bossy, but those who know them understand this comes from a source need to do good not (usually) from an inflated ego.\n",
    "Virgo": "You are a Virgo ♍ 👧\nVirgos have keen minds, and are delightful to chat with, often convincing others of outlandish tales with ease and charm. Virgos are inquisitive and are very skilled at drawing information from people. This trait also makes them naturally intuitive. Combine this with their remarkable memories, and we see an advanced, analytical personality. However the Virgo needs balance in their lives otherwise they may become short-tempered, impatient and self-serving. Virgos are excellent teammates in work and social activities. They work well with others, although they freely express their opinions (even when unwarranted).\n",
    "Libra": "You are a Libra ♎ ⚖ \nAs their zodiac signs and meanings would indicate, Libras are all about balance, justice, equanimity and stability. They easily surround themselves with harmony and beauty, but sometimes go to extremes to do so if their goals are unreasonable or unhealthy. With Venus as their ruling planet, Libras are very understanding, caring, and often the champion of underdogs. They have keen intuitions, but often don’t give themselves enough credit for their perceptions. They can be quiet and shy if not persuaded to come out of their shell. Ironically and in spite of their introverted nature they make excellent debaters, often proving a point from out of seemingly nowhere.\n",
    "Scorpio": "You are a Scorpio ♏ 🦂 \nThe Scorpio is often misunderstood. These personalities are bold and are capable of executing massive enterprises with cool control and confidence. They can surmount seemingly all obstacles when they put their mind to the task and they have unshakable focus when the situation calls for it. Regardless of their bold nature, they are often secretive, but they are always observing behind their withdrawn manner.\n",
    "Sagittarius": "You are a Sagittarius ♐ 🏹 \nHere we have the philosopher among the zodiac signs and meanings. Like the Scorpio, they have great ability for focus, and can be very intense. However, they must channel their energy or they will waste time and wear themselves out going in too many directions at once. They are not very patient and expect quick results. However, when encountered with failure they make extreme comebacks often against incredible odds. They make loyal friends and lovers, but they do not handle commitment well as they refuse to be tied down while chasing philosophical pursuits.\n",
    "Capricorn": "You are a Capricorn ♑ 🐐 \nCapricorns are philosophical signs and are highly intelligent, too. They apply their knowledge to practical matters, and strive to maintain stability and order. They are good organizers, and they achieve their goals by purposeful, systematic means. They are very intuitive, although they don’t share this trait with others freely. They do not deal well with opposition or criticism but a healthy Capricorn will often shrug off negative comments towards their character. They are patient and persevering – they know they can accomplish any task as long as they follow a their plan step-by-step. Capricorns have broad shoulders, and typically take on others' problems with aplomb. Ironically, they rarely share their own problems and tend to go through bouts of inner gloom after a spell of dwelling on these problems.\n",
    "Aquarius": "You are an Aquarius ♒ 🏺 \nOften simple and unassuming, the Aquarian goes about accomplishing goals in quiet, often unorthodox ways. Although their methods may be unorthodox, the results for achievement are surprisingly effective. Aquarians will take up any cause, and are humanitarians of the zodiac. They are honest, loyal and highly intelligent. They are also easy going and make natural friendships. If not kept in check, the Aquarian can be prone to sloth and laziness. However, they know this about themselves, and try their best to motivate themselves to action. They are also prone to philosophical thoughts, and are often quite artistic and poetic.\n",
    "Pisces": "You are a Pisces ♓ 🐟 \nUnassuming in presentation, the Pisces zodiac signs and meanings deal with acquiring vast amounts of knowledge, but you would never know it. They keep an extremely low profile compared to others in the zodiac. They are honest, unselfish, trustworthy and often have quiet dispositions. They can be overcautious and sometimes gullible. These qualities can cause the Pisces to be taken advantage of, which is unfortunate as this sign is beautifully gentle, and generous. In the end, however, the Pisces is often the victor of ill circumstance because of his/her intense determination. They become passionately devoted to a cause – particularly if they are championing for friends or family.\n"
}

if reading_type == 1:
    western_sign = get_western_sign(birth_month, birth_day)
    print(western_readings[western_sign])



#Eastern Zodiac Option:

def get_eastern_sign(y):
    if (y == 1924 or y == 1936 or y == 1948 or y == 1960 or y == 1972 or y == 1984 or y == 1996 or y == 2008 or y == 2020 or y == 2032):
        return "Rat"
    elif (y == 1925 or y == 1937 or y == 1949 or y == 1961 or y == 1973 or y == 1985 or y == 1997 or y == 2009 or y == 2021 or y == 2033):
        return "Ox"
    elif (y == 1926 or y == 1938 or y == 1950 or y == 1962 or y == 1974 or y == 1986 or y == 1998 or y == 2010 or y == 2022 or y == 2034):
        return "Tiger"
    elif (y == 1927 or y == 1939 or y == 1951 or y == 1963 or y == 1975 or y == 1987 or y == 1998 or y == 2011 or y == 2023 or y == 2035):
        return "Rabbit"
    elif (y == 1928 or y == 1940 or y == 1952 or y == 1964 or y == 1976 or y == 1988 or y == 1999 or y == 2012 or y == 2024 or y == 2036):
        return "Dragon"
    elif (y == 1929 or y == 1941 or y == 1953 or y == 1965 or y == 1977 or y == 1989 or y == 2000 or y == 2013 or y == 2025 or y == 2037):
        return "Snake"
    elif (y == 1930 or y == 1942 or y == 1954 or y == 1966 or y == 1978 or y == 1990 or y == 2001 or y == 2014 or y == 2026 or y == 2038):
        return "Horse"
    elif (y == 1931 or y == 1943 or y == 1955 or y == 1967 or y == 1979 or y == 1991 or y == 2002 or y == 2015 or y == 2027 or y == 2039):
        return "Goat"
    elif (y == 1932 or y == 1944 or y == 1956 or y == 1968 or y == 1980 or y == 1992 or y == 2003 or y == 2016 or y == 2028 or y == 2040):
        return "Monkey"
    elif (y == 1933 or y == 1945 or y == 1957 or y == 1969 or y == 1981 or y == 1993 or y == 2004 or y == 2017 or y == 2029 or y == 2041):
        return "Rooster"
    elif (y == 1934 or y == 1946 or y == 1958 or y == 1970 or y == 1982 or y == 1994 or y == 2005 or y == 2018 or y == 2030 or y == 2042):
        return "Dog"
    else:
        return "Pig"

eastern_readings = {
    "Rat": "Your animal is the rat 🐀\nQuick-witted, resourceful, versatile, kind\n",
    "Ox": "Your animal is the ox 🐂\nDiligent, dependable, strong, determined\n",
    "Tiger": "Your animal is the tiger 🐯\nBrave, confident, competitive\n",
    "Rabbit": "Your animal is the rabbit 🐇\nQuiet, elegant, kind, responsible\n",
    "Dragon": "Your animal is the dragon 🐉\nConfident, intelligent, enthusiastic\n",
    "Snake": "Your animal is the snake 🐍\nEnigmatic, intelligent, wise\n",
    "Horse": "Your animal is the horse  🐴\nAnimated, active, energetic\n",
    "Goat": "Your animal is the goat 🐐\nCalm, gentle, sympathetic\n",
    "Monkey": "Your animal is the monkey 🐒\nSharp, smart, curiosity\n",
    "Rooster": "Your animal is the rooster 🐓\nObservant, hardworking, courageous\n",
    "Dog": "Your animal is the dog 🐶.\nLovely, honest, prudent\n",
    "Pig": "Your animal is the pig 🐖.\nCompassionate, generous, diligent\n"
}

if reading_type == 2:
    eastern_sign = get_eastern_sign(birth_year)
    print(eastern_readings[eastern_sign])



#Birthstones Option:

birthstones = ("Garnet 🔴", "Amethyst 🟣", "Aquamarine 🌐", "Diamond 💎", "Emerald 🟢", "Pearl 🦪", "Ruby 🔴", "Peridot 🔴", "Sapphire 🔵", "Opal ⚪", "Topaz 🟡", "Turquoise 🔵")

if reading_type == 3:
    user_birthstone = birthstones[birth_month -1]
    print(f"Your birthstone is: {user_birthstone}")

if reading_type == 1 or reading_type == 2:
    print("May you have good fortune! 🔮")