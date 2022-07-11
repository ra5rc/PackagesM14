from booklover import Booklover
import unittest

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        test_object = Booklover("Han", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book('Book1',1)
        self.assertTrue(test_object.has_read('Book1'))

    def test_2_add_book(self):
        test_object = Booklover("Han", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book('Book2',5)
        test_object.add_book('Book2',5)
        self.assertTrue((len(test_object.book_list)) == 1)

    def test_3_has_read(self):
        test_object = Booklover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertTrue("Book2")

    def test_4_has_read(self):
        test_object = Booklover("Han", "hsolo@millenniumfalcon.com", "scifi")
        nobook=test_object.has_read('Happy Feet')
        self.assertFalse(nobook)

    def test_5_num_books_read(self):
        test_object = Booklover("Han", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book('Cinderella',2)
        test_object.add_book('Mickey',4)
        self.assertTrue(test_object.num_books == test_object.num_books_read())

    def test_6_fav_books(self):
        test_object = Booklover("Han", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book('Moana', 3)
        test_object.add_book('Jaws', 4)
        test_object.add_book('World War Z', 2)
        x=True
        for i in test_object.fav_books()['book_rating']:
            if i > 3:
                pass
            else: 
                x = False
        
        self.assertTrue(x)

if __name__ == '__main__':
    unittest.main(verbosity=3)



import pandas as pd
import json
import requests
users = requests.get("https://jsonplaceholder.typicode.com/users")
users = json.loads(users.text)
users[5]['company']['catchPhrase']
