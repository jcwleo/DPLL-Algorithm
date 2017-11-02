# input_cnf = ['!P Q', '!Q R', 'S !R !P', 'P']
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


def unit_prop(cnf, liters):
    cnf = list(set(cnf))
    delete_list = []
    flag = True
    print(cnf)
    for i in range(len(cnf)):
        if ' ' not in cnf[i]:  # unit이 있는지 없는지 확인
            flag = False
            if '!' in cnf[i]:
                liters[cnf[i][1:]] = False
                del liters[cnf[i][1:]]
                for j in range(len(cnf)):
                    if cnf[i] in cnf[j]:
                        delete_list.append(j)
                    elif cnf[i][1:] in cnf[j]:
                        if len(cnf) == 2:
                            return ([False])
                        cnf[j] = cnf[j].replace(cnf[i][1:],' ')
                        while cnf[j].find('  ') >= 0:
                            cnf[j] = cnf[j].replace('  ',' ')
                        cnf[j] = cnf[j].strip(' ')

            else:
                liters[cnf[i]] = True
                del liters[cnf[i]]
                for j in range(len(cnf)):
                    if cnf[i] in cnf[j] and '!'+cnf[i] not in cnf[j]:
                        delete_list.append(j)
                    elif '!'+cnf[i] in cnf[j]:
                        if len(cnf) == 2:
                            return ([False])
                        cnf[j] = cnf[j].replace('!'+cnf[i],' ')
                        while cnf[j].find('  ') >= 0:
                            cnf[j] = cnf[j].replace('  ',' ')
                        cnf[j] = cnf[j].strip(' ')

            idx = 0
            for k in range(len(delete_list)):
                del cnf[delete_list[k]-idx]
                idx += 1
            break

    if flag is False:
        print(liters)
        dpll(cnf, liters)

    return cnf


def splitting(cnf, liters):
    delete_list = []
    i = 0
    j=0
    k=0

    return cnf


def dpll(cnf, liters):
    if cnf == []:
        print('satis')
        return True
    cnf = unit_prop(cnf, liters)
    if False in cnf:
        print('unsatis')
    cnf = splitting(cnf, liters)

    return False


def main():
    input_cnf = open('input2.txt', 'r').read()
    liters, cnf = preproc(input_cnf)
    result = dpll(cnf, liters)


if __name__ == '__main__':
    main()
