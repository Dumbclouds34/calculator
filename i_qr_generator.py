import qrcode
from tkinter import Tk, colorchooser, filedialog
from PIL import Image

class QRCodeGenerator:
    def __init__(self):
        # Initialize tkinter root (hidden as no GUI is displayed)
        self.root = Tk()
        self.root.withdraw()
    
    def prompt_data(self):
        # Prompt user to enter data to encode
        self.data = input("Enter the data to convert to QR code: ")

    def prompt_save_path(self):
        # Prompt user to choose the save path and file name
        print("Please select the folder where you want to save the QR code.")
        self.save_path = filedialog.askdirectory(title="Select folder to save QR code")
        self.file_name = input("Enter the name to save the QR code image (without extension): ")

    def prompt_colors(self):
        # Prompt user to pick colors for background and fill
        print("Select the background color:")
        self.bg_color = colorchooser.askcolor(title="Choose Background Color")[1]
        print("Select the fill color:")
        self.fill_color = colorchooser.askcolor(title="Choose Fill Color")[1]
    
    def generate_qr_code(self):
        # Generate the QR code with the specified settings
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=self.fill_color, back_color=self.bg_color)
        
        # Save the generated QR code to the specified path
        save_location = f"{self.save_path}/{self.file_name}.png"
        img.save(save_location)
        
        print("Success! You can check your folder for the image.")

    def run(self):
        # Run all prompts and generate the QR code
        self.prompt_data()
        self.prompt_save_path()
        self.prompt_colors()
        self.generate_qr_code()

# Instantiate and run the QRCodeGenerator
qr_code_gen = QRCodeGenerator()
qr_code_gen.run()
