import unittest
from classes import Card, Bag
import functions as fn


def get_random_number(lst):
    for i in lst:
        if i != 0:
            rand_num = i
            break
    return rand_num


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card_human = Card('Human', False)

    def test_init(self):
        self.assertEqual(self.card_human.name, 'Human')
        self.assertFalse(self.card_human.is_comp)
        self.assertEqual(self.card_human.remaining_numbers, 15)
        self.assertTrue(self.card_human.is_in_game)
        self.assertEqual(len(self.card_human.card), 27)

    def test_set_is_comp(self):
        self.card_human.is_comp = True
        self.assertTrue(self.card_human.is_comp)
        self.card_human.is_comp = False

    def test_set_remaining_numbers(self):
        self.card_human.remaining_numbers = 14
        self.assertEqual(self.card_human.remaining_numbers, 14)

    def test_set_is_in_game(self):
        self.card_human.is_in_game = False
        self.assertFalse(self.card_human.is_in_game)
        self.card_human.is_in_game = True

    def test_set_card(self):
        gen_card = fn.generate_card()
        self.card_human.card = gen_card
        self.assertEqual(len(self.card_human.card), 27)
        # Проверяем исключение
        with self.assertRaises(Exception):
            self.card_human.card = [1, 2, 3]

    def test_print_card(self):
        rand_num = get_random_number(self.card_human.card)
        self.assertTrue(str(rand_num) in self.card_human.print_card())
        self.assertFalse(' - ' in self.card_human.print_card())

        self.card_human.remove_number(rand_num)
        self.assertTrue(' - ' in self.card_human.print_card())

    def test_remove_number(self):
        self.card_human.remove_number(91)
        self.assertEqual(len(self.card_human.card), 27)

        self.card_human.remove_number(get_random_number(self.card_human.card))
        self.assertEqual(len(self.card_human.card), 27)

    def test_check_answer(self):
        self.assertTrue(self.card_human.check_answer('y', get_random_number(self.card_human.card)))
        self.assertFalse(self.card_human.check_answer('y', 91))

        self.assertFalse(self.card_human.check_answer('n', get_random_number(self.card_human.card)))
        self.assertTrue(self.card_human.check_answer('n', 91))

    def test_str(self):
        self.assertTrue('Human' in str(self.card_human))

    def test_eq(self):
        card_comp = Card('Comp', False)
        self.assertTrue(self.card_human == card_comp)

    def test_contains(self):
        rand_num = get_random_number(self.card_human.card)
        self.assertTrue(rand_num in self.card_human)


class TestBag(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()

    def test_init(self):
        self.assertEqual(len(self.bag.set_numbers), 90)
        self.assertEqual(self.bag.remaining_numbers, 90)
        self.assertEqual(len(self.bag.dropped_numbers), 0)

    def test_set_remaining_numbers(self):
        self.bag.remaining_numbers = 14
        self.assertEqual(self.bag.remaining_numbers, 14)

    def test_get_number(self):
        num = self.bag.get_number()
        self.assertFalse(num in self.bag.set_numbers)

    def test_str(self):
        self.assertTrue('90' in str(self.bag))

    def test_eq(self):
        bag2 = Bag()
        self.assertTrue(self.bag == bag2)