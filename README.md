# 📚 Ứng dụng Quản Lý Thư Viện bằng Python

## 🧾 Giới thiệu

Đây là một ứng dụng quản lý thư viện được xây dựng bằng ngôn ngữ Python theo mô hình lập trình hướng đối tượng (OOP), kết hợp với cơ sở dữ liệu MySQL. Chương trình hỗ trợ quản lý sách, thành viên và việc mượn/trả sách thông qua giao diện dòng lệnh.

---

## 🗃️ Cấu trúc cơ sở dữ liệu

### Bảng `books`
Lưu thông tin sách, gồm các cột:
- `book_id`, `title`, `author`, `pages`, `year_published`, `status`, `category`
- Các thuộc tính mở rộng:
  - `genre` (cho tiểu thuyết)
  - `subject`, `level` (cho giáo khoa)
  - `field` (cho khoa học)

### Bảng `members`
Lưu thông tin thành viên:
- `member_id`, `name`

### Bảng `borrowing`
Lưu thông tin mượn sách:
- `borrowing_id`, `member_id`, `book_id`, `borrow_date`, `due_date`, `return_date`

---

## 🧩 Các chức năng chính

- Thêm, sửa, xóa, tìm kiếm sách
- Thêm, sửa, xóa, tìm kiếm thành viên
- Mượn sách, trả sách
- Hiển thị danh sách sách đã mượn quá hạn

---

## 🗂️ Cấu trúc thư mục
library-management/
├── book.py          # Quản lý sách
├── member.py        # Quản lý thành viên 
├── borrowing.py     # Quản lý mượn/trả sách 
├── database.py      # Kết nối MySQL 
├── bailab2_2.py     # Giao diện dòng lệnh 
└── README.md

