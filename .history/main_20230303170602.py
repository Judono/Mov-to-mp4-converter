import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from moviepy.editor import VideoFileClip

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MOV to MP4 Converter")
        
        # Create the GUI widgets
        self.label = QLabel("Click 'Convert' to select a MOV file for conversion to MP4", self)
        self.label.setGeometry(10, 10, 400, 50)
        self.convert_btn = QPushButton("Convert", self)
        self.convert_btn.setGeometry(10, 70, 80, 30)
        self.convert_btn.clicked.connect(self.convert_video)
        self.status_label = QLabel("", self)
        self.status_label.setGeometry(10, 120, 400, 50)
        
    def convert_video(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select MOV file", "", "MOV files (*.mov);;All Files (*)")
        if not file_path:
            return
        clip = VideoFileClip(file_path)
        mp4_path = file_path.replace(".mov", ".mp4")
        clip.write_videofile(mp4_path)
        clip.close()
        self.status_label.setText("Conversion complete!")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 420, 180)
    window.show()
    sys.exit(app.exec())