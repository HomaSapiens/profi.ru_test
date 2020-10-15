from typing import List, Dict
import unittest


# space/time complexity - O(N)
def remove_list_duplicates(l: List) -> List:
    hash_map: Dict = dict()
    result: List = []

    for elem in l:
        if elem not in hash_map.keys():
            hash_map[elem] = 1
            result.append(elem)
    return result


class TestStringMethods(unittest.TestCase):
    def test_remove_list_duplicates(self):
        empty_list = []
        one_elem = [42]
        two_elem_diff = [42, 2]
        two_elem_eq = [42, 42]
        complex_list = [1, 3, 2, 1, 5, 3, 5, 1, 4]
        diff_types = [1, 2, 'test', 'test', 2, 3, 'test', 5, 8.0, (1, 2), (1, 2)]

        self.assertEqual(remove_list_duplicates(empty_list), [])
        self.assertEqual(remove_list_duplicates(one_elem), [42])
        self.assertEqual(remove_list_duplicates(two_elem_diff), [42, 2])
        self.assertEqual(remove_list_duplicates(two_elem_eq), [42])
        self.assertEqual(remove_list_duplicates(complex_list), [1, 3, 2, 5, 4])
        self.assertEqual(remove_list_duplicates(diff_types), [1, 2, 'test', 3, 5, 8.0, (1, 2)])


if __name__=="__main__":

    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    example_list_1 = [1, 2, 3, 1]
    example_list_2 = [1, 3, 2, 1, 5, 3, 5, 1, 4]

    print(f'{example_list_1} -> {remove_list_duplicates(example_list_1)}')
    print(f'{example_list_2} -> {remove_list_duplicates(example_list_2)}')
