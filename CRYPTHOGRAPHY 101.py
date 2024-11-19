from sympy import isprime, gcd
from Crypto.Util.number import long_to_bytes
from sympy.ntheory import factorint

# Given values
c = 231722077914684998818993776518942509384465803531548983146869754932667754136315007943497593396644630089073196170276638447665765624960333289097324447779290700092664403080584161276778064977902852018557301618273474139777712464709585187730351308079009718870031364399745764326436147001877583703027251271265576350621173
e = 65537
n = 257208938346934642693512128888810986151634836498153528507638790770764504946719195736987613302526116425873247750032929224521429342437621496424825810959518932424007107126934957421561529561264636001476988808843995824395131838577901446930016348590793828420808295335603083382120208905347497068915850813369038886980997

# Step 1: Attempt to factorize n
factors = factorint(n)

# Check if factorization was successful (we expect two prime factors p and q if this is RSA)
if len(factors) == 2:
    p, q = list(factors.keys())
    
    # Verify that p and q are primes (sanity check)
    if isprime(p) and isprime(q) and p * q == n:
        # Step 2: Calculate Euler's totient function
        phi = (p - 1) * (q - 1)
        
        # Step 3: Compute the private exponent d
        d = pow(e, -1, phi)
        
        # Step 4: Decrypt the ciphertext
        m = pow(c, d, n)
        
        # Step 5: Convert the decrypted message from integer to bytes
        decrypted_message = long_to_bytes(m)
        print(decrypted_message.decode(errors='ignore'))
    else:
        print("Factorization failed or factors are not prime.")
else:
    print("Factorization failed; n could not be decomposed into two primes.")