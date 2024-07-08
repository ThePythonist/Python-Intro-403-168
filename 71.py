users = {
    "09936256040": "30 rooze 10gig",
    "09126030255": "10 rooze 10gig",
    "09922101617": "1 rooze 1gig",
    "09124223020": "30 rooze 15gig",
}

msg = """
moshtarake gerami {} shoma 85% basteye
{} khod ra masraf kardid.
"""

for x,y in users.items():
    print(msg.format(x,y))
