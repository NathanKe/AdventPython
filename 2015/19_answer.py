import re
import itertools
import random

rule_text = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg""".splitlines()

base_molecule = "CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl"


def line_to_tuple(l):
    m = re.search(r"^(.+?)\s=>\s(.+?)$", l)
    return m[1], m[2]


rule_tuples = list(map(line_to_tuple, rule_text))


def apply_all_rules(s):
    non_unique_results = []
    for rule in rule_tuples:
        finds = re.finditer(rule[0], s)
        for find in finds:
            left = s[:find.start()]
            right = s[find.end():]
            non_unique_results.append(left + rule[1] + right)
    return list(set(non_unique_results))


print('Part 1: ', len(apply_all_rules(base_molecule)))


def apply_random_rule_repeatedly(s, d, a):
    a += 1
    random.shuffle(rule_tuples)
    rule = rule_tuples[0]
    while True:
        prev_s = s
        s = s.replace(rule[1], rule[0], 1)
        if prev_s == s:
            break
        else:
            d += 1
    return s, d, a


x = (base_molecule, 0, 0)

while x[0] != 'e':
    x = apply_random_rule_repeatedly(*x)
    if x[2] > 1000:
        print("reset!")
        x = (base_molecule, 0, 0)

print('Part 2: ', x[1])
