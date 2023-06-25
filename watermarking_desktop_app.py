from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import filedialog, Tk, Button, Entry, Label, StringVar, Toplevel


class WatermarkApp:
    def __init__(self):
        self.image_path = None
        self.image = None
        self.text = None
        self.logo_path = None
        self.preview_image = None
        self.preview_label = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename()

    def select_logo(self):
        self.logo_path = filedialog.askopenfilename()

    def update_preview(self):
        if self.image_path:
            self.preview_image = Image.open(self.image_path).convert("RGBA")
            width, height = self.preview_image.size
            draw = ImageDraw.Draw(self.preview_image)
            font_size = round(self.preview_image.width * 0.05)
            font = ImageFont.truetype("arial.ttf", font_size)
            if self.text:
                bbox = draw.textbbox((0, 0, width, height), self.text, font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                x = self.preview_image.width - text_width - round(self.preview_image.width * 0.05)
                y = self.preview_image.height - text_height - round(self.preview_image.height * 0.05)
                draw.text((x, y), self.text, font=font, fill=(255, 255, 255, 128))
            if self.logo_path:
                logo = Image.open(self.logo_path).convert("RGBA")
                logo_size = round(min(self.preview_image.width, self.preview_image.height) * 0.2)
                logo.thumbnail((logo_size, logo_size))
                x = round(self.preview_image.width * 0.05)
                y = round(self.preview_image.height * 0.05)
                self.preview_image.paste(logo, (x, y), logo)
            self.update_preview_label()

    def update_preview_label(self):
        if self.preview_image:
            photo = ImageTk.PhotoImage(self.preview_image)
            self.preview_label.configure(image=photo)
            self.preview_label.image = photo

    def save_watermarked_image(self):
        if self.image_path:
            image = Image.open(self.image_path).convert("RGBA")
            width, height = image.size
            draw = ImageDraw.Draw(image)
            font_size = round(image.width * 0.05)
            font = ImageFont.truetype("arial.ttf", font_size)
            if self.text:
                bbox = draw.textbbox((0, 0, width, height), self.text, font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                x = image.width - text_width - round(image.width * 0.05)
                y = image.height - text_height - round(image.height * 0.05)
                draw.text((x, y), self.text, font=font, fill=(255, 255, 255, 128))
            if self.logo_path:
                logo = Image.open(self.logo_path).convert("RGBA")
                logo_size = round(min(image.width, image.height) * 0.2)
                logo.thumbnail((logo_size, logo_size))
                x = round(image.width * 0.05)
                y = round(image.height * 0.05)
                image.paste(logo, (x, y), logo)
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                image.save(save_path)
                print("Watermark added successfully!")

    def create_gui(self):
        root = Tk()
        root.title("Watermark App")

        select_image_button = Button(root, text="Select Image", command=self.select_image)
        select_image_button.pack()

        select_logo_button = Button(root, text="Select Logo", command=self.select_logo)
        select_logo_button.pack()

        text_entry_label = Label(root, text="Watermark Text:")
        text_entry_label.pack()
        text_entry = Entry(root, textvariable=StringVar())
        text_entry.pack()

        def update_text():
            self.text = text_entry.get()

        update_text_button = Button(root, text="Update Text", command=update_text)
        update_text_button.pack()

        preview_window = Toplevel(root)
        preview_window.title("Preview")
        self.preview_label = Label(preview_window)
        self.preview_label.pack()

        update_preview_button = Button(root, text="Update Preview", command=self.update_preview)
        update_preview_button.pack()

        save_button = Button(root, text="Save Watermarked Image", command=self.save_watermarked_image)
        save_button.pack()

        root.mainloop()

    def run(self):
        self.create_gui()


if __name__ == "__main__":
    watermark_app = WatermarkApp()
    watermark_app.run()




