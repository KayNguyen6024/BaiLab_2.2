-- Active: 1761805215250@@127.0.0.1@3306@library


-- Tạo cơ sở dữ liệu
CREATE DATABASE Library;

-- Sử dụng cơ sở dữ liệu Library
USE Library;

-- Bảng sách
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    pages INT NOT NULL,
    year_published INT NOT NULL,
    status INT NOT NULL, -- 0: có sẵn, 1: đã mượn, 2: trạng thái khác
    category VARCHAR(255) NOT NULL -- Cho phép nhập tự do loại sách
);
SELECT * FROM books;
ALTER TABLE books
ADD genre VARCHAR(255),
ADD subject VARCHAR(255), 
ADD level VARCHAR(255),
ADD field VARCHAR(255);

-- Bảng thành viên
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
SELECT * FROM members;
-- Bảng mượn sách
CREATE TABLE borrowing (
    borrowing_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    book_id INT NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
SELECT * FROM borrowing;
