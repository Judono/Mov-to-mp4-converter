import sys
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QProgressBar
from moviepy.editor import VideoFileClip

class ConversionThread(QThread):
    progressChanged = pyqtSignal(int)
    conversionFinished = pyqtSignal()
    
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.mp4_path = file_path.replace(".mov", ".mp4")
        
    def run(self):
        clip = VideoFileClip(self.file_path)
        clip.write_videofile(self.mp4_path, progress_bar=lambda *args: self.update_progress(*args))
        clip.close()
        self.conversionFinished.emit()
    
    def update_progress(self, progress, *args):
        self.progressChanged.emit(int(progress * 100))

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
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 170, 400, 20)
        self.progress_bar.setVisible(False)
        
    def convert_video(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select MOV file", "", "MOV files (*.mov);;All Files (*)")
        if not file_path:
            return
        self.progress_bar.setValue(0)
        self.progress_bar.setVisible(True)
        self.conversion_thread = ConversionThread(file_path)
        self.conversion_thread.progressChanged.connect(self.update_progress)
        self.conversion_thread.conversionFinished.connect(self.conversion_finished)
        self.conversion_thread.start()
    
    def update_progress(self, progress):
        self.progress_bar.setValue(progress)
    
    def conversion_finished(self):
        self.status_label.setText("Conversion complete!")
        self.progress_bar.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 420, 220)
    window.show()
    sys.exit(app.exec())