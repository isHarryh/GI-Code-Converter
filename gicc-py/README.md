GI-Code-Converter (Python)
==========

## 环境要求 <sub>Requirements</sub>
- 语言级别 (Language Level)：Python 3
- 依赖库 (Dependencies)：无 (None)


## 接口定义 <sub>Interfaces</sub>
- 解码 (Decoding)：
    ```
    (method) CodeConverter.decode(code:str) -> list

    Converts the Sharing Code to a card IDs list.

    :param code: The given Sharing Code string.
    :returns: The converted card IDs list.
    :raises ValueError: If illegal input was given.
    ```
- 编码 (Encoding)：
    ```
    (method) CodeConverter.encode(deck:list) -> str
    
    Converts the card IDs list to a Sharing Code.
    :param deck: The given card IDs list.
    :returns: The converted Sharing Code.
    :raises ValueError: If illegal input was given.
    ```


## 用例 <sub>Examples</sub>
代码 (Code)：
```python
from gicc import CodeConverter

code = "AvAA3wEOAAAg4D0PAxDQ8YEPCFAQ9pUPC2BA/LgPC9HQCr0QDLEgC9kQDeGQDt4QDfAA"
print(CodeConverter.decode(code))

deck = [32, 1, 2, 61, 61, 129, 129, 149, 180, 184, 189, 189, 194, 217, 217, 222, 223, 223, 224, 224, 241, 241, 245, 246, 246, 252, 253, 266, 267, 267, 270, 270, 271]
print(CodeConverter.encode(deck))
```

输出 (Output)：
```
[32, 1, 2, 61, 61, 129, 129, 149, 180, 184, 189, 189, 194, 217, 217, 222, 223, 223, 224, 224, 241, 241, 245, 246, 246, 252, 253, 266, 267, 267, 270, 270, 271]
AvAA3wEOAAAg4D0PAxDQ8YEPCFAQ9pUPC2BA/LgPC9HQCr0QDLEgC9kQDeGQDt4QDfAA
```
