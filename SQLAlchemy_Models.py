import datetime
from typing import List
import sqlalchemy as sq
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Publisher(Base):
    __tablename__ = "publisher"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False, unique=True)

    books: Mapped["Book"] = relationship(back_populates="publishers")

    def __str__(self):
        return f'{self.id}: {self.name}'


class Book(Base):

    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    id_publisher = mapped_column(ForeignKey("publisher.id"))

    publishers: Mapped["Publisher"] = relationship(back_populates="books")

    stocks: Mapped[List["Stock"]] = relationship(back_populates="books")

    def __str__(self):
        return f'Книга {self.title} под номером {self.id}'


class Shop(Base):

    __tablename__ = "shop"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)

    stocks: Mapped[List["Stock"]] = relationship(back_populates="shops")

    def __str__(self):
        return f'Магазин {self.name} под номером {self.id}'


class Stock(Base):

    __tablename__ = "stock"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_book = mapped_column(ForeignKey("book.id"), nullable=False)
    id_shop = mapped_column(ForeignKey("shop.id"), nullable=False)
    count: Mapped[int]

    books: Mapped["Book"] = relationship(back_populates="stocks")
    shops: Mapped["Shop"] = relationship(back_populates="stocks")

    sales: Mapped[List["Sale"]] = relationship(back_populates="stocks")

    def __str__(self):
        return f'В магазине под номером {self.id_shop} ' \
               f'находится книга под номером {self.id_book} в количестве {self.count}'


class Sale(Base):

    __tablename__ = "sale"

    id: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(nullable=False)
    date_sale = mapped_column(Date)
    id_stock = mapped_column(ForeignKey("stock.id"), nullable=False)
    count: Mapped[int] = mapped_column(nullable=False)

    stocks: Mapped["Stock"] = relationship(back_populates="sales")

    def __str__(self):
        return f'{self.price}, {self.date_sale}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)