def reverseString(s):
    left,right=0,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+= 1
        right-= 1
    print(s)

input_str=list('hello')
reverseString(input_str)
output_str = ''.join(input_str) 
print("Reversed string:", output_str)
name = "python"
name_list = list(name)
name_list[0], name_list[-1] = name_list[-1], name_list[0]
new_name = ''.join(name_list)
print(new_name) 