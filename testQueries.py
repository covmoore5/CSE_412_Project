import queryScripts as qs

rows = qs.find_ind_for_med('penicillin')

for row in rows:
    print(row[0])