import argparse
from collections import deque
from collections import Counter
from functools import reduce
from itertools import combinations
import json
from math import gcd


def predicted(k_value, radius):
    if radius % 2:
        return 2 * k_value <= radius * radius - 1
    if 2 * k_value <= radius * radius - radius:
        return True
    if 2 * k_value > radius * radius:
        return False
    return k_value % 2 == 0 if radius % 4 == 0 else k_value % 4 == 2


def adjacency(order, generator):
    return tuple(((vertex // order + generator // order) % 2) * order
                 + (vertex % order + generator % order) % order
                 for vertex in range(2 * order))


def diameter(neighbors, size):
    distances = [-1] * size
    distances[0] = 0
    queue = deque([0])
    visited = 1
    maximum = 0
    while queue:
        vertex = queue.popleft()
        next_distance = distances[vertex] + 1
        for table in neighbors:
            target = table[vertex]
            if distances[target] < 0:
                distances[target] = next_distance
                maximum = next_distance
                visited += 1
                queue.append(target)
    return maximum if visited == size else None


def exhaustive(maximum_k, maximum_radius):
    pair_count = 0
    rows = []
    for k_value in range(1, maximum_k + 1):
        order = 2 * k_value
        size = 2 * order
        tables = [adjacency(order, generator) for generator in range(size)]
        inverses = [(generator // order) * order + (-generator % order) % order
                    for generator in range(size)]
        best = None
        for first, second in combinations(range(size), 2):
            pair_count += 1
            result = diameter([tables[first], tables[inverses[first]],
                               tables[second], tables[inverses[second]]], size)
            if result is not None and (best is None or result < best):
                best = result
        assert best is not None
        for radius in range(1, maximum_radius + 1):
            assert (best <= radius) == predicted(k_value, radius), (k_value, radius, best)
        rows.append({'k': k_value, 'minimum_diameter': best})
    return {'k_range': [1, maximum_k], 'radius_range': [1, maximum_radius],
            'distinct_pairs': pair_count, 'comparisons': maximum_k * maximum_radius,
            'minimum_diameters': rows}


def sufficient_families(maximum_t):
    family_count = 0
    element_count = 0
    for t_value in range(1, maximum_t + 1):
        for j_value in range(t_value):
            if t_value % 2 and j_value % 2:
                continue
            deficit = t_value * t_value - j_value
            order = 4 * deficit
            half = t_value // 2
            if t_value % 2 == 0:
                first = (half % 2) * order + (t_value + 1) % order
                second = ((1 - half) % 2) * order + (1 - t_value) % order
            else:
                first = ((half + 1) % 2) * order + (2 * (half + 1) - deficit) % order
                second = ((-half) % 2) * order + (deficit - 2 * half) % order
            assert first != second
            inverse_first = (first // order) * order + (-first % order) % order
            inverse_second = (second // order) * order + (-second % order) % order
            result = diameter([adjacency(order, generator) for generator in
                               [first, inverse_first, second, inverse_second]], 2 * order)
            assert result is not None and result <= 2 * t_value, (t_value, j_value)
            entries = [2 * (t_value - j_value), -2 * (t_value + j_value),
                       2 * (t_value - 1), 2 * (t_value + 1)]
            assert reduce(gcd, entries) == 2
            determinant = entries[0] * entries[3] - entries[1] * entries[2]
            assert determinant == 8 * deficit
            for first_coefficient, second_coefficient in [entries[:2], entries[2:]]:
                assert (first_coefficient * (first // order)
                        + second_coefficient * (second // order)) % 2 == 0
                assert (first_coefficient * (first % order)
                        + second_coefficient * (second % order)) % order == 0
            family_count += 1
            element_count += 2 * order
    return {'t_range': [1, maximum_t], 'admissible_families': family_count,
            'group_elements': element_count}


def cylinder(t_value, parity, target):
    if parity == 0:
        quotient = (target + t_value) // (2 * t_value + 1)
        remainder = target - (2 * t_value + 1) * quotient
        return quotient - remainder, quotient + remainder
    quotient, remainder = divmod(target, 2 * t_value + 1)
    return quotient + 1 - remainder + t_value, quotient + remainder - t_value


def lower_formulas(maximum_t):
    odd_count = 0
    even_count = 0
    for t_value in range(maximum_t + 1):
        bound = 2 * t_value * (t_value + 1)
        for parity in range(2):
            for target in range(-bound, bound + 1):
                first, second = cylinder(t_value, parity, target)
                assert (first + second) % 2 == parity
                assert t_value * first + (t_value + 1) * second == target
                assert abs(first) + abs(second) <= 2 * t_value + 1
                odd_count += 1
        if t_value == 0:
            continue
        bound = 2 * t_value * (t_value - 1)
        for parity in range(2):
            for target in range(-bound - t_value, bound + t_value + 1):
                shift = next(value for value in [-1, 0, 1]
                             if abs(target - value * t_value) <= bound)
                first, second = cylinder(t_value - 1, (parity - shift) % 2,
                                         target - shift * t_value)
                second += shift
                assert (first + second) % 2 == parity
                assert (t_value - 1) * first + t_value * second == target
                assert abs(first) + abs(second) <= 2 * t_value
                even_count += 1
    return {'t_range': [0, maximum_t], 'odd_representations': odd_count,
            'even_representations': even_count}


def even_invariant_factors():
    rows = []
    pair_count = 0
    for first_order in [4, 6]:
        for multiplier in range(1, 5):
            second_order = first_order * multiplier
            size = first_order * second_order
            tables = [tuple(((vertex // second_order + generator // second_order)
                             % first_order) * second_order
                            + (vertex % second_order + generator % second_order) % second_order
                            for vertex in range(size)) for generator in range(size)]
            inverses = [(-(generator // second_order) % first_order) * second_order
                        + (-(generator % second_order) % second_order)
                        for generator in range(size)]
            best = None
            for first, second in combinations(range(size), 2):
                pair_count += 1
                result = diameter([tables[first], tables[inverses[first]],
                                   tables[second], tables[inverses[second]]], size)
                if result is not None and (best is None or result < best):
                    best = result
            assert best is not None and size <= 2 * best * best
            if size == 2 * best * best:
                assert best % first_order == 0
            if best % 2:
                assert size <= 2 * best * best - 2
            rows.append({'c': first_order, 'k': multiplier, 'order': size,
                         'minimum_diameter': best})
    return {'c_values': [4, 6], 'k_range': [1, 4], 'distinct_pairs': pair_count,
            'groups': rows}


def odd_residue_bound(first_order, radius):
    quotient, remainder = divmod(radius, first_order)
    if remainder < (first_order - 1) // 2:
        return 2 * quotient * quotient
    if remainder < first_order - 1:
        return 2 * quotient * (quotient + 1)
    return 2 * quotient * (quotient + 1) + 1


def residue_counts():
    cases = 0
    for radius in range(1, 41):
        for first_order in range(3, 32, 2):
            counts = Counter((first % first_order, second % first_order)
                             for first in range(-radius, radius + 1)
                             for second in range(-radius + abs(first),
                                                 radius - abs(first) + 1))
            minimum = min(counts[(first, second)]
                          for first in range(first_order)
                          for second in range(first_order))
            assert minimum == odd_residue_bound(first_order, radius)
            cases += 1
    return {'s_range': [1, 40], 'odd_c_range': [3, 31],
            'diamond_residue_comparisons': cases}


def global_order_formula():
    rows = []
    for radius in range(2, 101):
        odd_number = 2 * radius + 1
        prime = next(value for value in range(2, odd_number + 1)
                     if odd_number % value == 0)
        predicted_order = (2 * radius * radius if prime == odd_number else
                           2 * radius * radius + 2 * radius - (prime * prime - 1) // 2)
        if radius == 2:
            predicted_order = 9
        bounds = [(2 * radius * radius // (first_order * first_order))
                  * first_order * first_order if first_order % 2 == 0 else
                  first_order * first_order * odd_residue_bound(first_order, radius)
                  for first_order in range(2, 2 * radius + 2)]
        assert max(bounds) == predicted_order
        if prime == odd_number and radius >= 3:
            first_order, second_order = radius, 2 * radius
            first, second = 1, second_order + 1
        elif radius == 2:
            first_order, second_order = 3, 3
            first, second = 1, second_order
        else:
            quotient = (odd_number // prime - 1) // 2
            first_order = prime
            second_order = 2 * prime * quotient * (quotient + 1)
            first, second = second_order + quotient, second_order + quotient + 1
        assert first_order * second_order == predicted_order
        moves = [divmod(first, second_order), divmod(second, second_order)]
        distances = {(0, 0): 0}
        queue = deque([(0, 0)])
        while queue:
            vertex = queue.popleft()
            for delta_first, delta_second in moves:
                for sign in [-1, 1]:
                    target = ((vertex[0] + sign * delta_first) % first_order,
                              (vertex[1] + sign * delta_second) % second_order)
                    if target not in distances:
                        distances[target] = distances[vertex] + 1
                        queue.append(target)
        assert len(distances) == predicted_order and max(distances.values()) <= radius
        rows.append({'s': radius, 'maximum_order': predicted_order,
                     'attaining_invariant_factors': [first_order, second_order],
                     'diameter': max(distances.values())})
    return {'s_range': [2, 100], 'formula_and_attaining_pair_comparisons': len(rows),
            'examples': rows}


def perfect_set_correction():
    radius, order = 2, 13
    chosen = {2, 10}
    values = [(first * 2 + second * 10) % order
              for first in range(-radius, radius + 1)
              for second in range(-radius + abs(first), radius - abs(first) + 1)]
    assert len(values) == len(set(values)) == order
    assert chosen == {(5 * 2) % order, (5 * 3) % order}
    assert all(chosen != {(multiplier * 2) % order, (multiplier * 3) % order}
               for multiplier in range(5))
    return {'s': radius, 'group_order': order, 'generators': sorted(chosen),
            'distinct_coefficient_images': len(set(values)),
            'corrected_unit_multiplier': 5, 'printed_domain_excluded': [0, 4]}


def small_noncyclic_groups():
    rows = []
    pair_count = 0
    for first_order in range(2, 8):
        for multiplier in range(1, 61 // (first_order * first_order) + 1):
            second_order = first_order * multiplier
            size = first_order * second_order
            tables = [tuple(((vertex // second_order + generator // second_order)
                             % first_order) * second_order
                            + (vertex % second_order + generator % second_order) % second_order
                            for vertex in range(size)) for generator in range(size)]
            inverses = [(-(generator // second_order) % first_order) * second_order
                        + (-(generator % second_order) % second_order)
                        for generator in range(size)]
            best = None
            for first, second in combinations(range(size), 2):
                pair_count += 1
                result = diameter([tables[first], tables[inverses[first]],
                                   tables[second], tables[inverses[second]]], size)
                if result is not None and (best is None or result < best):
                    best = result
            assert best is not None
            if first_order % 2:
                assert multiplier <= odd_residue_bound(first_order, best)
            rows.append({'c': first_order, 'k': multiplier, 'order': size,
                         'minimum_diameter': best})
    expected = {2: 9, 3: 18, 4: 36, 5: 50}
    observed = {radius: max(row['order'] for row in rows
                           if row['minimum_diameter'] <= radius)
                for radius in expected}
    assert observed == expected
    assert all(row['minimum_diameter'] > 1 for row in rows)
    return {'group_order_bound': 61, 's_range': [2, 5],
            'distinct_pairs': pair_count, 'groups': rows,
            'maximum_orders': observed}


def main():
    parser = argparse.ArgumentParser(description='Finite checks of signed two-generator diameters.')
    parser.add_argument('--max-k', type=int, default=40)
    parser.add_argument('--max-radius', type=int, default=12)
    parser.add_argument('--max-t', type=int, default=12)
    arguments = parser.parse_args()
    assert arguments.max_k >= 1 and arguments.max_radius >= 1 and arguments.max_t >= 1
    result = {'status': 'pass', 'scope': 'Finite checks of the stated parameter ranges.',
              'classification': exhaustive(arguments.max_k, arguments.max_radius),
              'sufficient_family': sufficient_families(arguments.max_t),
              'lower_range_formulas': lower_formulas(arguments.max_t),
              'even_invariant_factors': even_invariant_factors(),
              'odd_residue_counts': residue_counts(),
              'global_extremal_order': global_order_formula(),
              'perfect_set_domain_correction': perfect_set_correction(),
              'small_noncyclic_groups': small_noncyclic_groups()}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
