from application import app, detail_book, delete_book
from application import db
from sqlalchemy import or_
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from .models import Book
from .forms CreateBookForm, UptadeBookForm, DeleteBookForm


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/books/list')
def list_books():
    return render_template('books/list.html', books=books)


@app.route('/books/detail/<int:book_id>')
def detail_book(book_id):
    book = Book.query.filter_by(id=book_id).first()

    return render_template('books/detail.html', book=book)


@app.route('/books/create', methods=('GET', 'POST'))
def create_book():
    form = CreateBookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('list_books'))

    return render_template('books/create.html', form=form)


@app.route('/books/update/<int:book_id>', methods=('GET', 'POST'))
def edit_book(book_id):
    book = Book.query.get(book_id)
    form = UptadeBookForm()

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        return redirect(url_for('list_books'))
    elif request.method == 'GET':
        form.title
    return render_template('books/edit.html', book=book)


@app.route('/books/delete/<int:book_id>', methods=('GET', 'POST'))
def delete_book(book_id):
    book = Book.query.get(book_id)
    form = DeleteBookForm()
    if form.validate_on_submit():
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('list_books'))

    return render_template('books/delete.html', book=book, form=form)