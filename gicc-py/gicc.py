# -*- coding: utf-8 -*-
# Copyright (c) 2023, Harry Huang
# @ MIT License

class CodeConverter:
    '''
    Genius Invokation Code Converter, GICC.
    See https://github.com/isHarryh/GI-Code-Converter

    :author: Harry Huang
    :version: 0.1
    '''

    __BASE64_CHARS      = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    __BITS_PER_CARD     = 12
    __CARDS_IN_DECK     = 33
    __BITS_PER_DECK     = __BITS_PER_CARD * __CARDS_IN_DECK                          # = 396 (bits)
    __STRING_LENGTH     = (__BITS_PER_DECK // 24 + (__BITS_PER_DECK % 24 > 0)) * 4    # = 68 (chars)

    @staticmethod
    def decode(code:str) -> list:
        '''
        Converts the Sharing Code to a card IDs list.
        :param code: The given Sharing Code string.
        :returns: The converted card IDs list.
        :raises ValueError: If illegal input was given.
        '''
        if len(code) != CodeConverter.__STRING_LENGTH:
            raise ValueError(f"Illegal string length {len(code)} ({CodeConverter.__STRING_LENGTH} expected)")
        raw = CodeConverter.__base64_str2int(code)
        raw = CodeConverter.__remove_cover(raw, CodeConverter.__STRING_LENGTH * 6 - CodeConverter.__BITS_PER_DECK)
        ordered = CodeConverter.__order(raw, CodeConverter.__BITS_PER_DECK)

        deck = []
        mask = (1 << CodeConverter.__BITS_PER_CARD) - 1
        for i in range(CodeConverter.__CARDS_IN_DECK):
            offset = CodeConverter.__BITS_PER_DECK - (i + 1) * CodeConverter.__BITS_PER_CARD
            deck.append(ordered >> offset & mask)
        return deck

    @staticmethod
    def encode(deck:list) -> str:
        '''
        Converts the card IDs list to a Sharing Code.
        :param deck: The given card IDs list.
        :returns: The converted Sharing Code.
        :raises ValueError: If illegal input was given.
        '''
        if len(deck) != CodeConverter.__CARDS_IN_DECK:
            raise ValueError(f"Illegal deck length {len(deck)} ({CodeConverter.__CARDS_IN_DECK} expected)")
        ordered = 0
        for i in range(len(deck)):
            card = deck[i]
            if card < 0 or card > (1 << CodeConverter.__BITS_PER_CARD) - 1:
                raise ValueError(f"Illegal card ID {card}")
            ordered = ordered << CodeConverter.__BITS_PER_CARD | card
        
        raw = CodeConverter.__disorder(ordered, CodeConverter.__BITS_PER_DECK)
        code = CodeConverter.__base64_int2str(raw, CodeConverter.__BITS_PER_DECK)
        return code
    
    @staticmethod
    def __base64_str2int(data:str) -> int:
        length = len(data)
        if length % 4 != 0:
            raise ValueError(f"Illegal string length {length} (4n expected)")
        result = 0
        for i in range(length):
            result += CodeConverter.__BASE64_CHARS.index(data[i]) << (length - i - 1) * 6
        return result
    
    @staticmethod
    def __base64_int2str(data:int, data_size:int) -> str:
        result = ""
        for i in range(data_size // 24 + (data_size % 24 != 0)):
            for j in range(4):
                offset = data_size - i * 24 - (j + 1) * 6
                value = (data >> offset if offset >= 0 else data << -offset) & 0b111111
                result += CodeConverter.__BASE64_CHARS[value]
        return result

    @staticmethod
    def __remove_cover(data:int, cover_size:int) -> int:
        cover_data = data & (1 << cover_size) - 1
        if cover_data != 0:
            raise ValueError(f"Illegal cover bits {bin(cover_data)} (0b0 expected)")
        return data >> cover_size

    @staticmethod
    def __order(data:int, data_size:int) -> int:
        evens, odds, odds_size = 0, 0, 0
        for i in range(data_size):
            offset = data_size - i - 1
            if i % 16 < 8:
                evens = (evens << 1) | (data >> offset & 1)
            else:
                odds = (odds << 1) | (data >> offset & 1)
                odds_size += 1
        return evens << odds_size | odds
    
    @staticmethod
    def __disorder(data:int , data_size:int) -> int:
        result = 0
        split_byte_pos = data_size // 16
        for i in range(data_size // 8 + (data_size % 8 != 0)):
            raw_offset = data_size - (i + 1) * 8
            new_idx = ((i - split_byte_pos) * 2 - 1) if i > split_byte_pos else (i * 2)
            new_offset = data_size - (new_idx + 1) * 8
            value = ((data >> raw_offset) if raw_offset >= 0 else (data << -raw_offset)) & 0b11111111
            result |= value << new_offset if new_offset >= 0 else (value >> -new_offset)
        return result


if __name__ == '__main__':
    while True:
        s = input("Input Code: ")
        try:
            print(f"Card IDs result: {CodeConverter.decode(s)}")
        except Exception as e:
            print(f"Error: {e}")
