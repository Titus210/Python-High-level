#!/usr/bin/python3
incmplt_1 = ["Tit", "i", "a", "intell", "bo"]
incmplt_2 = ["us", "s", "n", "igent","y"]
complete = [i + j for i, j in zip(incmplt_1,incmplt_2)]
print(complete)
