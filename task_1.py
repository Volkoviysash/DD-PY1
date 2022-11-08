from pprint import pprint


# TODO решить с помощью list comprehension и распечатать его
list_output = [{"bin": bin(number),
                "dec": number,
                "hex": hex(number),
                "oct": oct(number)}
               for number in range(16)]

pprint(list_output)
