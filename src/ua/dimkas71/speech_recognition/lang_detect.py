# -*- coding: utf-8 -*-
from fast_langdetect import detect_langs, detect

if __name__ == '__main__':
    print(detect_langs("hello world"))
    print(detect_langs("Привіт Маруся how are you"))
    print(detect_langs("Привет моя мамуля"))
    print(detect_langs("Bonjour tout le monde"))
    print(detect_langs("नमस्ते, दुनिया!", low_memory=False))
    print(detect_langs("नमस्ते, दुनिया!", low_memory=False))
    print(detect_langs("Merhaba, dünya!"))
    print(detect_langs("Halo, dunia!", low_memory=False))
    print(detect("Halo, dunia!", low_memory=False))
