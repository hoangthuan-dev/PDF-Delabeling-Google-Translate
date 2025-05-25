---
title: Xoá Nhãn Machine Translated by Google cho PDF
emoji: 🧹
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.31.0
app_file: app.py
pinned: false
---

# 🧹 Công Cụ Xoá Nhãn PDF: Loại Bỏ "Machine Translated by Google"

Đây là một công cụ web đơn giản nhưng hiệu quả, giúp loại bỏ dòng chữ **"Machine Translated by Google"** trong các file PDF được dịch tự động bằng Google Translate.

Ứng dụng được xây dựng bằng [Gradio](https://www.gradio.app/) và [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/), cho phép bạn xử lý tài liệu chỉ với vài cú nhấp chuột — không cần lập trình!

---

## ✨ Tính Năng

- ✅ Giao diện kéo thả dễ dàng để tải file PDF
- ✅ Tự động tìm và xoá dòng chữ: **"Machine Translated by Google"**
- ✅ Hiển thị bản PDF sau xử lý và cho phép tải về ngay
- ✅ Chạy trực tiếp trên trình duyệt (thông qua Hugging Face Spaces) — không cần cài đặt

---

## 📌 Trường Hợp Sử Dụng

Khi bạn sử dụng Google Translate để dịch file PDF, mỗi trang sẽ có thêm một dòng chữ:

```
Machine Translated by Google
```

Công cụ này sẽ giúp bạn xoá dòng chữ đó một cách gọn gàng, phục vụ cho:

- 📄 Tài liệu gửi khách hàng trông chuyên nghiệp hơn
- 🔒 Báo cáo nội bộ, tài liệu công ty rõ ràng hơn
- 📚 Dùng cho học thuật hoặc lưu trữ mà không có dấu vết dịch máy

---

## 🚀 Dùng Thử Trực Tuyến

👉 [Chạy ngay trên Hugging Face Spaces](https://huggingface.co/spaces/hoangthuandev/PDF-Delabeling-Google-Translate)  

---

## 🖥️ Cách Chạy Trên Máy Tính Cá Nhân

### 1. Clone dự án
```bash
git clone https://github.com/YOUR_USERNAME/pdf-label-remover.git
cd pdf-label-remover
```

### 2. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 3. Chạy ứng dụng
```bash
python app.py
```

Sau đó mở trình duyệt và truy cập [http://127.0.0.1:7860](http://127.0.0.1:7860)

---

## 📦 Cấu Trúc Dự Án

```
PDF-Delabeling-Google-Translate/
├── app.py               # Mã nguồn chính
├── requirements.txt     # Các thư viện cần thiết
└── README_vi.md         # File giới thiệu tiếng Việt
```

---

## 🛠️ Công Nghệ Sử Dụng

- [Gradio](https://gradio.app) — Tạo giao diện web đơn giản cho ứng dụng ML
- [PyMuPDF](https://pymupdf.readthedocs.io/) — Thư viện chỉnh sửa PDF bằng Python
- [Hugging Face Spaces](https://huggingface.co/spaces) — Nền tảng miễn phí để chạy ứng dụng AI và web

---

## 🤝 Giấy Phép

Dự án này sử dụng **MIT License**.  
Bạn có thể sử dụng, chỉnh sửa hoặc chia sẻ thoải mái!

---

## 👤 Tác Giả

**Hoàng Thuận DEV**
🌐 Website: [hoangthuan.dev](https://hoangthuan.dev)
📫 [Email hoặc GitHub](https://github.com/hoangthuan-dev)

---

## 💡 Đóng Góp

Mọi ý tưởng đóng góp, chỉnh sửa hoặc cải tiến tính năng đều được chào đón!  
Bạn có thể giúp cải thiện thuật toán nhận dạng nhãn hoặc hỗ trợ ngôn ngữ khác nếu muốn.

---

## ✅ Hướng dẫn chạy thử app Gradio trên máy cục bộ (localhost)

### 🧩 Bước 1: Cài đặt thư viện cần thiết

Mở terminal / CMD và chạy:

```bash
pip install gradio pymupdf
```

> Nếu bạn đang dùng môi trường như Anaconda, bạn có thể tạo 1 môi trường mới để test cho sạch:

```bash
conda create -n pdf-cleaner python=3.10
conda activate pdf-cleaner
pip install gradio pymupdf
```

---

### 🧩 Bước 2: Tạo file `app.py`

Copy đoạn code Gradio mình đã cung cấp ở trên vào một file tên là `app.py`.

---

### 🧩 Bước 3: Chạy ứng dụng

Trong thư mục chứa `app.py`, chạy:

```bash
python app.py
```

---

### 🧪 Kết quả:

* Bạn sẽ thấy dòng như:

  ```
  Running on local URL:  http://127.0.0.1:7860
  ```

* Mở trình duyệt và truy cập **[http://127.0.0.1:7860](http://127.0.0.1:7860)**

* Giao diện app sẽ hiển thị:

  * Kéo thả PDF
  * Nhấn nút “Xóa nhãn”
  * Tải file đã xử lý

---

## ❓Nếu bị lỗi khi chạy:

Gửi lỗi cho mình, mình sẽ hỗ trợ fix ngay. Một số lỗi có thể gặp:

* Không tìm thấy thư viện → chưa `pip install`
* Lỗi PDF → file gốc không hợp lệ
* Encoding / Unicode → fix trong xử lý `fitz`

---
