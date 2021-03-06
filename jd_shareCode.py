#!/usr/bin/python
import re
import json

JD_COOKIE = '- JD_COOKIE='
PLANT_BEAN_SHARECODES = '- PLANT_BEAN_SHARECODES='
FRUITSHARECODES = '- FRUITSHARECODES='
PETSHARECODES = '- PETSHARECODES='
DDFACTORY_SHARECODES = '- DDFACTORY_SHARECODES='
DREAM_FACTORY_SHARE_CODES = '- DREAM_FACTORY_SHARE_CODES='
JDZZ_SHARECODES = '- JDZZ_SHARECODES='
JDJOY_SHARECODES = '- JDJOY_SHARECODES='

with open("jd_shareCode.json", 'r') as load_f:
    load_dict = json.load(load_f)

own = load_dict['own']
frd = load_dict['frd']

# get JD_COOKIE
for i in range(len(own)):
    if i >= 1:
        JD_COOKIE = JD_COOKIE + '&'
    pt_key = 'pt_key=' + own[i]['pt_key'] + ';'
    pt_pin = 'pt_pin=' + own[i]['pt_pin'] + ';'
    JD_COOKIE = JD_COOKIE + pt_key + pt_pin


def sort(parameter):
    parameter = re.sub(r'@+', "@", parameter)
    parameter = re.sub(r'&+', "&", parameter)
    parameter = parameter.replace('@&', '&')
    parameter = parameter.strip('@')

    return parameter


def get_finalcode(parameter):
    # get full code
    all_code = ''
    final_code = ''
    for j in range(len(own)):
        if j >= 1:
            all_code = all_code + '@'
        all_code = all_code + own[j][parameter]

    for j in range(len(frd)):
        all_code = all_code + '@' + frd[j][parameter]
    # combine all code
    for j in range(len(own)):
        if j >= 1:
            final_code = final_code + '&'
        final_code = final_code + all_code.replace(own[j][parameter], '')

    return sort(final_code)


PLANT_BEAN_SHARECODES = PLANT_BEAN_SHARECODES + get_finalcode('beans')
FRUITSHARECODES = FRUITSHARECODES + get_finalcode('fruits')
PETSHARECODES = PETSHARECODES + get_finalcode('pets')
DDFACTORY_SHARECODES = DDFACTORY_SHARECODES + get_finalcode('dd_factory')
DREAM_FACTORY_SHARE_CODES = DREAM_FACTORY_SHARE_CODES + get_finalcode('jx_factory')
JDZZ_SHARECODES = JDZZ_SHARECODES + get_finalcode('makemoney')
JDJOY_SHARECODES = JDJOY_SHARECODES + get_finalcode('crazyjoy')

# finish and print
print(JD_COOKIE)
print(PLANT_BEAN_SHARECODES)
print(FRUITSHARECODES)
print(PETSHARECODES)
print(DDFACTORY_SHARECODES)
print(DREAM_FACTORY_SHARE_CODES)
print(JDZZ_SHARECODES)
print(JDJOY_SHARECODES)
