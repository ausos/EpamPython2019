""""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt -
в нем содержится таблица переводов кодонов РНК в аминокислоту,
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что,
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""

# read the file dna.fasta
with open('./files/dna.fasta', 'r') as file:
    dna = {}
    for line in file:
        if line.startswith('>'):
            dna_key = line.strip()
            dna[dna_key] = []
        else:
            dna[dna_key].append(line.strip())

with open('./files/rna_codon_table.txt') as file:
    codon_table = file.read().split()


def translate_from_dna_to_rna(dna):
    transcription = {'A': 'U',
                     'C': 'G',
                     'T': 'A',
                     'G': 'C'}

    rna = {}
    for key in dna:
        rna_key = key
        rna[rna_key] = []
        for line in dna[key]:
            rna[rna_key].append(''.join(transcription[elem] for elem in line))

    return rna


def count_nucleotides(dna):
    num_of_nucleotides = []

    for key in dna:
        num_of_nucleotides.append(key)
        value = ''
        for line in dna[key]:
            value = value + line
        num_of_nucleotides.append('A: {}'.format(value.count('A')))
        num_of_nucleotides.append('C: {}'.format(value.count('C')))
        num_of_nucleotides.append('G: {}'.format(value.count('G')))
        num_of_nucleotides.append('T: {}'.format(value.count('T')))

    return num_of_nucleotides


def translate_rna_to_protein(rna):

    codon_transcription = dict(zip(codon_table[::2], codon_table[1::2]))
    triplet_function = lambda x, n=3: [x[i:i+n] for i in range(0, len(x), n)]

    protein = {}
    for key in rna:
        protein_key = key
        protein[key] = []
        for line in rna[key]:
            line = triplet_function(line)
            for triplet in line:
                if len(triplet) == 3:
                    protein[key].append(codon_transcription[triplet])
                else:
                    None
        protein[key] = ''.join(protein[key])

    return protein


print('Cтатистика по количеству нуклеотидов в ДНК :\n')
print(count_nucleotides(dna))
print('\n\nПоследовательность РНК для каждого гена : \n')
print(translate_from_dna_to_rna(dna))
rna = translate_from_dna_to_rna(dna)
print('\n\nПоследовательность кодонов для каждого гена: \n')
print(translate_rna_to_protein(rna))
