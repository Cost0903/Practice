import re

with open('smbios_dt7.txt', 'r') as fin:
    smbios_dt7 = fin.readlines()
    result = ""
    for i in range(len(smbios_dt7)):
        if "L2" in smbios_dt7[i]: 
            for j in range(i,len(smbios_dt7)):
                if "Maximum amount" in smbios_dt7[j]:
                    result = "".join(smbios_dt7[j].split(":")[-1:]).strip().split(" ")[0]
                    print(F'L2_cache_MB = {result} MB')
                    print(F'L2_cache_KB = {float(result) * 1024} KB')
                    break
