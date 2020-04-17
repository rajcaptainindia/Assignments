#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    P= patient_medical_speciality_list.count('P')
    O=  patient_medical_speciality_list.count('O')
    E= patient_medical_speciality_list.count('E')
    if(P>E and P>O):
        return medical_speciality['P']
    elif(E>P and E>O):
        return medical_speciality['E']
    else:
        return medical_speciality['O']

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'E',302, 'E' ,305, 'P' ,401, 'O' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
