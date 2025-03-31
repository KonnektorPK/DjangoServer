def getFrameRu(id):
    frame = int(id[6])
    frame_mapping_ru = {
        1: "Главный корпус",
        2: "Строительный корпус",
        3: "Архитектурный корпус",
        4: "Корпус на Егорова",
        5: "Пятый корпус",
        6: "Корпус на Серпуховской"
    }
    return frame_mapping_ru[frame]

def getFrameEn(id):
    frame_mapping_en = {
        1: "Main Building",
        2: "Construction Building",
        3: "Architectural Building",
        4: "Building on Egorova",
        5: "Fifth Building",
        6: "Building on Serpukhovskaya"
    }
    return frame_mapping_en[int(id[6])]