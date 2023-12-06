with open('test.txt', 'w', encoding="utf-8") as f:
    with open('1.txt', 'r', encoding='utf-8') as f1:
        with open('2.txt', 'r', encoding='utf-8') as f2:
            with open('3.txt', 'r', encoding='utf-8') as f3:
#
                lines_1 = f1.readlines()
                len_1 = len(lines_1)
                lines_2 = f2.readlines()
                len_2 = len(lines_2)
                lines_3 = f3.readlines()
                len_3 = len(lines_3)
                lines_list = []
                lines_list.append(len_1)
                lines_list.append(len_2)
                lines_list.append(len_3)
                lines_list.sort()
                for len_files in lines_list:
                    if len_files == len_1:
                        f.write("1.txt\n")
                        f.write(str(len_1))
                        f.write('\n')
                        for l in lines_1:
                            f.write(l)
                        f.write('\n\n')
                    else:
                        if len_files == len_2:
                            f.write("2.txt\n")
                            f.write(str(len_2))
                            f.write('\n')
                            for l in lines_2:
                                f.write(l)
                            f.write('\n')
                        else:
                            if len_files == len_3:
                                f.write("3.txt\n")
                                f.write(str(len_3))
                                f.write('\n')
                                for l in lines_3:
                                    f.write(l)
                                f.write('\n')

