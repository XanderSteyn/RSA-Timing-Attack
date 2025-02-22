import time
import random
from Crypto.Util.number import getPrime, inverse
import sys
import os
import multiprocessing

def PreciseModExp(Base, Exponent, Modulus):
    Result = 1
    Base = Base % Modulus
    for Bit in bin(Exponent)[2:]:
        Result = (Result * Result) % Modulus
        if Bit == '1':
            Result = (Result * Base) % Modulus
    return Result

def GenerateRSAKeys(Bits=512):
    Prime1, Prime2 = getPrime(Bits), getPrime(Bits)
    Modulus = Prime1 * Prime2
    Totient = (Prime1 - 1) * (Prime2 - 1)
    PublicExponent = 65537
    PrivateExponent = inverse(PublicExponent, Totient)
    return (Modulus, PublicExponent), (Modulus, PrivateExponent)

def AttackBit(Modulus, CurrentGuessedBits, NumTrials, BitPosition):
    TimeFor0, TimeFor1 = 0, 0
    for _ in range(NumTrials):
        message = random.randint(2, Modulus - 1)
        StartTime = time.perf_counter_ns()
        PreciseModExp(message, int('0' + CurrentGuessedBits, 2), Modulus)
        EndTime = time.perf_counter_ns()
        TimeFor0 += EndTime - StartTime
        StartTime = time.perf_counter_ns()
        PreciseModExp(message, int('1' + CurrentGuessedBits, 2), Modulus)
        EndTime = time.perf_counter_ns()
        TimeFor1 += EndTime - StartTime
    
    if TimeFor1 > TimeFor0:
        return ('1', BitPosition)
    else:
        return ('0', BitPosition)

def TimingAttack(Modulus, PublicExponent, PrivateExponent, NumTrials=100, BatchSize=50):
    GuessedBits = ""
    Pool = multiprocessing.Pool(processes = multiprocessing.cpu_count())
    BitLength = len(bin(PrivateExponent)) - 2
    Tasks = []

    for BitPosition in range(BitLength):
        Tasks.append(Pool.apply_async(AttackBit, (Modulus, GuessedBits, NumTrials, BitPosition)))

    Pool.close()
    Pool.join()

    for task in Tasks:
        Result, BitPosition = task.get()
        GuessedBits += Result

    return GuessedBits

if __name__ == '__main__':
    PublicKey, PrivateKey = GenerateRSAKeys()
    Modulus, PublicExponent = PublicKey
    _, PrivateExponent = PrivateKey

    while True:
        GuessedPrivateKey = ""
        StartTime = time.perf_counter()
        GuessedPrivateKey = TimingAttack(Modulus, PublicExponent, PrivateExponent)
        EndTime = time.perf_counter()

        os.system("cls")
        sys.stdout.write("Guessed private key")
        print()
        sys.stdout.write(f"{GuessedPrivateKey}")
        print()
        sys.stdout.write("Actual private key")
        print()
        sys.stdout.write(f"{bin(PrivateExponent)}")
        sys.stdout.flush()


        if GuessedPrivateKey == bin(PrivateExponent)[2:]:
            print(f"\nMatch found!\n")
            print(GuessedPrivateKey)
            break
        else:
            print()
            print("\nMismatch, Trying Again...\n")