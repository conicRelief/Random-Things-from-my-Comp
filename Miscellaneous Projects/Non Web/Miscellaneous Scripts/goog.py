import re

import timeit


# input = ["hello", "groovy", "world"]
# text = "groovy well hello world well hello there groovy hello hello a groovy fancy fancy world to"
input = ['a','b','c']
text = 'a b a b a b b b c c c b a b b c a b a b c b a c b a c b a c'
#
# text = "a b c d a"
# input = ["a","c","d"]


start_time = timeit.default_timer()


rebuild ,prev = "" ,""
for x in text.split(" "):
    if x != prev or x not in input:
        rebuild = " ".join([rebuild,x])
    prev = x
print rebuild
print timeit.default_timer() - start_time

start_time = timeit.default_timer()
print  " ".join([text[x] for x in range(len(text)) if (x == 0) or (x > 0 and text[x-1] != text[x])])
print timeit.default_timer() - start_time











def remove_repetition(text, terms):
    rebuild ,prev = "" ,""
    for x in text.split(" "):
        if x != prev or x not in terms:
            rebuild = " ".join([rebuild,x])
        prev = x
    return rebuild

print [text[x] for x in range(len(text)) if (x == 0) or (x > 0 and text[x-1] != text[x])]

def answer(document, searchTerms):

    doc = remove_repetition(document,searchTerms).split(" ")
    p = popt = 0
    q = qopt = len(doc)-1
    v = 0
    while v < len(doc):
        while all(x in doc[p:q-1] for x in searchTerms):
            q= q-1
        while all(x in doc[p+1:q] for x in searchTerms):
            p= p+1
        if q-p < qopt - popt and all(x in doc[p:q] for x in searchTerms) and p < len(doc)+1 and q < len(doc):
            popt = p
            qopt = q
            vopt = v
        if len(doc) > p:
            p = p+1
        if len(doc) > q:
            q = q+1
        v = v+ 1
    return " ".join(doc[popt:qopt])



def remove_repetition(text, terms):
    rebuild ,prev = "" ,""
    for x in text.split(" "):
        if x != prev or x not in terms:
            rebuild = " ".join([rebuild,x])
        prev = x
    return rebuild

def find_all_valid_substrings2(text, terms):
    p,q = 0,len(text.split(" ")) - 1
    doc = text.split(" ")

    for x in terms:
        if not x in text:
            return None
    if len(text.split(" ")) < len(terms):
        return None
    left = " ".join(text.split(" ")[:-1])
    right =" ".join(text.split(" ")[1:])
    processed_left = find_all_valid_substrings2(left, terms)
    processed_right = find_all_valid_substrings2(right, terms)
    if processed_left is None and processed_right is None:
        return text
    else:
        return processed_left if processed_left is not None else "" + processed_right if processed_right is not None else ""





def goog(document, terms):
    doc = document.split(" ")
    lendoc = len(doc)
    p,q,v  = 0,lendoc-1,0
    popt,qopt,vopt = p,q,v
    while v + p - len(terms) < lendoc:
        while all(x in doc[p:q] for x in terms):
            q= q-1
        q = q+1
        while all(x in doc[p:q] for x in terms):
            p= p+1
        p = p-1
        if q-p < qopt - popt and all(x in doc[p:q] for x in terms) and q-1<lendoc and p-1<lendoc:
            print q, lendoc
            popt = p
            qopt = q
            vopt = v
        if lendoc > p + v:
            p = p+1
        if lendoc > q+ v:
            q = q+1
        v = v+ 1

    # print doc[popt:qopt]
    return " ".join(doc[popt:qopt])

    # popt,qopt,vopt = q+1,p-1,0
    # print p,q
    # print doc[p:q]
    # print
    # # # while(v+p< len(doc)):
    #     while all(x in doc[v+p:v+q] for x in terms):
    #         q= q-1
    #     while all(x in doc[v+p:v+q] for x in terms):
    #         p= p+1
    #     v = v+1
    #     print "DOC::", doc
    #     print "RDOC",doc[p+1:q+1]
    #     print p,q


print "a" in ["happen"]

print ord("a".upper())-64


def find_all_valid_substrings(text, terms):
    relevant_regex = [x for x in re.findall(".*".join(terms), text) if x is not None]
    if len(relevant_regex) == 0:
        return None
    contender = min(relevant_regex)
    left = " ".join(contender.split(" ")[:-1])
    right =" ".join(contender.split(" ")[1:])
    processed_left = find_all_valid_substrings(left, terms)
    processed_right = find_all_valid_substrings(right, terms)
    if processed_left is None and processed_right is None:
        return contender
    else:
        return processed_left if processed_left is not None else "" + processed_right if processed_right is not None else ""

def earliest_substring(substrings):
    pass

answer(text,input)
text = remove_repetition(text, input)
# print goog(text,input), "<<<<"
# a = find_all_valid_substrings2(text,input)
# valid_substrings_via_histogram_sweep(text,input)
# sorted_substrings = sorted([find_all_valid_substrings(text,x) for x in iter.permutations(input,len(input))], key=len)
# smallest = filter(lambda s :len(s)==len(sorted_substrings[0]), sorted_substrings )



# @return a string
# # def minWindow(S, T):
# #     minWindow = [-1,-1]
# #     # The begin and end position (both inclusive) of current window
# #     begin, end = -1, 0
# #
# #     totalCount = dict((i,0) for i in T)
# #
# #     # Compute the char distribution in T
# #     need = {}
# #     for item in T:  need[item] = need.get(item, 0) + 1
# #
# #     # Find the first window, containing all the characters in T
# #     needCount = len(T)
# #     while end < len(S):
# #         if S[end] in need:
# #             if begin == -1:         begin = end
# #             totalCount[S[end]] += 1
# #
# #             if totalCount[S[end]] <= need[S[end]]:
# #                 # Find one more char for a qualified window
# #                 needCount -= 1
# #
# #                 # Enough chars to form a window
# #                 if needCount == 0:  break
# #         end += 1
# #     else:
# #         # Did not find a window
# #         return ""
# #
# #     # Try to minimize the window length by removing the leftmost items
# #     while True:
# #         if S[begin] in need:
# #             if totalCount[S[begin]] > need[S[begin]]:
# #                 totalCount[S[begin]] -= 1
# #                 begin += 1
# #             else:
# #                 # Already be minimum
# #                 break
# #         else:
# #             begin += 1
# #
# #     minWindow = [begin, end]
# #
# #     # Try next window, ending with S[begin]
# #     while True:
# #         # Find the next window, ending with current S[begin]
# #         end += 1
# #         while end < len(S):
# #             if S[end] == S[begin]:      break
# #             if S[end] in totalCount:    totalCount[S[end]] += 1
# #             end += 1
# #         else:
# #             # No windows left.
# #             break
# #
# #         # Minimize current window, by removing the leftmost items
# #         begin += 1
# #         while begin <= end:
# #             if S[begin] in need:
# #                 if totalCount[S[begin]] > need[S[begin]]:
# #                     totalCount[S[begin]] -= 1
# #                     begin += 1
# #                 else:
# #                     # Minimized
# #                     break
# #             else:
# #                 begin += 1
# #
# #         if end - begin < minWindow[1] - minWindow[0]:
# #             # Find a shorter window
# #             minWindow[0], minWindow[1] = begin, end
# #     print S
# #     return S[minWindow[0]: minWindow[1]+1]
#
# print minWindow(text.split(" "), input)
test_cases =[
"-683 -501 -214 -182 542 900 1000 291 -451 -82 849 444 887 | -638 -954 823 607 653 -444 543 217 -36 -795 -896 -307 345",
"-596 675 -854 -704 11 721 914 650 -764 -67 | 776 230 -93 -512 -122 39 412 -31 -289 -10 | -785 -772 -386 41 -776 242 663 241 72 -831 | 911 935 363 454 -32 -267 611 -203 495 -948 | -807 137 804 7 874 106 373 -165 -156 159 | -766 -291 276 840 -153 612 -452 -999 -736 -892 | -487 -868 -569 -816 560 812 -620 -827 -887 741 | 533 963 127 -579 -392 459 -781 -443 -236 230 | -841 -201 793 391 -154 950 -515 369 -938 -835"
]

for test in test_cases:
    list_of_scores =  [ [y for y in x.split(" ") if len(y) > 0] for x in test.split("|")]
    print " ".join([max(x) for x in list_of_scores])


test_cases = ["13,8","17,6"]
for test in test_cases:
    term_a , term_b = test.split(",")[0],test.split(",")[1]
