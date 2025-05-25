import fitz  # PyMuPDF
import gradio as gr
import os
import tempfile

def remove_google_label(pdf_file):
    # pdf_file là đường dẫn đến file tạm thời
    input_path = pdf_file
    temp_dir = tempfile.mkdtemp()
    output_path = os.path.join(temp_dir, "cleaned_output.pdf")

    doc = fitz.open(input_path)
    
    for page in doc:
        text_instances = page.search_for("Machine Translated by Google")
        for inst in text_instances:
            page.draw_rect(inst, color=(1, 1, 1), fill=(1, 1, 1))  # Xóa nhãn
    
    doc.save(output_path)
    doc.close()
    
    return output_path

# Giao diện Gradio
with gr.Blocks(title="Xóa nhãn 'Machine Translated by Google'") as demo:
    gr.Markdown("### 🧹 Xóa nhãn 'Machine Translated by Google' trong file PDF dịch tự động")
    gr.Markdown("Thả file PDF vào bên trái, nhấn nút xử lý, và tải file kết quả ở bên phải.")

    with gr.Row():
        pdf_input = gr.File(label="📤 File PDF cần xử lý", file_types=[".pdf"])
        pdf_output = gr.File(label="📥 File PDF đã xử lý", interactive=False)

    process_button = gr.Button("🪄 Xóa nhãn")

    process_button.click(fn=remove_google_label, inputs=pdf_input, outputs=pdf_output)

demo.launch()
