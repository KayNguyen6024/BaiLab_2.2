from database import Database
from book import Book
from member import Member
from borrowing import Borrowing
from datetime import datetime, timedelta

def main():
    db = Database()
    
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ THƯ VIỆN ---")
        print("1. Thêm sách")
        print("2. Sửa thông tin sách")
        print("3. Tìm kiếm sách")
        print("4. Hiển thị danh sách sách")
        print("5. Thêm thành viên")
        print("6. Tìm kiếm thành viên")
        print("7. Mượn sách")
        print("8. Trả sách")
        print("9. Hiển thị sách đã mượn quá hạn")
        print("10. Thoát")

        choice = input("Chọn chức năng: ")
        
        if choice == "1":
            title = input("Nhập tên sách: ")
            author = input("Nhập tác giả: ")
            pages = int(input("Nhập số trang: "))
            year_published = int(input("Nhập năm xuất bản: "))
            status = int(input("Nhập trạng thái sách (0: có sẵn, 1: đã mượn): "))
            category = input("Nhập chủng loại sách (Tiểu thuyết, Giáo khoa, Khoa học): ").strip().lower()

            # Khởi tạo các thuộc tính mở rộng
            genre = subject = level = field = None

            if category == "tiểu thuyết":
                genre = input("Nhập thể loại tiểu thuyết (lãng mạn, kinh dị, viễn tưởng...): ")
                category = "Tiểu thuyết"

            elif category == "giáo khoa":
                subject = input("Nhập môn học (Toán, Văn, Anh...): ")
                level = input("Nhập cấp độ (Tiểu học, THCS, THPT): ")
                category = "Giáo khoa"

            elif category == "khoa học":
                field = input("Nhập lĩnh vực khoa học (CNTT, Điện tử, Cơ khí...): ")
                category = "Khoa học"

            else:
                print("Chủng loại sách không hợp lệ. Sách sẽ được lưu với loại 'Khác'.")
                category = "Khác"
            book = Book(None, title, author, pages, year_published, status, category, genre, subject, level, field)
            book.add_book(db)

        elif choice == "2":
            book_id = int(input("Nhập ID sách: "))
            book = Book.search_book(db, book_id)
            if book:
                title = input("Nhập tên mới: ")
                author = input("Nhập tác giả mới: ")
                pages = int(input("Nhập số trang mới: "))
                year_published = int(input("Nhập năm xuất bản mới: "))
                status = int(input("Nhập trạng thái mới: "))
                category = input("Nhập chủng loại sách mới (Tiểu thuyết, Giáo khoa, Khoa học): ").strip().lower()
                genre = subject = level = field = None
                if category == "tiểu thuyết":
                    genre = input("Nhập thể loại tiểu thuyết mới(lãng mạn, kinh dị, viễn tưởng...): ")
                    category = "Tiểu thuyết"

                elif category == "giáo khoa":
                    subject = input("Nhập môn học mới (Toán, Văn, Anh...): ")
                    level = input("Nhập cấp độ mới (Tiểu học, THCS, THPT): ")
                    category = "Giáo khoa"

                elif category == "khoa học":
                    field = input("Nhập lĩnh vực khoa học mới (CNTT, Điện tử, Cơ khí...): ")
                    category = "Khoa học"
                else:
                    print("Chủng loại sách không hợp lệ. Sách sẽ được lưu với loại 'Khác'.")
                    category = "Khác"
                updated_book = Book(book_id, title, author, pages, year_published, status, category, genre, subject, level, field)
                updated_book.update_book(db)
            else:
                print("Sách không tồn tại.")
                


        elif choice == "3":
            book_id = int(input("Nhập ID sách cần tìm: "))
            book = Book.search_book(db, book_id)
            if book:
                print(book)
            else:
                print("Sách không tồn tại.")

        elif choice == "4":
            books = Book.get_all_books(db)
            if books:
                print("\nDanh sách sách:")
                for book in books:
                    print(book)
            else:
                print("Không có sách nào trong thư viện.")

        elif choice == "5":  # Thêm thành viên
            name = input("Nhập tên thành viên: ")
            member = Member(None, name)
            member.add_member(db)
            
        
        elif choice == "6":  # Tìm kiếm thành viên
            member_id = int(input("Nhập ID thành viên cần tìm: "))
            member = Member.search_member(db, member_id)
            if member:
                print(f"ID: {member_id}, Tên: {member.name}")
            else:
                print("Thành viên không tồn tại.")

        elif choice == "7":  # Mượn sách
            member_id = input("Nhập ID thành viên: ")
            title = input("Nhập tên sách cần mượn: ")
            book = Book.search_book_by_title(db, title)  # Tìm sách theo tên
            if book:
                borrow_date = datetime.today().strftime('%Y-%m-%d')
                
                # Tính ngày trả sách (14 ngày sau ngày mượn)
                return_date = (datetime.today() + timedelta(days=14)).strftime('%Y-%m-%d')
                
                borrowing = Borrowing(None,member_id, book.book_id, borrow_date, return_date)
                borrowing.borrow_book(db)
                print(f"Sách '{title}' đã được mượn thành công. Ngày trả sách là {return_date}.")
            else:
                print(f"Sách '{title}' không tồn tại trong thư viện.")

        elif choice == "8":  # Trả sách
            member_id = input("Nhập ID thành viên: ")
            title = input("Nhập tên sách cần trả: ")
            book = Book.search_book_by_title(db, title)

            if book:
                # Kiểm tra xem sách có đang được mượn bởi thành viên này không
                query = """
                    SELECT * FROM borrowing 
                    WHERE member_id = %s AND book_id = %s AND return_date IS NULL
                """
                borrowing_record = db.fetch_one(query, (member_id, book.book_id))

                if borrowing_record:
                    return_date = datetime.today().strftime('%Y-%m-%d')

                    # Cập nhật ngày trả sách
                    update_query = """
                        UPDATE borrowing 
                        SET return_date = %s 
                        WHERE member_id = %s AND book_id = %s AND return_date IS NULL
                    """
                    db.execute_query(update_query, (return_date, member_id, book.book_id))

                    # Cập nhật trạng thái sách về "có sẵn"
                    db.execute_query("UPDATE books SET status = 0 WHERE book_id = %s", (book.book_id,))
                    print(f"Đã trả sách '{title}' thành công vào ngày {return_date}.")
                else:
                    print("Không tìm thấy thông tin mượn sách này.")
            else:
                print("Sách không tồn tại.")

        elif choice == "9":  # Hiển thị sách đã mượn quá hạn
            today = datetime.today().date()

            query = """
                SELECT b.title, m.name, br.borrow_date 
                FROM borrowing br
                JOIN books b ON br.book_id = b.book_id
                JOIN members m ON br.member_id = m.member_id
                WHERE br.return_date IS NULL AND br.borrow_date < %s
            """
            overdue_date = today - timedelta(days=14)
            overdue_books = db.fetch_all(query, (overdue_date,))

            if overdue_books:
                print("\n Danh sách sách đã mượn quá hạn:")
                for title, member_name, borrow_date in overdue_books:
                    print(f"- '{title}' mượn bởi {member_name} từ ngày {borrow_date}")
            else:
                print("Không có sách nào quá hạn.")

        elif choice == "10":  # Thoát
            print("Cảm ơn bạn đã sử dụng hệ thống.")
            break


if __name__ == "__main__":
    main()
