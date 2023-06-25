import sqlalchemy as sq
from sqlalchemy import create_engine
from sqlalchemy import String, func
from sqlalchemy.orm import sessionmaker, Session
from SQLAlchemy_Models import create_tables, Publisher, Book, Shop, Stock, Sale


engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/book_db")
create_tables(engine)


with Session(engine) as session:

    publisher_one = Publisher(id=1, name="Фёдор Достоевский")
    publisher_two = Publisher(id=2, name="Александр Пушкин")
    publisher_three = Publisher(id=3, name="Максим Горький")
    publisher_four = Publisher(id=4, name="Лев Толстой")
    publisher_five = Publisher(id=5, name="Корней Чуковский")

    book_dostoevsky_one = Book(id=1, title="Преступление и наказание", id_publisher=1)
    book_dostoevsky_two = Book(id=2, title="Идиот", id_publisher=1)
    book_dostoevsky_three = Book(id=3, title="Бесы", id_publisher=1)
    book_pushkin_one = Book(id=4, title="Капитанская дочка", id_publisher=2)
    book_pushkin_two = Book(id=5, title="Евгений Онегин", id_publisher=2)
    book_pushkin_three = Book(id=6, title="Дубровский", id_publisher=2)
    book_gorkiy_one = Book(id=7, title="Мать", id_publisher=3)
    book_gorkiy_two = Book(id=8, title="На дне", id_publisher=3)
    book_gorkiy_three = Book(id=9, title="Старик", id_publisher=3)
    book_tolstoy_one = Book(id=10, title="Война и мир", id_publisher=4)
    book_tolstoy_two = Book(id=11, title="Отрочество", id_publisher=4)
    book_tolstoy_three = Book(id=12, title="Казаки", id_publisher=4)
    book_chukovsky_one = Book(id=13, title="Мойдодыр", id_publisher=5)
    book_chukovsky_two = Book(id=14, title="Айболит", id_publisher=5)
    book_chukovsky_three = Book(id=15, title="Муха-цокотуха", id_publisher=5)

    shop_one = Shop(id=1, name="Читай город")
    shop_two = Shop(id=2, name="Литрес")
    shop_three = Shop(id=3, name="Дом книги")

    stock_one = Stock(id=1, id_book=1, id_shop=1, count=15)
    stock_two = Stock(id=2, id_book=1, id_shop=2, count=10)
    stock_three = Stock(id=3, id_book=1, id_shop=3, count=10)
    stock_four = Stock(id=4, id_book=2, id_shop=1, count=12)
    stock_five = Stock(id=5, id_book=2, id_shop=2, count=5)
    stock_six = Stock(id=6, id_book=2, id_shop=3, count=8)
    stock_seven = Stock(id=7, id_book=3, id_shop=2, count=20)
    stock_eight = Stock(id=8, id_book=4, id_shop=3, count=5)
    stock_nine = Stock(id=9, id_book=5, id_shop=1, count=20)
    stock_ten = Stock(id=10, id_book=5, id_shop=2, count=40)
    stock_eleven = Stock(id=11, id_book=6, id_shop=1, count=5)
    stock_twelve = Stock(id=12, id_book=6, id_shop=3, count=3)
    stock_thirteen = Stock(id=13, id_book=7, id_shop=2, count=5)
    stock_fourteen = Stock(id=14, id_book=8, id_shop=2, count=11)
    stock_fifteen = Stock(id=15, id_book=9, id_shop=1, count=7)
    stock_sixteen = Stock(id=16, id_book=9, id_shop=3, count=9)
    stock_seventeen = Stock(id=17, id_book=10, id_shop=1, count=25)
    stock_eighteen = Stock(id=18, id_book=10, id_shop=2, count=55)
    stock_nineteen = Stock(id=19, id_book=10, id_shop=3, count=15)
    stock_twenty = Stock(id=20, id_book=11, id_shop=3, count=6)
    stock_twenty_one = Stock(id=21, id_book=12, id_shop=1, count=13)
    stock_twenty_two = Stock(id=22, id_book=13, id_shop=1, count=3)
    stock_twenty_three = Stock(id=23, id_book=13, id_shop=2, count=23)
    stock_twenty_four = Stock(id=24, id_book=13, id_shop=3, count=7)
    stock_twenty_five = Stock(id=25, id_book=14, id_shop=1, count=4)
    stock_twenty_six = Stock(id=26, id_book=14, id_shop=2, count=30)
    stock_twenty_seven = Stock(id=27, id_book=15, id_shop=1, count=11)
    stock_twenty_eight = Stock(id=28, id_book=15, id_shop=2, count=14)
    stock_twenty_nine = Stock(id=29, id_book=15, id_shop=3, count=19)

    sale_one = Sale(price=397, date_sale='2022-01-18', id_stock=1, count=1)
    sale_two = Sale(price=276, date_sale='2022-01-22', id_stock=4, count=1)
    sale_three = Sale(price=542, date_sale='2022-02-02', id_stock=7, count=1)
    sale_four = Sale(price=733, date_sale='2022-02-09', id_stock=9, count=2)
    sale_five = Sale(price=700, date_sale='2022-02-19', id_stock=11, count=1)
    sale_six = Sale(price=612, date_sale='2022-02-19', id_stock=13, count=1)
    sale_seven = Sale(price=314, date_sale='2022-03-12', id_stock=14, count=1)
    sale_eight = Sale(price=118, date_sale='2022-03-16', id_stock=15, count=1)
    sale_nine = Sale(price=255, date_sale='2022-04-15', id_stock=17, count=1)
    sale_ten = Sale(price=1255, date_sale='2022-05-06', id_stock=19, count=2)
    sale_eleven = Sale(price=311, date_sale='2022-05-06', id_stock=20, count=1)
    sale_twelve = Sale(price=300, date_sale='2022-07-03', id_stock=21, count=5)
    sale_thirteen = Sale(price=180, date_sale='2022-07-27', id_stock=23, count=3)
    sale_fourteen = Sale(price=211, date_sale='2022-08-29', id_stock=26, count=10)
    sale_fifteen = Sale(price=145, date_sale='2022-09-05', id_stock=28, count=7)

    try:
        session.add_all([publisher_one, publisher_two, publisher_three, publisher_four, publisher_five])
        session.add_all(
            [book_dostoevsky_one, book_dostoevsky_two, book_dostoevsky_three, book_pushkin_one, book_pushkin_two,
             book_pushkin_three, book_gorkiy_one, book_gorkiy_two, book_gorkiy_three, book_tolstoy_one,
             book_tolstoy_two, book_tolstoy_three, book_chukovsky_one, book_chukovsky_two, book_chukovsky_three])
        session.add_all([shop_one, shop_two, shop_three])
        session.add_all(
            [stock_one, stock_two, stock_three, stock_four, stock_five, stock_six, stock_seven, stock_eight, stock_nine,
             stock_ten, stock_eleven, stock_twelve, stock_thirteen, stock_fourteen, stock_fifteen, stock_sixteen,
             stock_seventeen, stock_eighteen, stock_nineteen, stock_twenty, stock_twenty_one, stock_twenty_two,
             stock_twenty_three, stock_twenty_four, stock_twenty_five, stock_twenty_six, stock_twenty_seven,
             stock_twenty_eight, stock_twenty_nine])
        session.add_all(
            [sale_one, sale_two, sale_three, sale_four, sale_five, sale_six, sale_seven, sale_eight, sale_nine,
             sale_ten, sale_eleven, sale_twelve, sale_thirteen, sale_fourteen, sale_fifteen])

    except:
        session.rollback()
        print("Исправьте код")
    else:
        session.commit()

with Session(engine) as session:
    info_publisher = input("Введите ID или имя издателя:")

    query = session.query(Book.title, Shop.name, func.cast(Sale.price, String),
                          func.to_char(Sale.date_sale, 'DD-MM-YYYY')).select_from(Shop).join(Stock.shops).\
        join(Stock.books).join(Book.publishers).join(Sale)
    if info_publisher.isdigit():
        a = query.filter(Publisher.id == info_publisher).all()
        print(a)
    else:
        b = query.filter(Publisher.name == info_publisher).all()
        print(b)

