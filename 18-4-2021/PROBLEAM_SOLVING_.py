
# Something What All Programmers need to know

# BITWISE OPERATOR

# 1. (&) -> it will do bitwise AND on binary of operands
#       E.G. A & B will give bitwise AND of A,B
#            - 5 & 4 = 4 EXP: binary of 5 is 101 and binary of 4 is 100 so AND of (101,100) is 100 which is binary of 4

# 2. (|) -> it will do bitwise OR on binary of operands
#       E.G. A | B will give bitwise OR of A,B
#            - 5 & 4 = 5 EXP: binary of 5 is 101 and binary of 4 is 100 so OR of (101,100) is 101 which is binary of 5

# 3. (^) -> it will do bitwise XOR on binary of operands
#       E.G. A ^ B will give bitwise XOR of A,B
#            - 5 ^ 4 = 1 EXP: binary of 5 is 101 and binary of 4 is 100 so XOR of (101,100) is 001 which is binary of 1

## AND HERE I WANT ALL READERS TO EXPLORE WHAT IS 32 BIT - 64 BIT ARCHITECTURE, 2's COMPLEMENT, LEFT SHIFT & RIGHT SHIFT THEN READ BELOW

# 4. (~) -> it will do bitwise OR on binary of operand
#       E.G. ~A will give bitwise NOR of A
#            - ~5 = -6 EXP: binary of 5 is 101 and so NOT of (101) is 010 which is binary of 2 BUTTTTTTTTTTT we will get -6 why? answer is below
#               negative number will store based on 2's Complimant

# 5. (<<) -> it will do LEFT SHIFT on binary of left operand by right operand
#       E.G. A << B will LEFT SHIFT binary of A for B times
#            - 5 << 2 =  1 EXP: binary of 5 is 101 and 1'st left shift of 101 is 1010 and 2'nd left shift of 101 is 10100 = 20 in int

# 6. (>>) -> it will do RIGHT SHIFT on binary of left operand by right operand
#       E.G. A >> B will RIGHT SHIFT binary of A for B times
#            - 5 >> 2 =  1 EXP: binary of 5 is 101 and 1'st left shift of 101 is 010 and 2'nd left shift of 101 is 001 = 1 in int

## NOW QUE 1 ) PRINT THE FOLLOWING PATTERN FOR THE VALUE OF N:
#    *
#   ***
#  *****
# *******
#*********
# above is for n=5



n = int(input())

for i in range(0,n):
    print(" "*(n-1-i) + "*"*(2*i-1))
