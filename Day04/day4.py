

if __name__ == "__main__":
    f = open("input.txt")
    inpt = f.read().strip()
    f.close()
    print(inverse_captcha(inpt))    
    print(inverse_captcha_halfway(inpt))    
