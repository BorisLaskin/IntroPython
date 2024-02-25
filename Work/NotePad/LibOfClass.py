from dataclasses import dataclass
from datetime import datetime


# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок.

# Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки.

# Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента
@dataclass
class SingleNote:
    id_note: int
    title: str
    text: str
    date_note: datetime

    def __init__(self, id_note: int, title: str, text: str, date_note=datetime.now()):
        self.idNote = id_note
        self.title = title
        self.text = text
        self.date_note = date_note

    def __str__(self):
        return str(self.id_note) + "\\s" + self.title + ":" + self.text + "\\s" + str(self.date_note)


@dataclass
class NotePad:
    __data: dict[int, SingleNote]
    __last_note = 0

    def add_new_note(self, title: str, text: str):
        self.__last_note += 1
        temp_node = SingleNote(id_note=self.__last_note, title=title, text=text)
        self.__data[temp_node.id_note] = temp_node

    def count_notes(self):
        return len(self.__data.keys())

    def delete_note(self, id_note):
        del self.__data[id_note]

    def pop_note(self, id_note):
        temp = self.__data[id_note]
        self.delete_note(id_note)
        return temp

    def read_note(self, id_note):
        return str(self.__data[id_note])

    def correct_note_text(self, id_note, text):
        self.__data[id_note].text = text

    def correct_note_title(self, id_note, title):
        self.__data[id_note].title = title
