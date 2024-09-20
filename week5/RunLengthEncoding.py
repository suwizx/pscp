"""Run Length Encoding"""

def main():
    """Run Length Encoding"""
    prompt = input()
    char_num = len(prompt)
    char_now = 0
    def compress_string(s):
        if not s:
            return ""
        
        result = []
        current_char = s[0]
        count = 1
        
        for char in s[1:]:
            if char == current_char:
                count += 1
            else:
                result.append(f"{count}{current_char}")
                current_char = char
                count = 1
        
        result.append(f"{count}{current_char}")
        return ''.join(result)
    print(compress_string(prompt))
main()
