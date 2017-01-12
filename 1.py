# Caesar substitution
# Shift by 2
# origstr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# Ciphertext suggests using same substitution on URL, which is, at essence,
# "map.html"
origstr = "map"

transtable = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")

result = origstr.translate(transtable)

print("http://www.pythonchallenge.com/pc/def/{}.html".format(result))
