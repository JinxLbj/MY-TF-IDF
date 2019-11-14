import jieba
import sys
import os
import math

target_path = sys.argv[1]
all_path = sys.argv[2]

def getWordList(path):
    f = open(path)
    content = f.read()
    after_cut = jieba.cut(content)
    all_dict = {}
    total_num = 0
    for key in after_cut:
        if key in all_dict:
            all_dict[key] = all_dict[key] + 1
        else:
            all_dict[key] = 1
        total_num += 1
    return all_dict, total_num


def ifExist(dict):
    all_num = 0
    all_dict = {}
    files = os.listdir(all_path)
    for i in files:
        all_num += 1
        res = getWordList(all_path + "/" + i)
        after_cut = res[0]
        for this_key in dict:
            for all_key in after_cut:
                print(this_key)
                print(all_key)
                if this_key == all_key:
                    if this_key in all_dict:
                        all_dict[this_key] += 1
                    else:
                        all_dict[this_key] = 1
                    break
    return all_dict, all_num

this_res = getWordList(target_path)
this_dict = this_res[0]
this_num = this_res[1]

this_frequency = {}
for key in this_dict:
    this_frequency[key] = this_dict[key] / this_num

total_res = ifExist(this_dict)
all_dict = total_res[0]
all_num = total_res[1]

result = {}
for key in this_frequency:
    idf = 0
    if key in all_dict:
        idf = math.log(all_num / all_dict[key] + 1)
    else:
        idf = math.log(all_num / 1)
    result[key] = this_frequency[key] * idf

sorted_result = sorted(result.keys(), reverse=True)
print(sorted_result)
