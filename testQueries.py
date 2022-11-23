import queryScripts as qs

# rows = qs.find_ind_for_med('penicillin')

# for row in rows:
#     print(row[0])

# rows = qs.find_se_for_med('trandolapril')

# for row in rows:
#     print(row[0])

# rows = qs.get_all_patients()

# for row in rows:
#     print(row[0])

rows = qs.find_patient_presc('Martin,Madaline')

for row in rows:
    print(row[0])