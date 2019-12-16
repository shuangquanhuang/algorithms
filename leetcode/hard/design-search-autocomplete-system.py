# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/13 20:55

"""


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        trie = {}
        for s, c in zip(sentences, times):
            t = trie
            for w in s:
                if w not in t:
                    t[w] = {}
                t = t[w]
            t['#'] = c
        self.trie = trie

        self.last = trie
        self.prefix = ''

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.last = self.trie
            self.insert(self.prefix)
            self.prefix = ''
            return []

        self.prefix += c
        if not self.last:
            return []

        t = self.last
        if c not in t:
            self.last = None
            return []

        t = t[c]
        self.last = t
        res = self.count(t, self.prefix)
        res.sort()
        res = res[:3]

        return [w for c, w in res]

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        if '#' in t:
            t['#'] += 1
        else:
            t['#'] = 1

    def count(self, t, w):
        if not t:
            return []

        ans = [(-t['#'], w)] if '#' in t else []
        for ch in t:
            if ch != '#':
                ans.extend(self.count(t[ch], w + ch))
        return ans


# s = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
# print(s.input('i'))
# print(s.input(' '))
# print(s.input('a'))
# print(s.input('#'))

# print('#' * 30)
#
# s = AutocompleteSystem(["i love you","island","iroman","i love leetcode"], [5,3,2,2])
# for i in [["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"],["i"],[" "],["a"],["#"]]:
#     print(s.input(i[0]))

s = AutocompleteSystem([
    "uqpewwnxyqxxlhiptuzevjxbwedbaozz","ewftoujyxdgjtazppyztom",
    "pvyqceqrdrxottnukgbdfcr",
    "qtdkgdbcyozhllfycfjhdsdnuhycqcofaojknuqqnozltrjcabyxrdqwrxvqrztkcxpenbbtnnnkfhmebj",
    "jwfbusbwahyugiaiazysqbxkwgcawpniptbtmhqyrlxdwxxwhtumglihrgizrczv",
    "cfptjitfzdcrhw",
    "aitqgitjgrcbacgnaasvbouqsqcwbyskkpsnigtfeecmlkcjbgduban",
    "utsqkmiqqgglufourfdpgdmrkbippffacwvtkpflzrvdlkdxykfpkoqcb",
    "ethtbdopotpamvrwuomlpahtveyw",
    "jiaqkaxovsqtkpdjfbkajpvpyetuoqwnrnpjdhoojbsdvneecsdvgqpyurmsvcy",
    "j",
    "btbnuplyeuccjbernsfbnveillrwdbqledwvpmvdbcugkurrkabtpykhlcogeszclyfuquafouv",
    "hndjzblegevtfkgbjttektox",
    "gtvnlninpvenapyfgmsjdisfnmiktitrutctawosjflvzfkbegnprixzqwzcyhoovsivuwmofsveqkyosowuyamuvy",
    "sawrirvrfrbfagreahrioaombukmdwztbpggnxd",
    "mgdcwptvbvhzyvvumvbjjn",
    "otjvvkegwleyyxtghwgfmlsqlhrlibdvqfinyyebotjpwoaejhtornfgikmifdmwswbqgwhcbzuhrpajxuqicegcptszct",
    "zlondsttyvnnnnxjtoqnlktitwzurissczzbyfsbgpoawodwjpsmavaugnhqtsbeixwl",
    "yehvdehbtmwqkmcjmvpivfzqvevkotwzvjoyfvp",
    "bjximtpayjdcxbrnksbtfnpynzaygygdflowewprqngdadzdhxcpgapjejojrkzrutgcsfpfvpluagniqimfqddldxqiw",
    "bysyrxfykivyauysytgxfhqcrxliulahuizjvozpywrokxujhzpauxwufcxiitukljiiclatfrspqcljjoxpxziumstnhqr",
    "uxtvutlgqapyfltiulwrplesmtowzoyhhjhzihatpuvmutxqgxfawpwypedbz",
    "jzgsdjdawrqfladolduldhpdpagmvllvzamypuqlrpbmhxxadqaqrqavtxeghcyysjynovkiyjtvdluttodtmtocajgttmv",
    "mbijfkmepalhdiubposdksdmmttxblkodcdrxbnxaqebnwliatnxpwaohbwkidia",
    "ljggggbyxwrwanhjonoramexdmgjigrtpz",
    "cqfvkutpipxjepfgsufonvjtotwfxyn",
    "kvseesjazssavispavchdpzvdhibptowhyrrshyntpwkez",
    "nveuzbaosuayteiozmnelxlwkrrrjlwvhejxhupvchfwmvnqukphgoacnazuoimcliubvhv",
    "uwrpwhfdrxfnarxqpkhrylkwiuhzubjfk",
    "bniyggdcloefwy",
    "ihranmhbsahqjxesbtmdkjfsupzdzjvdfovgbtwhqfjdddwhdvrnlyscvqlnqpzegnvvzyymrajvso",
    "lscreasfuxpdxsiinymuzybjexkpfjiplevqcjxlm",
    "uwgnfozopsygnmptdtmmuumahoungpkodwxrcvfymqpeymaqruayvqqgoddgbnhemtsjifhxwiehncswxzrghf",
    "nyfbxgcpfrzyqwfjzgmhuohjhrjizsyjqgmertmooeiaadcmiuyyylpcosnweoyydeauazhzbeaqn",
    "tpylrxbwnkrfxckfdlvrbytaezuzmyscpvruthuvbxjenkeolvqsrjqzizyclzmqtjvnamdansmzyspcfghfprorqprua",
    "nhldlmxpuckxeekipkrzugatjiivtazjbjyxokksyueyjbgmrovbckbxqcqefaiavzsarbbypgmpxe",
    "sylraqsd",
    "xr",
    "xkzpxkhrucyatpatkigvntohihibyisyqtkjdhatdvyvxbjttz",
    "nvnz",
    "blzddwxphkgqfsfzfclwytstpvpzgcdeggdwzukzirscfzcteeuqbmmrfxcnokbbyxkqrxtjfarcefiynwfmy",
    "inuxmuhtdwpuvyludwtokhtalxbuccepsayrjycbcwbtnfholjvkmypodv",
    "awwillrm",
    "xznodxngrstjrwqzmlmigpw",
    "khlxjdtictufdfbkgfusdtaaeuspbbfmtjodflgqofzlqnulkdztflm",
    "nlngmckslyqzjiyiexbropbxnynjcstziluewypboqhqndqsxhtnosrgrameajovsclrgwqjgnztvxrkhwnxkfrf",
    "yroadxhxyacaexrwju",
    "ujxlbpcbxdqrvubifnpzjmmkolyljzjhdegaiowaal",
    "tnfnjgtxbckbpyplucprxcqzhrfjimylmlhdglntfydepltjvklyxesndzuubienhvuaqc",
    "ouedhtkpkg",
    "ygchsrrubucqffewifsxaefwocfaiiupqbomktvrcddggqfgnaycstpccwtbheyaqwhosxajqeqqxzyjsfng",
    "jqqgpjvfkgjh",
    "csowoazaiyejgyixszqmtctpzlkccccqregyhtvxccvrpkupwcyhqatxscevzdfbdqnuyadiyfnhysddfyxpgqtjiogmxsmzbbkr",
    "dlzxdpchkdaztkqtrjmuujgoiae",
    "plcjkwukkyqluxjbhxsyeaqvviinfuujsafwsquidvmutsrukxwrv",
    "yopqbtpoqhpcktjangauzcvvpephhprpaaclbbkgchlqkrwdsaupeizlwxzcpkchoagmrrkwdkthosmrjefgbumnrjsb"],
[12,9,4,4,1,5,3,4,7,9,2,4,2,3,11,13,1,3,4,10,7,1,9,5,10,14,5,3,2,11,5,14,4,13,11,5,15,8,1,12,2,11,4,2,11,14,9,12,1,7,13,11,7,2,6,10])
for w in [["w"],["o"],["f"],["q"],["m"],["p"],["k"],["q"],["g"],["i"],["s"],["a"],["v"],["#"],["b"],["k"],["j"],["o"],["r"],["d"],["w"],["h"],["i"],["a"],["g"],["p"],["x"],["m"],["k"],["r"],["q"],["l"],["v"],["l"],["c"],["v"],["w"],["e"],["p"],["d"],["i"],["x"],["j"],["h"],["k"],["v"],["a"],["y"],["m"],["j"],["j"],["r"],["n"],["f"],["h"],["r"],["g"],["o"],["m"],["s"],["d"],["d"],["h"],["x"],["g"],["s"],["k"],["l"],["f"],["m"],["s"],["x"],["t"],["i"],["n"],["s"],["i"],["m"],["w"],["c"],["f"],["f"],["f"],["c"],["f"],["h"],["j"],["m"],["r"],["#"],["h"],["e"],["f"],["y"],["w"],["c"],["t"],["p"],["f"],["j"],["w"],["q"],["t"],["k"],["b"],["l"],["w"],["#"],["k"],["n"],["u"],["f"],["g"],["u"],["j"],["t"],["i"],["n"],["k"],["o"],["r"],["c"],["v"],["o"],["u"],["w"],["f"],["y"],["n"],["b"],["x"],["a"],["o"],["m"],["n"],["e"],["j"],["a"],["u"],["l"],["n"],["l"],["m"],["e"],["f"],["w"],["n"],["g"],["k"],["h"],["z"],["i"],["q"],["n"],["f"],["m"],["x"],["d"],["v"],["j"],["w"],["o"],["w"],["b"],["v"],["p"],["r"],["b"],["k"],["f"],["l"],["y"],["o"],["p"],["y"],["u"],["g"],["b"],["o"],["l"],["v"],["g"],["n"],["g"],["w"],["i"],["x"],["f"],["j"],["e"],["r"],["m"],["h"],["y"],["#"],["y"],["v"],["k"],["a"],["j"],["x"],["b"],["c"],["i"],["v"],["k"],["y"],["a"],["u"],["e"],["b"],["a"],["q"],["k"],["#"],["x"],["x"],["l"],["c"],["y"],["m"],["z"],["e"],["v"],["o"],["c"],["k"],["z"],["o"],["y"],["d"],["g"],["b"],["e"],["f"],["k"],["v"],["z"],["h"],["e"],["h"],["w"],["i"],["o"],["k"],["b"],["s"],["q"],["t"],["a"],["k"],["i"],["a"],["b"],["#"],["h"],["m"],["r"],["t"],["w"],["p"],["k"],["w"],["h"],["r"],["j"],["p"],["w"],["y"],["h"],["f"],["o"],["q"],["t"],["w"],["p"],["w"],["m"],["k"],["h"],["q"],["f"],["b"],["t"],["y"],["j"],["z"],["c"],["w"],["c"],["s"],["t"],["j"],["z"],["m"],["k"],["j"],["u"],["u"],["t"],["o"],["j"],["z"],["e"],["m"],["k"],["h"],["z"],["u"],["z"],["y"],["d"],["i"],["c"],["y"],["q"],["d"],["x"],["r"],["k"],["d"],["i"],["j"],["y"],["u"],["i"],["d"],["o"],["v"],["s"],["r"],["n"],["g"],["e"],["z"],["g"],["n"],["g"],["r"],["y"],["x"],["n"],["e"],["x"],["r"],["m"],["l"],["g"],["n"],["m"],["m"],["x"],["#"],["z"],["p"],["j"],["l"],["g"],["g"],["q"],["v"],["m"],["a"],["a"],["u"],["w"],["l"],["r"],["f"],["b"],["q"],["e"],["q"],["p"],["b"],["b"],["z"],["p"],["d"],["u"],["w"],["h"],["v"],["t"],["w"],["q"],["v"],["j"],["d"],["z"],["v"],["h"],["q"],["m"],["d"],["w"],["z"],["q"],["m"],["f"],["m"],["n"],["s"],["g"],["f"],["d"],["b"],["x"],["y"],["f"],["s"],["z"],["m"],["o"],["k"],["i"],["i"],["n"],["l"],["e"],["s"],["v"],["h"],["m"],["g"],["f"],["q"],["r"],["m"],["e"],["w"],["a"],["x"],["f"],["h"],["c"],["a"],["u"],["n"],["w"],["#"],["k"],["h"],["i"],["k"],["p"],["v"],["u"],["y"],["q"],["z"],["t"],["m"],["b"],["l"],["j"],["u"],["p"],["r"],["t"],["c"],["v"],["w"],["i"],["v"],["y"],["z"],["l"],["x"],["p"],["v"],["p"],["j"],["g"],["a"],["s"],["g"],["u"],["x"],["n"],["j"],["q"],["u"],["m"],["u"],["f"],["e"],["l"],["o"],["#"],["j"],["r"],["g"],["n"],["r"],["a"],["n"],["y"],["c"],["w"],["n"],["r"],["q"],["u"],["t"],["d"],["a"],["k"],["m"],["e"],["d"],["n"],["w"],["r"],["y"],["i"],["j"],["k"],["r"],["d"],["q"],["v"],["u"],["t"],["u"],["t"],["q"],["p"],["u"],["f"],["j"],["j"],["e"],["p"],["s"],["x"],["d"],["f"],["m"],["a"],["s"],["s"],["b"],["w"],["u"],["t"],["d"],["d"],["f"],["o"],["k"],["h"],["a"],["o"],["c"],["b"],["f"],["i"],["m"],["v"],["u"],["e"],["v"],["o"],["l"],["v"],["b"],["k"],["n"],["r"],["d"],["g"],["c"],["v"],["s"],["o"],["x"],["t"],["p"],["w"],["n"],["g"],["b"],["v"],["r"],["#"],["b"],["c"],["p"],["f"],["y"],["s"],["x"],["a"],["e"],["c"],["m"],["a"],["b"],["f"],["e"],["i"],["s"],["q"],["r"],["y"],["y"],["v"],["d"],["t"],["k"],["b"],["m"],["z"],["u"],["f"],["l"],["u"],["j"],["g"],["f"],["q"],["i"],["o"],["j"],["#"],["h"],["s"],["u"],["t"],["r"],["k"],["o"],["e"],["b"],["p"],["k"],["e"],["d"],["s"],["h"],["l"],["k"],["l"],["a"],["b"],["b"],["m"],["n"],["s"],["#"],["y"],["v"],["a"],["z"],["p"],["m"],["v"],["a"],["a"],["x"],["p"],["x"],["b"],["e"],["t"],["v"],["u"],["c"],["i"],["b"],["f"],["z"],["h"],["e"],["m"],["c"],["i"],["c"],["f"],["r"],["k"],["l"],["d"],["r"],["d"],["a"],["l"],["z"],["h"],["e"],["a"],["c"],["u"],["u"],["h"],["z"],["c"],["h"],["w"],["z"],["s"],["m"],["t"],["o"],["g"],["t"],["b"],["i"],["z"],["d"],["g"],["y"],["h"],["x"],["c"],["c"],["m"],["e"],["v"],["g"],["o"],["w"],["q"],["w"],["#"],["x"],["x"],["z"],["q"],["j"],["q"],["a"],["t"],["e"],["h"],["y"],["b"],["z"],["h"],["i"],["y"],["a"],["j"],["g"],["w"],["n"],["q"],["x"],["s"],["n"],["b"],["d"],["w"],["j"],["d"],["b"],["y"],["x"],["n"],["c"],["t"],["o"],["#"],["y"],["q"],["x"],["r"],["j"],["v"],["e"],["h"],["u"],["b"],["k"],["d"],["a"],["h"],["s"],["x"],["z"],["i"],["q"],["b"],["p"],["j"],["v"],["x"],["a"],["f"],["t"],["o"],["w"],["r"],["p"],["c"],["u"],["e"],["j"],["h"],["n"],["w"],["p"],["w"],["c"],["l"],["f"],["q"],["u"],["o"],["p"],["i"],["#"],["k"],["o"],["b"],["x"],["p"],["x"],["x"],["f"],["x"],["r"],["s"],["d"],["s"],["v"],["q"],["k"],["h"],["q"],["w"],["x"],["u"],["k"],["p"],["r"],["f"],["x"],["n"],["q"],["j"],["c"],["n"],["c"],["g"],["z"],["q"],["x"],["o"],["d"],["a"],["p"],["f"],["s"],["i"],["m"],["h"],["p"],["l"],["c"],["d"],["h"],["q"],["v"],["s"],["t"],["#"],["s"],["f"],["w"],["q"],["x"],["a"],["e"],["v"],["c"],["f"],["e"],["u"],["e"],["y"],["q"],["k"],["y"],["j"],["k"],["p"],["i"],["i"],["z"],["u"],["o"],["b"],["r"],["f"],["d"],["v"],["m"],["b"],["u"],["k"],["k"],["y"],["n"],["i"],["t"],["c"],["g"],["b"],["s"],["u"],["n"],["x"],["z"],["f"],["n"],["h"],["l"],["m"],["s"],["m"],["f"],["i"],["d"],["p"],["z"],["e"],["w"],["e"],["z"],["k"],["r"],["z"],["s"],["s"],["w"],["k"],["i"],["v"],["w"],["p"],["m"],["f"],["#"],["u"],["l"],["z"],["f"],["g"],["o"],["m"],["p"],["n"],["w"],["v"],["s"],["h"],["k"],["u"],["q"],["p"],["p"],["z"],["u"],["s"],["r"],["p"],["d"],["i"],["o"],["w"],["b"],["n"],["a"],["h"],["e"],["z"],["g"],["w"],["h"],["g"],["z"],["b"],["i"],["j"],["k"],["y"],["n"],["d"],["w"],["w"],["j"],["s"],["o"],["k"],["z"],["p"],["o"],["k"],["n"],["i"],["j"],["r"],["p"],["q"],["e"],["d"],["e"],["l"],["d"],["g"],["y"],["v"],["l"],["x"],["o"],["o"],["n"],["f"],["v"],["v"],["y"],["x"],["p"],["m"],["s"],["w"],["j"],["x"],["o"],["h"],["r"],["p"],["s"],["k"],["e"],["w"],["#"],["p"],["e"],["t"],["f"],["m"],["g"],["s"],["k"],["e"],["v"],["k"],["t"],["f"],["w"],["w"],["a"],["u"],["z"],["s"],["n"],["h"],["a"],["m"],["y"],["u"],["#"],["i"],["p"],["j"],["q"],["p"],["c"],["s"],["v"],["l"],["f"],["j"],["a"],["o"],["m"],["r"],["c"],["i"],["w"],["k"],["g"],["v"],["z"],["h"],["t"],["w"],["t"],["w"],["a"],["o"],["h"],["c"],["m"],["k"],["w"],["i"],["v"],["t"],["w"],["x"],["h"],["#"],["l"],["u"],["j"],["#"],["o"],["t"],["t"],["s"],["b"],["w"],["i"],["m"],["b"],["r"],["l"],["u"],["x"],["z"],["c"],["d"],["f"],["d"],["d"],["x"],["e"],["a"],["b"],["p"],["z"],["v"],["c"],["y"],["e"],["k"],["x"],["b"],["t"],["c"],["z"],["j"],["x"],["o"],["s"],["c"],["x"],["g"],["d"],["e"],["y"],["i"],["w"],["n"],["y"],["c"],["y"],["e"],["y"],["w"],["v"],["f"],["u"],["b"],["g"],["n"],["x"],["y"],["d"],["a"],["t"],["p"],["z"],["o"],["n"],["o"],["b"],["n"],["s"],["x"],["e"],["m"],["b"],["e"],["n"],["w"],["u"],["w"],["s"],["o"],["g"],["v"],["#"],["e"],["m"],["k"],["g"],["g"],["#"],["v"],["z"],["v"],["w"],["l"],["z"],["f"],["v"],["k"],["q"],["h"],["c"],["d"],["v"],["i"],["l"],["b"],["s"],["r"],["n"],["r"],["c"],["v"],["b"],["f"],["j"],["o"],["l"],["c"],["z"],["f"],["v"],["s"],["g"],["y"],["w"],["g"],["e"],["q"],["v"],["j"],["p"],["s"],["f"],["c"],["w"],["s"],["h"],["d"],["l"],["z"],["f"],["g"],["w"],["w"],["l"],["v"],["g"],["t"],["y"],["k"],["l"],["z"],["d"],["o"],["x"],["m"],["#"],["z"],["h"],["k"],["j"],["f"],["u"],["i"],["x"],["l"],["n"],["p"],["y"],["j"],["e"],["n"],["m"],["q"],["z"],["n"],["y"],["w"],["f"],["x"],["r"],["i"],["y"],["x"],["t"],["i"],["f"],["f"],["f"],["f"],["v"],["y"],["q"],["k"],["v"],["a"],["k"],["p"],["m"],["w"],["m"],["v"],["k"],["n"],["o"],["c"],["b"],["s"],["e"],["e"],["n"],["a"],["c"],["y"],["l"],["h"],["a"],["m"],["r"],["d"],["g"],["v"],["w"],["i"],["v"],["#"],["d"],["q"],["x"],["l"],["d"],["w"],["p"],["#"],["g"],["r"],["i"],["f"],["x"],["m"],["r"],["p"],["j"],["o"],["g"],["b"],["e"],["e"],["m"],["l"],["w"],["m"],["j"],["x"],["b"],["e"],["a"],["e"],["a"],["y"],["z"],["j"],["v"],["b"],["r"],["z"],["u"],["m"],["l"],["#"],["m"],["p"],["l"],["h"],["a"],["f"],["m"],["t"],["y"],["j"],["g"],["o"],["t"],["n"],["o"],["n"],["e"],["a"],["w"],["c"],["q"],["j"],["z"],["q"],["c"],["p"],["i"],["#"],["x"],["h"],["e"],["f"],["z"],["e"],["x"],["a"],["n"],["g"],["b"],["b"],["z"],["a"],["l"],["c"],["d"],["i"],["a"],["l"],["v"],["y"],["q"],["i"],["r"],["y"],["c"],["n"],["m"],["a"],["i"],["y"],["#"],["o"],["s"],["r"],["n"],["r"],["r"],["c"],["n"],["d"],["s"],["x"],["j"],["r"],["l"],["p"],["d"],["s"],["o"],["i"],["x"],["w"],["b"],["g"],["a"],["p"],["q"],["v"],["c"],["b"],["x"],["n"],["f"],["l"],["c"],["f"],["y"],["d"],["x"],["l"],["g"],["j"],["y"],["b"],["i"],["t"],["z"],["w"],["d"],["x"],["o"],["b"],["q"],["g"],["s"],["h"],["y"],["z"],["h"],["x"],["a"],["r"],["h"],["q"],["m"],["p"],["q"],["p"],["j"],["z"],["b"],["g"],["p"],["q"],["f"],["h"],["x"],["j"],["g"],["c"],["k"],["a"],["c"],["q"],["r"],["d"],["c"],["e"],["p"],["s"],["h"],["t"],["z"],["w"],["v"],["#"],["r"],["p"],["h"],["o"],["f"],["l"],["t"],["p"],["r"],["i"],["c"],["k"],["n"],["i"],["m"],["y"],["y"],["o"],["w"],["p"],["m"],["c"],["a"],["u"],["w"],["z"],["r"],["z"],["t"],["p"],["f"],["a"],["j"],["i"],["o"],["t"],["j"],["f"],["p"],["m"],["r"],["y"],["u"],["e"],["j"],["e"],["e"],["s"],["t"],["w"],["o"],["q"],["s"],["e"],["j"],["f"],["i"],["k"],["l"],["x"],["d"],["d"],["v"],["u"],["f"],["f"],["m"],["e"],["x"],["a"],["h"],["o"],["y"],["c"],["w"],["g"],["f"],["v"],["x"],["i"],["z"],["f"],["g"],["q"],["r"],["t"],["k"],["#"],["a"],["l"],["k"],["l"],["u"],["j"],["c"],["n"],["f"],["d"],["d"],["q"],["w"],["p"],["j"],["p"],["x"],["x"],["y"],["z"],["v"],["k"],["c"],["f"],["b"],["w"],["z"],["e"],["m"],["a"],["o"],["s"],["p"],["n"],["w"],["v"],["s"],["c"],["x"],["l"],["y"],["r"],["c"],["e"],["u"],["z"],["f"],["b"],["q"],["o"],["x"],["g"],["p"],["t"],["#"],["h"],["c"],["b"],["j"],["z"],["r"],["y"],["i"],["s"],["d"],["e"],["h"],["i"],["b"],["u"],["w"],["k"],["o"],["i"],["e"],["y"],["y"],["k"],["b"],["j"],["l"],["g"],["e"],["e"],["a"],["k"],["k"],["m"],["y"],["i"],["f"],["g"],["n"],["t"],["b"],["s"],["z"],["f"],["p"],["t"],["y"],["e"],["u"],["a"],["q"],["o"],["j"],["f"],["u"],["t"],["c"],["p"],["x"],["l"],["z"],["v"],["p"],["g"],["i"],["#"],["b"],["t"],["x"],["e"],["m"],["g"],["b"],["v"],["q"],["i"],["u"],["h"],["l"],["n"],["a"],["q"],["i"],["y"],["h"],["i"],["w"],["d"],["q"],["j"],["o"],["m"],["t"],["c"],["y"],["m"],["j"],["x"],["#"],["n"],["a"],["u"],["a"],["l"],["v"],["d"],["u"],["f"],["v"],["f"],["x"],["f"],["u"],["a"],["s"],["r"],["u"],["u"],["j"],["m"],["k"],["u"],["x"],["h"],["m"],["m"],["i"],["f"],["j"],["a"],["w"],["f"],["p"],["t"],["l"],["e"],["n"],["j"],["y"],["j"],["w"],["j"],["t"],["v"],["o"],["f"],["l"],["z"],["g"],["a"],["u"],["g"],["a"],["y"],["x"],["e"],["r"],["i"],["w"],["n"],["a"],["p"],["o"],["v"],["p"],["o"],["r"],["m"],["v"],["s"],["a"],["c"],["r"],["s"],["o"],["h"],["i"],["f"],["g"],["h"],["b"],["i"],["a"],["q"],["y"],["z"],["q"],["h"],["t"],["u"],["z"],["w"],["r"],["l"],["g"],["n"],["c"],["t"],["x"],["#"],["l"],["i"],["o"],["b"],["x"],["j"],["y"],["v"],["f"],["k"],["f"],["n"],["r"],["j"],["x"],["q"],["o"],["d"],["d"],["u"],["w"],["n"],["p"],["o"],["m"],["c"],["c"],["e"],["m"],["g"],["p"],["e"],["q"],["o"],["u"],["h"],["z"],["m"],["g"],["t"],["k"],["v"],["k"],["b"],["a"],["j"],["o"],["x"],["b"],["i"],["g"],["q"],["x"],["d"],["l"],["s"],["t"],["k"],["j"],["n"],["q"],["n"],["c"],["q"],["d"],["c"],["m"],["b"],["d"],["j"],["y"],["e"],["z"],["i"],["d"],["v"],["o"],["v"],["q"],["j"],["x"],["g"],["w"],["q"],["z"],["n"],["b"],["y"],["w"],["h"],["m"],["#"],["k"],["r"],["m"],["t"],["n"],["e"],["j"],["x"],["d"],["d"],["z"],["g"],["b"],["a"],["f"],["c"],["u"],["b"],["b"],["j"],["f"],["d"],["v"],["k"],["w"],["v"],["o"],["f"],["b"],["e"],["w"],["k"],["t"],["v"],["d"],["v"],["j"],["f"],["p"],["q"],["m"],["i"],["g"],["p"],["o"],["g"],["m"],["i"],["w"],["x"],["t"],["l"],["r"],["l"],["w"],["q"],["f"],["g"],["s"],["a"],["e"],["l"],["v"],["g"],["h"],["l"],["l"],["r"],["c"],["p"],["v"],["p"],["t"],["p"],["m"],["u"],["c"],["k"],["l"],["j"],["v"],["o"],["z"],["z"],["g"],["s"],["z"],["n"],["w"],["i"],["o"],["a"],["z"],["f"],["d"],["y"],["h"],["f"],["#"],["x"],["a"],["m"],["x"],["n"],["s"],["r"],["b"],["h"],["c"],["z"],["o"],["t"],["m"],["u"],["r"],["c"],["c"],["l"],["a"],["t"],["f"],["x"],["b"],["r"],["y"],["i"],["a"],["t"],["p"],["i"],["j"],["c"],["j"],["x"],["h"],["e"],["w"],["w"],["j"],["j"],["o"],["y"],["g"],["c"],["x"],["p"],["m"],["c"],["o"],["l"],["n"],["c"],["t"],["j"],["t"],["s"],["d"],["w"],["s"],["a"],["s"],["d"],["m"],["n"],["c"],["f"],["y"],["p"],["v"],["x"],["j"],["s"],["v"],["x"],["d"],["p"],["f"],["i"],["c"],["j"],["x"],["r"],["v"],["b"],["c"],["r"],["q"],["r"],["n"],["d"],["l"],["f"],["v"],["t"],["#"],["n"],["b"],["x"],["t"],["w"],["x"],["x"],["f"],["p"],["b"],["t"],["e"],["s"],["p"],["k"],["l"],["o"],["m"],["t"],["q"],["i"],["e"],["p"],["l"],["j"],["m"],["w"],["a"],["x"],["h"],["c"],["a"],["p"],["t"],["e"],["y"],["d"],["w"],["s"],["t"],["h"],["l"],["z"],["f"],["o"],["z"],["z"],["a"],["h"],["h"],["j"],["p"],["z"],["#"],["y"],["w"],["f"],["m"],["p"],["#"],["s"],["w"],["r"],["w"],["y"],["b"],["i"],["p"],["e"],["s"],["v"],["h"],["n"],["o"],["p"],["e"],["j"],["x"],["s"],["r"],["h"],["e"],["h"],["t"],["w"],["w"],["w"],["y"],["z"],["f"],["b"],["o"],["n"],["x"],["f"],["h"],["g"],["x"],["d"],["s"],["m"],["b"],["n"],["x"],["j"],["z"],["d"],["g"],["q"],["a"],["g"],["k"],["m"],["u"],["u"],["n"],["t"],["r"],["b"],["d"],["h"],["v"],["x"],["c"],["c"],["k"],["q"],["c"],["v"],["o"],["g"],["o"],["a"],["e"],["i"],["m"],["o"],["l"],["h"],["d"],["d"],["#"],["g"],["r"],["k"],["i"],["n"],["u"],["k"],["d"],["q"],["j"],["i"],["i"],["i"],["s"],["q"],["a"],["k"],["h"],["e"],["c"],["p"],["g"],["j"],["p"],["a"],["c"],["j"],["p"],["e"],["f"],["w"],["j"],["v"],["g"],["h"],["v"],["b"],["m"],["b"],["r"],["s"],["f"],["n"],["z"],["d"],["i"],["q"],["e"],["i"],["y"],["u"],["k"],["j"],["k"],["k"],["k"],["c"],["q"],["a"],["r"],["#"],["o"],["v"],["z"],["d"],["l"],["v"],["x"],["n"],["h"],["t"],["b"],["c"],["a"],["q"],["m"],["h"],["t"],["c"],["m"],["j"],["k"],["q"],["l"],["t"],["u"],["z"],["a"],["g"],["l"],["b"],["a"],["z"],["d"],["d"],["b"],["r"],["v"],["k"],["x"],["i"],["r"],["o"],["g"],["x"],["y"],["x"],["s"],["k"],["f"],["n"],["#"],["m"],["k"],["n"],["z"],["g"],["y"],["s"],["k"],["p"],["l"],["i"],["v"],["p"],["l"],["w"],["l"],["y"],["m"],["n"],["z"],["a"],["h"],["d"],["x"],["p"],["#"],["x"],["e"],["f"],["c"],["v"],["y"],["m"],["n"],["w"],["l"],["v"],["u"],["d"],["o"],["u"],["z"],["q"],["s"],["b"],["s"],["o"],["h"],["a"],["b"],["k"],["i"],["v"],["a"],["y"],["j"],["f"],["s"],["y"],["k"],["n"],["q"],["v"],["t"],["n"],["b"],["r"],["s"],["q"],["r"],["p"],["p"],["m"],["#"],["o"],["v"],["f"],["i"],["e"],["p"],["z"],["s"],["o"],["f"],["o"],["d"],["v"],["l"],["s"],["#"],["d"],["j"],["q"],["k"],["k"],["d"],["o"],["a"],["t"],["#"],["s"],["#"],["d"],["t"],["z"],["i"],["u"],["f"],["q"],["y"],["g"],["q"],["w"],["z"],["f"],["u"],["e"],["z"],["n"],["v"],["g"],["e"],["n"],["z"],["i"],["z"],["o"],["v"],["q"],["a"],["l"],["w"],["h"],["t"],["q"],["e"],["j"],["u"],["x"],["f"],["s"],["a"],["p"],["k"],["b"],["n"],["u"],["v"],["h"],["p"],["h"],["y"],["w"],["#"],["y"],["p"],["s"],["p"],["e"],["g"],["b"],["v"],["s"],["d"],["r"],["m"],["o"],["i"],["e"],["c"],["o"],["l"],["k"],["m"],["i"],["g"],["#"],["w"],["b"],["e"],["h"],["n"],["p"],["j"],["m"],["y"],["k"],["w"],["c"],["y"],["d"],["k"],["z"],["p"],["l"],["l"],["u"],["d"],["g"],["n"],["l"],["j"],["s"],["d"],["y"],["y"],["t"],["s"],["y"],["n"],["c"],["f"],["v"],["m"],["r"],["u"],["r"],["z"],["r"],["k"],["v"],["b"],["o"],["l"],["w"],["t"],["j"],["r"],["b"],["v"],["#"],["b"],["u"],["c"],["o"],["w"],["k"],["y"],["l"],["i"],["b"],["y"],["#"],["a"],["h"],["u"],["y"],["a"],["a"],["g"],["z"],["e"],["k"],["d"],["u"],["i"],["e"],["c"],["g"],["t"],["m"],["g"],["x"],["g"],["g"],["a"],["s"],["q"],["n"],["b"],["g"],["o"],["e"],["y"],["r"],["x"],["p"],["k"],["o"],["q"],["e"],["i"],["x"],["t"],["s"],["k"],["g"],["l"],["#"],["p"],["o"],["r"],["i"],["x"],["a"],["n"],["s"],["l"],["c"],["c"],["x"],["b"],["f"],["l"],["s"],["h"],["p"],["u"],["g"],["l"],["m"],["x"],["a"],["k"],["h"],["i"],["d"],["h"],["n"],["m"],["w"],["u"],["c"],["y"],["w"],["j"],["x"],["a"],["n"],["r"],["b"],["m"],["u"],["z"],["z"],["o"],["z"],["i"],["w"],["w"],["y"],["b"],["i"],["v"],["m"],["n"],["g"],["t"],["d"],["d"],["o"],["k"],["u"],["x"],["v"],["r"],["x"],["u"],["b"],["q"],["f"],["s"],["p"],["p"],["v"],["v"],["k"],["z"],["z"],["f"],["l"],["g"],["o"],["m"],["y"],["o"],["j"],["h"],["y"],["h"],["#"],["k"],["s"],["z"],["n"],["b"],["z"],["s"],["a"],["u"],["j"],["x"],["e"],["d"],["b"],["d"],["y"],["c"],["h"],["l"],["g"],["c"],["u"],["t"],["l"],["t"],["e"],["b"],["g"],["g"],["k"],["y"],["i"],["k"],["p"],["h"],["t"],["u"],["i"],["i"],["x"],["l"],["b"],["j"],["m"],["d"],["d"],["p"],["n"],["j"],["u"],["m"],["q"],["y"],["b"],["y"],["n"],["t"],["y"],["d"],["s"],["i"],["#"],["s"],["x"],["n"],["e"],["s"],["i"],["b"],["i"],["o"],["t"],["u"],["o"],["i"],["u"],["h"],["a"],["f"],["k"],["w"],["k"],["d"],["q"],["x"],["e"],["u"],["d"],["f"],["p"],["p"],["h"],["k"],["t"],["o"],["v"],["b"],["e"],["w"],["a"],["e"],["a"],["s"],["d"],["f"],["f"],["l"],["d"],["k"],["z"],["g"],["u"],["t"],["w"],["o"],["o"],["j"],["v"],["c"],["j"],["w"],["v"],["i"],["d"],["k"],["r"],["p"],["p"],["o"],["o"],["d"],["c"],["a"],["s"],["p"],["j"],["k"],["l"],["y"],["n"],["i"],["l"],["#"]]:
    print(s.input(w[0]))