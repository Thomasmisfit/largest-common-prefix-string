#!/usr/bin/python
#-*-coding:utf-8 -*-

# author: 736626977@qq.com
# updated at: 2017-03-09

"""
How to find the longest common prefix string amongst an array of strings?

"""
import time
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# ---------------Method 1-----------------------------


def longestCommonPrefix_scanning(strs_list):
    """ Method 1:
                (1). 使用第一个列表中的字符串作为初始的最长公共前缀子串prefix;
                (2). prefix来与剩下的字符串strs_list[i](0<i<length-1)依次进行比较，每次和strs_list[i]比较的时候，选择prefix和strs_list[i]两个的最长公共前缀子串最为新的prefix;
                (3). 直到和列表中所有的字符串比较完毕之后，返回prefix作为最终的最长公共前缀子串

    Args:
                                                                    strs_list: a list of strings

    Returns:
                                                                    longest_common_prefix
    """
    if not isinstance(strs_list, list):
        return "Please make sure strs_list is a list"
    if len(strs_list) == 0:
        return ""
    prefix = strs_list[0]
    for str_item in strs_list:
        while str_item.find(prefix) != 0:
            prefix = prefix[0:len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix

# ---------------Method 2-----------------------------


def longestCommonPrefix_divide(strs_list):
    """ Method 2:
                (1). 将整个列表二分成left和rigth两个子列表；
                (2). 分别计算两个子列表的最长公共前缀子串（递归方式，再分别把每个子列表再分解问两个更小的子列表，最终到不能再分为止）
                (3). 比较两个子列表的最长公共前缀子串，选取两者的最长公共前缀子串一个作为最终的结果

    Args:
                                                                    strs_list: a list of strings

    Returns:
                                                                    longest_common_prefix
    """
    if not isinstance(strs_list, list):
        return "Please make sure strs_list is a list"
    if len(strs_list) == 0:
        return ""
    return longestCommonPrefix(strs_list, 0, len(strs_list) - 1)


def longestCommonPrefix(strs_list, l, r):
    if l == r:
        return strs_list[l]
    else:
        mid = (l + r) / 2
        lcpLeft = longestCommonPrefix(strs_list, l, mid)
        lcpRight = longestCommonPrefix(strs_list, mid + 1, r)
        return commonPrefix(lcpLeft, lcpRight)


def commonPrefix(left, right):
    min_len = min(len(left), len(right))
    for i in xrange(0, min_len):
        if left[i] != right[i]:
            return left[0:i]
    return left[0:min_len]

# ---------------Method 3-----------------------------


def longestCommonPrefix_binary_search(strs_list):
    """ Method 3: binary search
                (1). 确定整个列表中最短的字符串的长度，作为初始的最长公共前缀子串长度min_str_Len;
                (2). 选取第一个字符串的min_str_Len长度作为初始二叉搜索的初始字符串sub_first_string;
                (3). 将初始字符串sub_first_string二分为两部分，分裂的位置标记为middle, 如果列表中的所有字符串都是以sub_first_string[0:middle] 开头的，则向右移动middle的位置，否则向左移动middle的位置。
                (4). 直到不能再移动位置。则此时的sub_first_string[0:middle]作为最长公共前缀子串长度

    Args:
                                                                    strs_list: a list of strings

    Returns:
                                                                    longest_common_prefix
    """
    if not isinstance(strs_list, list):
        return "Please make sure strs_list is a list"
    if len(strs_list) == 0:
        return ""
    # min_str_Len is used to stored the min string length in the list of strings
    min_str_Len = min([len(strs) for strs in strs_list])
    low = 1
    high = min_str_Len
    while low <= high:
        middle = (low + high) / 2
        if isCommonPrefix(strs_list, middle):
            low = middle + 1
        else:
            high = middle - 1
    return strs_list[0][0:(low + high) / 2]


def isCommonPrefix(strs_list, length):
    sub_first_string = strs_list[0][0:length]
    for i in xrange(1, len(sub_first_string)):
        if not strs_list[i].startswith(sub_first_string):
            return False
    return True


# ----------------main-----------------------

def main():
    strs_list = ["aa", "aaabbbbbbb", "aaa", "a"]
    print "字符串列表为：", strs_list
    print "这里有三种方法来计算最长公共前缀子串，请输入（1，2，3）进行选择："
    while True:
        choose = int(raw_input("请输入（1，2，3）进行选择："))
        if choose == 1:
            start_ = datetime.utcnow()
            prefix_string = longestCommonPrefix_scanning(strs_list)
            end_ = datetime.utcnow()
            time_spent = (end_ - start_)
            print "最长公共前缀子串为：", prefix_string
            time_spent_sec = time_spent.microseconds / 1000.0 + time_spent.seconds
            print "总共耗时(seconds)：" + str(time_spent_sec)
        elif choose == 2:
            start_ = datetime.utcnow()
            prefix_string = longestCommonPrefix_divide(strs_list)
            end_ = datetime.utcnow()
            time_spent = (end_ - start_)
            print "最长公共前缀子串为：", prefix_string
            time_spent_sec = time_spent.microseconds / 1000.0 + time_spent.seconds
            print "总共耗时(seconds)：" + str(time_spent_sec)
        elif choose == 3:
            start_ = datetime.utcnow()
            prefix_string = longestCommonPrefix_binary_search(strs_list)
            end_ = datetime.utcnow()
            time_spent = (end_ - start_)
            print "最长公共前缀子串为：", prefix_string
            time_spent_sec = time_spent.microseconds / 1000.0 + time_spent.seconds
            print "总共耗时(seconds)：" + str(time_spent_sec)

        else:
            print "输入错误"


if __name__ == '__main__':
    main()
