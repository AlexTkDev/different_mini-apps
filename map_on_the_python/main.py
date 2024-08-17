import folium

# Координаты Центрального парка
central_park_location = [40.785091, -73.968285]

# Создаем карту с начальной точкой в Центральном парке
my_map = folium.Map(location=central_park_location, zoom_start=15, zoom_control=True)

# Добавляем красный круглый маркер для Центрального парка
central_park_marker = folium.CircleMarker(
    location=central_park_location,
    radius=5,
    color="red",
    fill=True,
    fill_color="red"
).add_to(my_map)

# Добавляем указатель на Центральный парк в виде маркера с popup-окном
central_park_popup_marker = folium.Marker(
    location=central_park_location,
    popup=folium.Popup('Central Park', max_width=200),
    icon=folium.Icon(color='red')
).add_to(my_map)


# Сохраняем карту в HTML файл
def main():
    my_map.save('map.html')


if __name__ == '__main__':
    main()
