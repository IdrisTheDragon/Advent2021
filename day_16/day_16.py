bits = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}






def b_to_i(binary):
    return int(binary,2)

def h_to_b(hexr):
    binary = ""
    for c in hexr:
        binary += bits[c]

    print(binary)
    return binary

sum = 0

def process_packet(packet):
    global sum
    print('processing:', packet)
    V = packet[0:3]
    sum += b_to_i(V)
    T = packet[3:6]
    print('V',b_to_i(V),'T',b_to_i(T))
    if T == '100': #4
        i = 6
        num = ''
        while True:
            # print(packet[i:i+5])
            num += packet[i+1:i+5]
            if packet[i] == '0':
                break
            i += 5
        print('num',b_to_i(num))
        return i +5 , b_to_i(num)
    numBits = 0
    nums = []
    if packet[6] == '0':
        length = packet[7:6+16]
        print(len(length),length,b_to_i(length))
        while numBits < b_to_i(length):
            i,num = process_packet(packet[6+16+numBits:])
            numBits += i
            nums.append(num)
        numBits = 6+16+numBits
    elif packet[6] == '1':
        length = packet[7:6+12]
        print(len(length),length,b_to_i(length))
        numBits = 0
        for _ in range(0,b_to_i(length)):
            i,num = process_packet(packet[6+12+numBits:])
            numBits += i
            nums.append(num)
        numBits = 6+12+numBits
    result = 0
    print('nums',nums,T)
    if T == '000':
        for num in nums:
            result += num
    elif T == '001':
        result = 1
        for num in nums:
            result *= num
    elif T == '010':
        result = min(nums)
    elif T == '011':
        result = max(nums)
    elif T == '101':
        result = 1 if nums[0] > nums[1] else 0
    elif T == '110':
        result = 1 if nums[0] < nums[1] else 0
    elif T == '111':
        result = 1 if nums[0] == nums[1] else 0

    
    return numBits, result

       


file = open("input.txt","r")

hexr = file.readline()[:-1]

binary = h_to_b(hexr)
i, num = process_packet(binary)
print('part1',sum)
print('part2',num)