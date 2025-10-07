import os

# Default downloads folder path
DOWNLOADS_FOLDER = os.path.expanduser("~/Downloads")

# File types mapping for organization
FILE_TYPES = {
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "archives": [".zip", ".tar", ".gz", ".rar"],
    "audio": [".mp3", ".wav", ".aac"],
    "video": [".mp4", ".mov", ".avi"],
}