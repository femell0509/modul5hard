import time
from typing import List


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.users: List[User] = []
        self.videos: List[Video] = []
        self.current_user = None

    def log_in(self, nickname_search, password_search):
        for user in self.users:
            if user.nickname == nickname_search and hash(password_search) == user.password:
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *add_video):
        for i in add_video:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, scan_video):
        list_video = []
        for arhiv in self.videos:
            if scan_video.lower() in arhiv.title.lower():
                list_video.append(arhiv.title)
        return list_video

    def register(self, nick, passw, ag):
        for user in self.users:
            if user.nickname == nick:
                print(f'Пользователь {nick} уже зарегистрирован!')
                return None
        new_user = User(nick, passw, ag)
        self.users.append(new_user)
        self.log_in(nick, passw)

    def watch_video(self, video:str):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return None
        videos = []
        for i in self.videos:
            if i.title == video:
                videos.append(i)
        for i in videos:
            if i.adult_mode and self.current_user.age <= 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return None
            while i.time_now < i.duration:
                i.time_now += 1
                time.sleep(1)
                print(i.time_now)
            print('Конец видео!')
            i.time_now = 0





    def __str__(self):
        return self.videos


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

#Добавление видео
ur.add(v1, v2) # Как тут нам передавать не  v1.title, а v1 для этого мы в классе Video мы создали метод __repr__

print(ur.videos)


# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



