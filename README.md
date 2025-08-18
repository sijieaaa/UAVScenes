

# UAVScenes 
(ICCV 2025) UAVScenes: A Multi-Modal Dataset for UAVs

[[arXiv]](http://arxiv.org/abs/2507.22412)  [ICCV 2025]

We introduce UAVScenes, a large-scale dataset designed to benchmark various tasks across both 2D and 3D modalities. Our benchmark dataset is built upon the well-calibrated multi-modal UAV dataset MARS-LVIG, originally developed only for simultaneous localization and mapping (SLAM). We enhance this dataset by providing manually labeled semantic annotations for both images and LiDAR point clouds, along with accurate 6-degree-of-freedom (6-DoF) poses. These additions enable a wide range of UAV perception tasks, including detection, segmentation, depth estimation, 6-DoF localization, place recognition, and novel view synthesis (NVS). To the best of our knowledge, this is the first UAV benchmark dataset to offer both image and LiDAR point cloud semantic annotations (120k labeled pairs), with the potential to advance multi-modal UAV perception research. 

<img src="https://github.com/sijieaaa/UAVScenes/raw/main/pics/supp_demo.png"  alt="pic" style="width:80%; height:auto;">

## Download
We provide both the full dataset (interval=1) and the key-frame only dataset (interval=5, 1/5 size). <br>
UAVScenes has been uploaded onto various cloud platforms.
- [OneDrive](https://entuedu-my.sharepoint.com/:f:/g/personal/wang1679_e_ntu_edu_sg/EgY6DU5GBchIiAIa-eQZmEAB0vJx3khCPHbFW3LnR77RFw?e=26GaSc)
- [Google Drive](https://drive.google.com/drive/folders/1HSJWc5qmIKLdpaS8w8pqrWch4F9MHIeN?usp=sharing)
- [Baidu/百度网盘](https://pan.baidu.com/s/13CgnxRFqevQ8Fa1Y3dkM0A?pwd=1679) (interval=5 only)
- [HuggingFace](https://huggingface.co/datasets/sijieaaa/UAVScenes) (interval=5 only)

⚠️ If you face any download problems, kindly please raise an [issue](https://github.com/sijieaaa/UAVScenes/issues/new) with screenshots. We will fix them ASAP🙂.

We currently include:
- Hikvision camera images with annotations
- Livox Avia LiDAR point clouds with annotations
- 6-DoF poses
- Reconstructed 3D point cloud/mesh maps 

## File Information
`cmap.py` contains color-ID mapping. <br>
`calibration_results.py` contains camera-LiDAR calibrations. <br>
`sampleinfos_interpolated.json` contains camera-3D map calibrations. <br>

`terra_ply/` contains the raw mesh map outputs from Terra, which contains multiple mesh blocks. <br>
`cloud_merged.ply` contains the raw point cloud map outputs from Terra. <br>
`Mesh.ply` is built by merging all mesh blocks from `terra_ply/` together. <br>


## Dataset Overview
- UAVScenes is built based on [MARS-LVIG](https://mars.hku.hk/dataset.html). Thanks for their excellent work.

- We use [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling) for 2D annotating, [CloudCompare](https://www.danielgm.net/cc/) for 3D annotating, and [DJI Terra (大疆智图)](https://enterprise.dji.com/dji-terra) for 3D reconstruction (much more accurate than COLMAP).

- More sensor and scene information can be found from [MARS-LVIG](https://mars.hku.hk/dataset.html).

<img src="https://github.com/sijieaaa/UAVScenes/raw/main/pics/dji_m300.png"  alt="pic" style="width:50%; height:auto;">

- UAVScenes consists of 4 large scenes (AMtown, AMvalley, HKairport, and HKisland). Each scene consists of multiple runs (e.g., 01, 02, and 03).

<img src="https://github.com/sijieaaa/UAVScenes/raw/main/pics/summary.png"  alt="pic" style="width:80%; height:auto;">


## Baseline Code
Under preparing. Please stay tuned.

## Citation
```
@article{wang2025uavscenes,
  title={UAVScenes: A Multi-Modal Dataset for UAVs},
  author={Wang, Sijie and Li, Siqi and Zhang, Yawei and Yu, Shangshu and Yuan, Shenghai and She, Rui and Guo, Quanjiang and Zheng, JinXuan and Howe, Ong Kang and Chandra, Leonrich and others},
  journal={arXiv preprint arXiv:2507.22412},
  year={2025}
}
```

## License
This work is available under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/) and is meant for academic use only. 
