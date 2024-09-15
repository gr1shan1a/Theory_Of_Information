from collections import Counter
import math

text = "Там королевич мимоходом пленяет грозного царя.У наших ушки на макушке! Чуть утро осветило пушки и леса синие верхушки - французы тут как тут."

counter = Counter(text)
total = sum(counter.values())
probabilities = {char: count / total for char, count in counter.items()}

sorted_probabilities = {k: v for k, v in sorted(probabilities.items(), key=lambda item: item[1], reverse=True)}

codes = {}
codeword_lengths = {}
n = len(sorted_probabilities)
previous_length = 0

for i, (char, probability) in enumerate(sorted_probabilities.items()):
    codeword = bin(i)[2:].zfill(math.ceil(math.log2(n)))
    codeword_lengths[char] = len(codeword)
    codes[char] = codeword

print("Символ\tКод\tДлина")
for char, code in codes.items():
    print(f"{char}\t{code}\t{codeword_lengths[char]}")

entropy = -sum(probability * math.log2(probability) for probability in probabilities.values())
print(f"\nЭнтропия: {entropy}")

mean_codeword_length = sum(probability * codeword_lengths[char] for char, probability in probabilities.items())
unequal_encoding_rate = mean_codeword_length / entropy

print(f"Средняя длина кодовых слов: {mean_codeword_length}")
print(f"Средняя скорость неравномерного кодирования: {unequal_encoding_rate}")


