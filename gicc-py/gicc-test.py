from gicc import CodeConverter

code = "AvAA3wEOAAAg4D0PAxDQ8YEPCFAQ9pUPC2BA/LgPC9HQCr0QDLEgC9kQDeGQDt4QDfAA"
print(CodeConverter.decode(code))

deck = [32, 1, 2, 61, 61, 129, 129, 149, 180, 184, 189, 189, 194, 217, 217, 222, 223, 223, 224, 224, 241, 241, 245, 246, 246, 252, 253, 266, 267, 267, 270, 270, 271]
print(CodeConverter.encode(deck))
