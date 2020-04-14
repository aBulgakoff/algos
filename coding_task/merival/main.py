from collections import defaultdict

if __name__ == '__main__':
    text = 'Platon made bamboo boats'
    vowels = set('aeiou')

    result_w_qty = defaultdict(list)
    for word in text.lower().split():
        all_vows_of_word = [ch for ch in word if ch in vowels]
        result_w_qty[
            tuple([frozenset(all_vows_of_word), len(word)])
        ].append(len(all_vows_of_word))

    result_w_average = {k: sum(v) / len(v) for k, v in result_w_qty.items()}

    print('\n'.join(f'{set(k[0]), k[1]} -> {int(v) if int(v) == v else v}'
                    for k, v
                    in sorted(result_w_average.items(), reverse=True)))
