# FINAL PROJECT TITLE HERE

## Project Description
Please describe your Startup Campus final project here. You may should your <b>model architecture</b> in JPEG or GIF.

## Contributor
| Full Name | Affiliation | Email | LinkedIn | Role |
| --- | --- | --- | --- | --- |
| Marsyanda Salsa Nabila | Startup Campus, AI Track | marsyandasalsa2021@gmail.com  | [link](https://www.linkedin.com/in/marsyandasalsanabila/) | Team Lead |
| Ilham Khefi Ramadhanu | Startup Campus, AI Track | ilhamramadhanu25@gmail.com | [link](https://www.linkedin.com/in/ilham-khefi-ramadhanu) | Team Member |
| Mochamad Freski Dino Fava | Startup Campus, AI Track | ... | ... | Team Member |
| Shafa Anisya Aji Divana | Startup Campus, AI Track | ... | ... | Team Member |
| Nisrina Alifa Adzahra | Startup Campus, AI Track | nisrinalifa@gmail.com | [link](https://www.linkedin.com/in/nisrina-alifa-adzahra/) | Team Member |
| Cijo Jidan Riady | Startup Campus, AI Track | ... | ... | Team Member |
| Ghea Dwi Apriliana | Startup Campus, AI Track | ... | ... | Team Member |
| Nicholas Dominic | Startup Campus, AI Track | nic.dominic@icloud.com | [link](https://linkedin.com/in/nicholas-dominic) | Supervisor |

## Setup
### Prerequisite Packages (Dependencies)
- pandas==2.1.0
- openai==0.28.0
- google-cloud-aiplatform==1.34.0
- google-cloud-bigquery==3.12.0
- ...
- ...

### Environment
| | |
| --- | --- |
| CPU | Example: Apple M3 Pro 12-core CPU |
| GPU | Example: Nvidia T4 (x1) |
| ROM | Example: 1 TB SSD |
| RAM | Example: 36 GB |
| OS | Example: macOS Sonoma v14.1.1 |

## Dataset
Describe your dataset information here. Provide a screenshot for some of your dataset samples (for example, if you're using CIFAR10 dataset, then show an image for each class).

Dataset "Jalan Rusak" dirancang untuk mendeteksi kerusakan jalan menggunakan teknik computer vision. Dataset ini terdiri dari gambar-gambar yang telah dianotasi dengan label yang merepresentasikan berbagai jenis kerusakan jalan.
- Link: https://universe.roboflow.com/tugas-xogo7/jalanrusak-zofhk

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
Inform your model validation performances, as follows:
- For classification tasks, use **Precision and Recall**.
- For object detection tasks, use **Precision and Recall**. Additionaly, you may also use **Intersection over Union (IoU)**.
- For image retrieval tasks, use **Precision and Recall**.
- For optical character recognition (OCR) tasks, use **Word Error Rate (WER) and Character Error Rate (CER)**.
- For adversarial-based generative tasks, use **Peak Signal-to-Noise Ratio (PNSR)**. Additionally, for specific GAN tasks,
  - For single-image super resolution (SISR) tasks, use **Structural Similarity Index Measure (SSIM)**.
  - For conditional image-to-image translation tasks (e.g., Pix2Pix), use **Inception Score**.

Feel free to adjust the columns in the table below.

| model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall | mAP50 | mAP 50-95 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLOv8s | 50 | 0.001 | 32 | AdamW | ... | ... | ... | 0.942 | 0.7 |
| YOLOv8s | 50 | 0.001 | 16 | AdamW | ... | ... | ... | 0.943 | 0.698 |
| YOLOv8n | 50 | 0.001 | 32 | AdamW | ... | ... | ... | 0.939 | 0.688 |
| YOLOv8n | 50 | 0.001 | 16 | AdamW | ... | ... | ... | 0.944 | 0.678 |
| vit_b_16 | 1000 |  0.0001 | 32 | Adam | 0.093 | 88.34% | 84.15% | ... |
| vit_l_32 | 2500 | 0.00001 | 128 | SGD | 0.041 | 90.19% | 87.55% | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | 

#### 2. Ablation Study
Any improvements or modifications of your base model, should be summarized in this table. Feel free to adjust the columns in the table below.

| model | layer_A | layer_B | layer_C | ... | top1_acc | top5_acc |
| --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | Conv(3x3, 64) x2 | Conv(3x3, 512) x3 | Conv(1x1, 2048) x3 | ... | 77.43% | 80.08% |
| vit_b_16 | Conv(3x3, 32) x3 | Conv(3x3, 128) x3 | Conv(1x1, 1028) x2 | ... | 72.11% | 76.84% |
| ... | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
Insert an image regarding your training and evaluation performances (especially their losses). The aim is to assess whether your model is fit, overfit, or underfit.
 
### Testing
Show some implementations (demos) of this model. Show **at least 10 images** of how your model performs on the testing data.
![Untitled](https://github.com/user-attachments/assets/5c446257-5b4d-43ad-85f3-dd91e46cc5ce)
![Untitled](https://github.com/user-attachments/assets/d3617873-5e79-4e93-a410-374d10834aac)
![Untitled](https://github.com/user-attachments/assets/d7520c73-9297-4ef2-9b89-c96d9f9ff4f1)
![Untitled](https://github.com/user-attachments/assets/60b3637e-8c18-4f5f-9d0c-27897aea001c)
![Untitled](https://github.com/user-attachments/assets/5278354f-c326-4590-8be1-f7cdf64fb3d3)
![Untitled](https://github.com/user-attachments/assets/14f1292f-0f65-4c5d-bf0c-4c90a34b11ea)
![Untitled](https://github.com/user-attachments/assets/3150a55f-1637-4c8b-9963-9c27f84429b3)
![Untitled](https://github.com/user-attachments/assets/41b6a002-7730-40b3-a778-82087fed4477)
![Untitled](https://github.com/user-attachments/assets/15985a3a-5f13-4b6a-970f-966323537173)
![Untitled](https://github.com/user-attachments/assets/45f5ca98-1979-4f35-a925-00fc524e93ba)

### Deployment (Optional)
Describe and show how you deploy this project (e.g., using Streamlit or Flask), if any.

## Supporting Documents
### Presentation Deck
- Link: https://...

### Business Model Canvas
Provide a screenshot of your Business Model Canvas (BMC). Give some explanations, if necessary.
![BMC](https://github.com/user-attachments/assets/25341651-8a71-464e-9c65-583735bd88c9)

### Short Video
Provide a link to your short video, that should includes the project background and how it works.
- Link: https://...

## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://...
- Link: https://...
- Link: https://...

## Additional Comments
Provide your team's additional comments or final remarks for this project. For example,
1. ...
2. ...
3. ...

## How to Cite
If you find this project useful, we'd grateful if you cite this repository:
```
@article{
...
}
```

## License
For academic and non-commercial use only.

## Acknowledgement
This project entitled <b>"AI-Driven Road Quality Detection for Accessiblity and Safety"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.
