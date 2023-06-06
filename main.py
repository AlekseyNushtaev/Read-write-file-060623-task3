file_dict = {}
for number in range(1, 4):
    with open(f'{number}.txt', 'rt', encoding='utf-8') as file:
        content_list = [number] + file.readlines()
        file_dict[len(content_list)] = content_list
sorted_list = sorted(file_dict.items())
with open('res.txt', 'w', encoding='utf-8') as file:
    for one_file in sorted_list:
        file.writelines([f'{one_file[1][0]}.txt\n', f'{one_file[0] - 1}\n'] + one_file[1][1:] + ['\n'])

