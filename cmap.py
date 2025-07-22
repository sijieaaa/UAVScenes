cmap = {
    0: {'name': 'background', 'RGB': [0, 0, 0]},
    1: {'name': 'roof', 'RGB': [119, 11, 32]},  
    2: {'name': 'dirt_motor_road', 'RGB': [180, 165, 180]},  
    3: {'name': 'paved_motor_road', 'RGB': [128, 64, 128]},  
    4: {'name': 'river', 'RGB': [173, 216, 230]},  
    5: {'name': 'pool', 'RGB': [0, 80, 100]},  
    6: {'name': 'bridge', 'RGB': [150, 100, 100]},  
    7: {'name': '', 'RGB': [150, 120, 90]}, 
    8: {'name': '', 'RGB': [70, 70, 70]},  
    9: {'name': 'container', 'RGB': [250, 170, 30]},  
    10: {'name': 'airstrip', 'RGB': [81, 0, 81]},  
    11: {'name': 'traffic_barrier', 'RGB': [102, 102, 156]},  
    12: {'name': '', 'RGB': [190, 153, 153]},  
    13: {'name': 'green_field', 'RGB': [107, 142, 35]},  
    14: {'name': 'wild_field', 'RGB': [210, 180, 140]},  
    15: {'name': 'solar_board', 'RGB': [220, 220, 0]},  
    16: {'name': 'umbrella', 'RGB': [153, 153, 153]},  
    17: {'name': 'transparent_roof', 'RGB': [0, 0, 90]},  
    18: {'name': 'car_park', 'RGB': [250, 170, 160]},  
    19: {'name': 'paved_walk', 'RGB': [244, 35, 232]},  
    20: {'name': 'sedan', 'RGB': [0, 0, 142]},  
    21: {'name': '', 'RGB': [224, 224, 192]},
    22: {'name': '', 'RGB': [220, 20, 60]},  
    23: {'name': '', 'RGB': [192, 64, 128]},
    24: {'name': 'truck', 'RGB': [0, 0, 70]},  
    25: {'name': '', 'RGB': [0, 60, 100]}  
}


if __name__ == '__main__':

    import numpy as np
        
    id2rgb = [v['RGB'] for k,v in cmap.items()]
    id2rgb = np.array(id2rgb)
    print(id2rgb)

    rgb2id = {}
    for k,v in cmap.items():
        rgb2id[tuple(v['RGB'])] = k
    print(rgb2id)

    print(set(cmap.keys()) )
    print(len(set(cmap.keys())) )   

