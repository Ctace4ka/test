import cv2

# Функция обработки событий мыши
def mouse_callback(event, x, y, flags, param):
    global drawing, top_left_pt, bottom_right_pt

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        top_left_pt = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        bottom_right_pt = (x, y)
        cv2.rectangle(image, top_left_pt, bottom_right_pt, (0, 255, 0), 2)
        cv2.imshow("photo_7_2024-02-02_17-00-23", image)

# Загрузка изображения
image = cv2.imread("photo_7_2024-02-02_17-00-23.jpg")

# Создание окна для отображения изображения
cv2.namedWindow("photo_7_2024-02-02_17-00-23")
cv2.imshow("photo_7_2024-02-02_17-00-23", image)

# Переменные для обработки событий мыши
drawing = False
top_left_pt, bottom_right_pt = (-1, -1), (-1, -1)

# Установка функции обработки событий мыши
cv2.setMouseCallback("photo_7_2024-02-02_17-00-23", mouse_callback)

# Бесконечный цикл для отображения изображения и ожидания событий
while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
