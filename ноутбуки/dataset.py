import torch
from torch.utils.data import Dataset
import librosa

class MorseAudioDataset(Dataset):
    def __init__(self, paths, labels, sr=16000, transform=None):
        """
        paths  : список путей до аудио
        labels : список меток (классы: dot/dash/...)
        sr     : частота дискретизации
        transform : функция, которая преобразует raw-аудио в спектр
        """
        self.paths = paths
        self.labels = labels
        self.sr = sr
        self.transform = transform

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, idx):
        audio_path = self.paths[idx]
        y, _ = librosa.load(audio_path, sr=self.sr)

        # Преобразование аудио в спектр/признаки
        if self.transform is not None:
            features = self.transform(y)
        else:
            # По умолчанию просто raw
            features = y

        label = self.labels[idx]  # int (класс)

        # Превращаем features в тензор
        features = torch.tensor(features, dtype=torch.float)
        print("Label type:", type(label))

        return features, label
