'''String rotator
   prompts for input, enter a word...'''
print(__doc__)
print((lambda x: [x[i:]+x[:i] for i in range(len(x))])(input()))


# found this code on solo learn....i didnt write it.