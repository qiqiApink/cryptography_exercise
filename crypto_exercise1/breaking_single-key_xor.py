import base64

def get_english_score(input_bytes):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def single_char_xor(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes


def bruteforce_single_char_xor(ciphertext):
    potential_messages = []
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        score = get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)
    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]['key']


def break_repeating_key_xor(ciphertext):
    average_distances = []
    for keysize in range(2,41):
        distances = []
        chunks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
        while True:
            try:
                chunk_1 = chunks[0]
                chunk_2 = chunks[1]
                distance = calculate_hamming_distance(chunk_1, chunk_2)
                distances.append(distance/keysize)
                del chunks[0]
                del chunks[1]
            except Exception as e:
                break
        result = {
            'key': keysize,
            'avg distance': sum(distances) / len(distances)
            }
        average_distances.append(result)

    possible_key_length = sorted(average_distances, key=lambda x: x['avg distance'])[0]['key']
    possible_plaintext = []
    key = b''
    for i in range(possible_key_length):
        block = b''
        for j in range(i, len(ciphertext), possible_key_length):
            block += bytes([ciphertext[j]])
        key += bytes([bruteforce_single_char_xor(block)])
    possible_plaintext.append((repeating_key_xor(ciphertext, key), key))
    return max(possible_plaintext, key=lambda x: get_english_score(x[0]))


def repeating_key_xor(message_bytes, key):
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes


def calculate_hamming_distance(input_bytes_1, input_bytes_2):
    hamming_distance = 0
    for b1, b2 in zip(input_bytes_1, input_bytes_2):
        difference = b1 ^ b2
        hamming_distance += sum([1 for bit in bin(difference) if bit == '1'])
    return hamming_distance


def main():
    with open('6.txt') as input_file:
        ciphertext = base64.b64decode(input_file.read())
    result, key = break_repeating_key_xor(ciphertext)
    print("Key: {}\nMessage: {}".format(key, result))


if __name__ == '__main__':
    main()
