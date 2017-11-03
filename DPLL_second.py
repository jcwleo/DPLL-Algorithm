def preproc(input_cnf):
    liters = list(set(input_cnf))
    if '!' in liters:
        liters.remove('!')
    if '\n' in liters:
        liters.remove('\n')
    if ' ' in liters:
        liters.remove(' ')
    liters = dict(zip(liters, [False] * len(liters)))
    input_cnf = input_cnf.splitlines()
    print('--------------------------------------------------')
    print('CNF : ', input_cnf)
    print('Liters : ', liters)
    print('--------------------------------------------------')
    return liters, input_cnf

def dpll(cnf, liters):
    # unit prop
    while True:
        if len(liters) == 1 and len(cnf) > 1:
            print('--------------------------------------------------')
            print(cnf)
            print(liters)
            break

        delete_list = []
        unit_clause = None
        cnf = list(set(cnf))
        print('--------------------------------------------------')
        print(cnf)
        print(liters)

        for i in range(len(cnf)):
            if ' ' not in cnf[i]:
                unit_clause = cnf[i]
                print('Unit : ', unit_clause)
                del cnf[i]
                break

        if unit_clause and '!' not in unit_clause:
            del liters[unit_clause]
            for j in range(len(cnf)):
                if '!' + unit_clause in cnf[j]:
                    cnf[j]= cnf[j].replace('!'+unit_clause,' ')
                    cnf[j] = cnf[j].strip(' ')
                elif unit_clause in cnf[j]:
                    delete_list.append(j)

            for index in sorted(delete_list, reverse=True):
                del cnf[index]

        elif unit_clause and '!' in unit_clause:
            del liters[unit_clause.replace('!','')]
            for j in range(len(cnf)):
                if unit_clause in cnf[j]:
                    delete_list.append(j)
                elif unit_clause.replace('!','') in cnf[j]:
                    cnf[j] = cnf[j].replace(unit_clause.replace('!','') , ' ')
                    cnf[j] = cnf[j].strip(' ')
            for index in sorted(delete_list, reverse=True):
                del cnf[index]

        else:
            break

    ##
    if cnf == []:
        return 'Satis'
    elif len(liters) == 1 and len(cnf) > 1:
        return 'UnSatis'


def main():
    input_cnf = open('input.txt', 'r').read()
    liters, cnf = preproc(input_cnf)
    print(dpll(cnf,liters))
    pass

if __name__ == '__main__':
    main()