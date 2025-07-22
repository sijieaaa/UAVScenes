'''
Note: 
These are "camera - LiDAR" calibrations from MARS-LVIG
These are not "camera - 3D map" calibrations, which are instead stored in .json files 
'''


# AMtown:
AMtown_calibration = {
    'camera_intrinsic': [1453.72, 0.0, 1172.18, 
                         0.0, 1453.28, 1041.78, 
                         0.0, 0.0, 1.0], 
    'camera_dist_coeffs': [-0.121, 0.1113, 0.0016, 0.00013, -0.062353], #k1, k2, p1, p2, k3
    'camera_ext_R': [0.00298088, -0.999728, -0.0231416, 
                     -0.00504636, 0.0231263, -0.99972, 
                     0.999983, 0.00309683, -0.00497605], 
    'camera_ext_t': [0.0025563, 0.0567484, -0.0512149]
}



# AMvalley:
AMvalley_calibration = {
    'camera_intrinsic': [1453.88, 0.0, 1182.53, 
                         0.0, 1452.85, 1045.82, 
                         0.0, 0.0, 1.0], 
    'camera_dist_coeffs': [-0.052, 0.1168, 0.0015, 0.00013, -0.068564], #k1, k2, p1, p2, k3
    'camera_ext_R': [0.00298068, -0.999735, -0.0231428, 
                     -0.00504595, 0.023132, -0.99974, 
                     0.999985, 0.00309701, -0.00497598], 
    'camera_ext_t': [-0.0025563, 0.0567484, -0.0512149]
}




# HKairport:
HKairport_calibration = {
    'camera_intrinsic': [1451.28, 0.0, 1177.5, 
                         0.0, 1451.29, 1043.5, 
                         0.0, 0.0, 1.0], 
    'camera_dist_coeffs': [-0.0572, 0.1209, 0.00124, -0.00018, -0.06327], #k1, k2, p1, p2, k3
    'camera_ext_R': [0.00322743, -0.999736, -0.022768, 
                     -0.0560389, 0.0227496, -0.999725, 
                     0.999979, 0.00335414, -0.00552898], 
    'camera_ext_t': [0.00242461, 0.0765454, -0.0313375]
}



# HKisland:
HKisland_calibration = {
    'camera_intrinsic': [1444.43, 0.0, 1177.8, 
                         0.0, 1444.34, 1043.6, 
                         0.0, 0.0, 1.0], 
    'camera_dist_coeffs': [-0.053, 0.121, 0.00127, 0.00043, -0.06495], #k1, k2, p1, p2, k3
    'camera_ext_R': [0.00352762, -0.999765, -0.0213775, 
                     -0.0111803, 0.0213369, -0.99971, 
                     0.999931, 0.00376561, -0.0111025], 
    'camera_ext_t': [-0.0025563, 0.0470454, -0.0513375]
}



# HK_GNSS:
HK_GNSS_calibration = {
    'camera_intrinsic': [1444.43, 0.0, 1179.50,
                        0.0,     1444.34,  1044.90,
                        0.0,     0.0,      1.0] ,
    'camera_dist_coeffs': [-0.0560, 0.1180, 0.00122, 0.00064, -0.0627], #k1, k2, p1, p2, k3
    'camera_ext_R': [0.00363212,-0.999819,-0.0213618,
                    -0.0111679,0.0214512,-0.999591,
                    0.999879,0.00375613,-0.0111134], 
    'camera_ext_t': [-0.0021928, 0.0470312, -0.0513126]
}



# Featureless_GNSS
Featureless_GNSS_calibration = {
    'camera_intrinsic': [1450.09, 0, 1177.5,
                        0.0,     1450.09, 1044.5,
                        0.0,     0.0,      1.0] ,
    'camera_dist_coeffs': [-0.0558, 0.1247, 0.00126, 0.0007, -0.06762], #k1, k2, p1, p2, k3
    'camera_ext_R': [0.00941312,-0.999586,-0.0271775,
                    -0.00737429,0.0271086,-0.999605,
                    0.999929,0.00960988,-0.00711613], 
    'camera_ext_t': [-0.0025563, 0.0567484, -0.0512149]
}


# AMtown010203 -> AMtown_calibration
# AMvalley010203 -> AMvalley_calibration
# HKairport010203 -> HK_GNSS_calibration
# HKisland010203 -> HKisland_calibration
# HKairport_GNSS_Evening -> HK_GNSS_calibration
# HKisland_GNSS_Evening -> Featureless_GNSS_calibration
# HKairport_GNSS010203 -> HK_GNSS_calibration
# HKisland_GNSS010203 -> HK_GNSS_calibration
# Featureless_GNSS010203 -> Featureless_GNSS_calibration

scenename_to_calibration = {
    'AMtown01': AMtown_calibration,
    'AMtown02': AMtown_calibration,
    'AMtown03': AMtown_calibration,
    'AMvalley01': AMvalley_calibration,
    'AMvalley02': AMvalley_calibration,
    'AMvalley03': AMvalley_calibration,
    'HKairport01': HK_GNSS_calibration,
    'HKairport02': HK_GNSS_calibration,
    'HKairport03': HK_GNSS_calibration,
    'HKisland01': HKisland_calibration,
    'HKisland02': HKisland_calibration,
    'HKisland03': HKisland_calibration,
    'HKairport_GNSS_Evening': HK_GNSS_calibration,
    'HKisland_GNSS_Evening': Featureless_GNSS_calibration,
    'HKairport_GNSS01': HK_GNSS_calibration,
    'HKairport_GNSS02': HK_GNSS_calibration,
    'HKairport_GNSS03': HK_GNSS_calibration,
    'HKisland_GNSS01': HK_GNSS_calibration,
    'HKisland_GNSS02': HK_GNSS_calibration,
    'HKisland_GNSS03': HK_GNSS_calibration,
    'Featureless_GNSS01': Featureless_GNSS_calibration,
    'Featureless_GNSS02': Featureless_GNSS_calibration,
    'Featureless_GNSS03': Featureless_GNSS_calibration
}
