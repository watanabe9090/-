import base64

is_letter = lambda ch : (ch >= 65 and ch <= 90) or (ch >= 97 and ch <= 122)
is_upper = lambda ch : (ch >= 65 and ch <= 90) 
is_lower = lambda ch : (ch >= 97 and ch <= 122)

@staticmethod
def _decript_ceaser(text: str, shift) -> str:
    shift %= 26 
    di_text = '' 
    for ch in text:
        ch_int = ord(ch)
        
        if is_letter(ch_int) and is_upper(ch_int):
            ch_int -= 65
            ch_int -= shift
            if ch_int <= 0: 
                ch_int *= -1
            ch_int %= 26
            ch_int += 65
        elif is_letter(ch_int) and  is_lower(ch_int):
            ch_int -= 97
            ch_int -= shift
            if ch_int <= 0: 
                ch_int *= -1
            ch_int %= 26
            ch_int += 97
        di_text += chr(ch_int)
    return di_text

@staticmethod
def _encript_ceaser(text: str, shift) -> str:
    shift %= 26 
    ci_text = '' 
    for ch in text:
        ch_int = ord(ch)
        
        if is_letter(ch_int) and is_upper(ch_int):
            ch_int -= 65
            ch_int += shift
            ch_int %= 26
            ch_int += 65
        elif is_letter(ch_int) and  is_lower(ch_int):
            ch_int -= 97
            ch_int += shift
            ch_int %= 26
            ch_int += 97
        ci_text += chr(ch_int)
    return ci_text

@staticmethod
def _from_base_64(base64_text: str) -> str:
    base64_bytes = base64_text.encode('ascii')
    text_bytes = base64.b64decode(base64_bytes)
    text = text_bytes.decode('ascii')
    return text
    

@staticmethod
def _to_base_64(text: str) -> str:
    text_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('ascii')
    return base64_text
    
@staticmethod
def encript(text: str) -> str:
    base64 = _to_base_64(text)
    encripted = _encript_ceaser(base64, 17)
    return encripted

@staticmethod
def decript(text: str) -> str:
    base64 = _to_base_64(text)
    encripted = _encript_ceaser(base64, 17)
    return encripted


# print(encript('1iid asld 21 po9dh12987 4y24978 {}sad sad 12d '))

print(_from_base_64('YXNkYXNkYXNk'))

