class Book:
    book_count = 0

    def __init__(self, title, author, genre, publication_year, price, availability=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.__price = price
        self.__availability = availability

        Book.book_count += 1

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def is_available(self):
        return self.__availability

    def set_available(self, is_available):
        self.__availability = is_available

    def display_details(self):
        availability_of_book = "Available" if self.is_available() else "Unavailable"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Price: ${self.get_price():.2f}")
        print(f"Availability: {availability_of_book}")

    def apply_discount(self, discount):
        if 0 < discount < 100:
            discounted_price = self.__price * (1 - discount / 100)
            self.set_price(discounted_price)

    def mark_unavailable(self):
        self.set_available(False)

    @classmethod
    def get_book_count(cls):
        return cls.book_count


book1 = Book("Tanbehul G'ofilin", "Samarqandy", "Science fiction", 833, 20.03)

book1.display_details()
book1.apply_discount(10)


book1.display_details()

print("Total books created:", Book.get_book_count())
#C:\Users\designer\Documents\bookclass.py