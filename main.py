
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中的函数体内编写代码，每个题目的函数后有调用语句用于检验，
# 上交作业时提交本文件，命名为h8_学号_姓名.py，如h8_1700000012_张三.py
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业在4月27日23：59之前提交到作业提交网站



# ========= 2 单词最小编辑距离问题 =========
# 实现一个函数，给定两个单词，得出从源单词变到目标单词所需要的最小编辑距离，返回总得分与编辑操作过程
# # 可以进行的操作有：
# 从源单词复制一个字母到目标单词
# 从源单词删除一个字母
# 在目标单词插入一个字母
# 参数：两个字符串，即源单词original与目标单词target，以及不同操作对应的分值，即一个字典
# 返回值：一个整数与一个列表，最低的分数与操作过程，示例见检验
## 编辑操作过程不一定唯一，给出一种满足条件的操作过程即可
def dpWordEdit(original, target, oplist):
    operations = []
    original = ' ' + original
    target = ' ' + target
    original_len = len(original)
    target_len = len(target)
    dp = [[0 for i in range(target_len)] for i in range(original_len)]
    op = [['' for i in range(target_len)] for i in range(original_len)]
    for i in range(1, target_len):
        dp[0][i] = i * oplist['insert']
        op[0][i] = 'insert ' + target[i]
    for i in range(1, original_len):
        dp[i][0] = i * oplist['delete']
        op[i][0] = 'delete ' + original[i]
    for i in range(1, original_len):
        for j in range(1, target_len):
            copy = 0x3f3f3f3f
            if original[i] is target[j]:
                copy = dp[i-1][j-1] + oplist['copy']
            delete = dp[i-1][j] + oplist['delete']
            insert = dp[i][j-1] + oplist['insert']
            dp[i][j] = min(copy, delete, insert)
            if dp[i][j] is copy:
                op[i][j] = 'copy ' + original[i]
            elif dp[i][j] is delete:
                op[i][j] = 'delete ' + original[i]
            elif dp[i][j] is insert:
                op[i][j] = 'insert ' + target[j]
    i = original_len - 1
    j = target_len - 1
    while True:
        if i is 0 and j is 0:
            break
        operations.append(op[i][j])
        if i is 0:
            j -= 1
        elif j is 0:
            i -= 1
        elif op[i][j].startswith('copy'):
            i -= 1
            j -= 1
        elif op[i][j].startswith('delete'):
            i -= 1
        elif op[i][j].startswith('insert'):
            j -= 1
    score = dp[-1][-1]
    operations.reverse()
    return score, operations

# 检验
print("========= 2 单词最小编辑距离问题 =========")
oplist = {'copy':10, 'delete':25, 'insert':20}
originalWords = ["cane", "sheep", "algorithm", "debug", "difficult", "directory", "wonderful"]
targetWords = ["new", "sleep", "alligator", "release", "sniffing", "framework", "terrific"]
for i in range(len(originalWords)):
    score, operations = dpWordEdit(originalWords[i], targetWords[i], oplist)
    print(score)
    print(operations)
    # exit()

# 操作所对应的分数可调整
# oplist = {'copy':5, 'delete':20, 'insert':20}
# 70
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 60
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 185
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 205
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 200
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 220
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 235
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#
# oplist = {'copy':5, 'delete':10, 'insert':15}
# 45
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 45
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 125
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 135
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 130
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 145
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 150
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
#
# oplist = {'copy':10, 'delete':25, 'insert':20}
# 90
# ['delete c', 'delete a', 'copy n', 'copy e', 'insert w']
# 85
# ['copy s', 'insert l', 'delete h', 'copy e', 'copy e', 'copy p']
# 230
# ['copy a', 'copy l', 'insert l', 'insert i', 'copy g', 'insert a', 'insert t', 'copy o', 'copy r', 'delete i', 'delete t', 'delete h', 'delete m']
# 230
# ['insert r', 'delete d', 'copy e', 'insert l', 'insert e', 'insert a', 'insert s', 'insert e', 'delete b', 'delete u', 'delete g']
# 245
# ['insert s', 'insert n', 'delete d', 'copy i', 'copy f', 'copy f', 'copy i', 'insert n', 'insert g', 'delete c', 'delete u', 'delete l', 'delete t']
# 265
# ['insert f', 'delete d', 'delete i', 'copy r', 'insert a', 'insert m', 'copy e', 'insert w', 'delete c', 'delete t', 'copy o', 'copy r', 'insert k', 'delete y']
# 280
# ['insert t', 'delete w', 'delete o', 'delete n', 'delete d', 'copy e', 'copy r', 'insert r', 'insert i', 'copy f', 'insert i', 'insert c', 'delete u', 'delete l']
