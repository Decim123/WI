import random

def generate_accept_code():
    # случайное 6-значное число
    accept_code = random.randint(100000, 999999)
    return accept_code


#if __name__ == "__main__":
#    accept_code = generate_accept_code()
#    print("Сгенерированный код подтверждения:", accept_code)
