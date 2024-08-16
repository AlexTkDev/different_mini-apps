import folium

map_center = [45.5236, -122.6750]
my_map = folium.Map(location=map_center, zoom_start=15, zoom_control=True)

folium.Marker(
    location=map_center,
    icon=folium.Icon(color='blue', icon='map'),
    popup=folium.Popup("Let's try quotes", parse_html=True, max_width=100),
).add_to(my_map)


# Отображаем карту
def main():
    my_map.save('map.html')


if __name__ == '__main__':
    main()
