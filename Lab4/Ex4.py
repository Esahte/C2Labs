mp_affiliation = {'GB': 'ALP', 'BS': 'UPP', 'JP': 'UPP', 'HL': 'ALP', 'KL': 'UPP', 'TP': 'KKK', 'GDP': 'KKK'}
party_size = {'ALP': 0, 'UPP': 0}
for (k, v) in mp_affiliation.items():
    if v in party_size.keys():
        party_size[v] += 1
    else:
        party_size[v] = 1


print(party_size)
# print(mp_affiliation.get('JP'))
# print(mp_affiliation)


