list=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand']
def num_to_string(num):
    string=''
    if num == 1000:
            return list[0] + list[28]
    if num % 100 == 0:
            return list[(num // 100) - 1] + list[27]
    if num > 100:
        string = string + list[(num // 100) - 1] + list[27] + 'and'
    num = num % 100
    if num == 10:
        return string + list[9]
    if num % 10 == 0:
        return string + list[((num //10) + 17)]
    if num <= 20:
        string+= list[num-1]
    else:
        string = string + list[(num // 10) + 17] + list[(num % 10) - 1 ]
    return (string)
d=''
for i in range(1,1001):
    print(num_to_string(i))
    d+=num_to_string(i)
print(len(d))