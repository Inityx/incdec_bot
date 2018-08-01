ROTATE_MAX_CHARS = 15

SUBGROUPS = {
    'EE': ['DiddleDad', 'fgsrfug', 'Selfishshellfish', 'aaronschraner'],
    'CS': ['tolvstaa', 'Codification', 'codysseus'],
    'CH': ['TheChemE'],
    'BO': [r'adny_bot'],
    'AN': [r'adny_bot', 'TheChemE', 'tolvstaa'],
    'CO': ['Codification', 'codysseus'],
    'GR': ['tolvstaa', 'Codification'],
    'NE': ['irandms'],
}

all_users = [user for group in SUBGROUPS.values() for user in group]
all_users = list(set(all_users))

SUBGROUPS['AL'] = all_users
SUBGROUPS['EV'] = SUBGROUPS['AL']
