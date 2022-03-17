

'''names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]'''


'''def assign_person_to_job(names, jobs):
'''

def person(names, jobs):
    x = {}

    for i, e in enumerate(names):
        y = jobs[i]
        x[e] = y



    return x

'''def person(names, jobs):
   return list(zip(names, jobs))'''










print(person( ["Dennis", "Vera", "Mabel", "Annette", "Sussan"], ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"] ))
