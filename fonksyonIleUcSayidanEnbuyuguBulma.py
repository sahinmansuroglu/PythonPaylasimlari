def enBuyukBul1(s1,s2,s3):
    if s1>s2 and s1>s3:
        return s1
    if s2>s1 and s2>s3:
        return s2
    if s3>s1 and s3>s2:
        return s3

def enBuyukBul2(s1,s2,s3):
    if s1>s2 and s1>s3:
        return s1
    elif s2>s3:
        return s2
    else:
        return s3
print(enBuyukBul2(8,6,3))
