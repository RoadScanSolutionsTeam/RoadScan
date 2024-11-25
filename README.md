# RoadScan

## Project Description
Please describe your Startup Campus final project here. You may should your <b>model architecture</b> in JPEG or GIF.

**RoadScan** adalah platform berbasis teknologi object detection yang memanfaatkan kecerdasan buatan (AI) untuk mendeteksi berbagai kerusakan infrastruktur jalan seperti lubang, retakan, atau deformasi. Solusi ini memberikan kemampuan otomatisasi, akurasi tinggi, dan efisiensi dalam memantau kondisi jalan untuk perencanaan perbaikan yang lebih strategis.

Detail Fitur dan Manfaat:
- **Automatisasi Inspeksi Jalan**<br>
   Sistem berbasis AI ini secara otomatis mampu mendeteksi jenis kerusakan jalan dari gambar atau video, menggantikan inspeksi manual yang memakan waktu dan tenaga.
- **Penghematan Biaya dan Waktu**<br>
   Implementasi sistem ini menghasilkan respons yang lebih cepat dan efisien terhadap kerusakan jalan sehingga mengurangi biaya perbaikan dan durasi inspeksi manual.
- **Pemetaan Kerusakan dan Prioritas Perbaikan**<br>
   Platform ini menghasilkan data untuk memetakan area dengan kerusakan paling parah, sehingga memudahkan penentuan prioritas perbaikan sesuai kebutuhan.
- **Peningkatan Keselamatan dan Kepuasan Pengguna Jalan**<br>
   Dengan deteksi dini kerusakan jalan ini menurunkan risiko kecelakaan akibat jalan rusak dan meningkatkan kepercayaan masyarakat terhadap kualitas infrastruktur.

RoadScan mendukung pencapaian Sustainable Development Goal (SDG) 11: Kota dan Pemukiman yang Berkelanjutan.
- Meningkatkan keselamatan dan mobilitas masyarakat melalui deteksi dini kerusakan jalan.
- Mendorong efisiensi dalam perbaikan jalan, sehingga mendukung kota yang lebih tangguh, aman, dan ramah lingkungan.

## Contributor
| Full Name | Affiliation | Email | LinkedIn | Role |
| --- | --- | --- | --- | --- |
| Marsyanda Salsa Nabila | Startup Campus, AI Track | marsyandasalsa2021@gmail.com  | [link](https://www.linkedin.com/in/marsyandasalsanabila/) | Team Lead |
| Ilham Khefi Ramadhanu | Startup Campus, AI Track | ilhamramadhanu25@gmail.com | [link](https://www.linkedin.com/in/ilham-khefi-ramadhanu) | Team Member |
| Mochamad Freski Dino Fava | Startup Campus, AI Track | dinofava12@gmail.com | [link](https://www.linkedin.com/in/mochamad-freski-dino-fava-4a9162323/) | Team Member |
| Shafa Anisya Aji Divana | Startup Campus, AI Track | shafadivana@gmail.com | [link](https://www.linkedin.com/in/shafadivana/) | Team Member |
| Nisrina Alifa Adzahra | Startup Campus, AI Track | nisrinalifa@gmail.com | [link](https://www.linkedin.com/in/nisrina-alifa-adzahra/) | Team Member |
| Cijo Jidan Riady | Startup Campus, AI Track | ... | ... | Team Member |
| Ghea Dwi Apriliana | Startup Campus, AI Track | gheapriliana96@gmail.com | [link](https://www.linkedin.com/in/ghea-dwi-apriliana-5623a8193/) | Team Member |
| Nicholas Dominic | Startup Campus, AI Track | nic.dominic@icloud.com | [link](https://linkedin.com/in/nicholas-dominic) | Supervisor |

## Setup
### Prerequisite Packages (Dependencies)
- pandas==2.1.0
- openai==0.28.0
- google-cloud-aiplatform==1.34.0
- google-cloud-bigquery==3.12.0
- tensorflow==2.12.0
- opencv-python==4.6.0
- numpy==1.23.0
- Pillow==7.1.2
- pyyaml==5.3.1
- requests==2.23.0
- seaborn==0.11.0
- scikit-learn==1.3.0
- torch==1.8.0
- torchvision==0.9.0
- tqdm==4.64.0
- ultralytics==8.3.31
- ultralytics-thop==2.0.0
- customtkinter==5.2.0
- matplotlib==3.3.0
- seaborn==0.12.0
- scipy==1.4.1
- contourpy==1.0.1
- cycler==0.10
- fonttools==4.22.0
- kiwisolver==1.0.1
- packaging==20.0
- pyparsing==2.3.1
- python-dateutil==2.7
- pytz==2020.1
- tzdata==2022.1
- charset-normalizer<4,==2
- idna<4,==2.5
- urllib3<3,==1.21.1
- certifi==2017.4.17
- typing-extensions==4.8.0
- MarkupSafe==2.0
- mpmath<1.4,==1.1.0
- ...
- ...

### Environment
| | |
| --- | --- |
| CPU | Intel(R) Core(TM) i7-7820HQ CPU @ 2.90GHz   2.90 GHz |
| GPU | NVIDIA GeForce 940MX |
| ROM | 256 GB SSD |
| RAM | 32 GB |
| OS | Example: Windows 10 Pro 22H2 |

## Dataset
Describe your dataset information here. Provide a screenshot for some of your dataset samples (for example, if you're using CIFAR10 dataset, then show an image for each class).

Dataset "Jalan Rusak" dirancang untuk mendeteksi kerusakan jalan menggunakan teknik computer vision. Dataset ini terdiri dari gambar-gambar yang telah dianotasi dengan label yang merepresentasikan berbagai jenis kerusakan jalan. Yaitu berisi kumpulan foto kerusakan jalan yang berjumlah 4.983 data, dengan pembagian sebanyak 4.098 data train, 591 data validation, dan 294 data test yang terbagi menjadi 6 kategori yaitu Lubang, Melintang, Memanjang, Pinggir, Retak Buaya dan Sambungan.

- Link: https://universe.roboflow.com/tugas-xogo7/jalanrusak-zofhk

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
Berikut adalah tuning terbaik yang kami pilih dan gunakan untuk modifikasi arsitektur model.

| model | epoch | learning_rate | batch_size | optimizer | val_precision | val_recall | mAP50 | mAP 50-95 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLOv8s | 50 | 0.001 | 32 | AdamW | 0.902 | 0.908 | 0.947 | 0.707 |
| YOLOv8s | 50 | 0.001 | 16 | AdamW | 0.898 | 0.902 | 0.943 | 0.698 |
| YOLOv8n | 50 | 0.001 | 32 | AdamW | 0.908 | 0.889 | 0.939 | 0.688 |
| YOLOv8n | 50 | 0.001 | 16 | AdamW | 0.904 | 0.888 | 0.944 | 0.678 |

Model dengan hyperparameter terbaik yang kami pilih adalah:
| model | epoch | learning_rate | batch_size | optimizer | val_precision | val_recall | mAP50 | mAP 50-95 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YOLOv8s | 50 | 0.001 | 32 | AdamW | 0.902 | 0.908 | 0.947 | 0.707 |

Alasan kami memilih model tersebut sebagai model terbaik yang kami terapkan karena tingkat keakuratan yang didapatkan cukup tinggi dan cukup optimal.

#### 2. Training/Validation Curve

##### Training Curve: 
- Precision Curve:
- Recall Curve:
- PR Curve:
- F1 Curve:

##### Validation Curve: 
- Precision Curve:
- Recall Curve:
- PR Curve:
- F1 Curve:

##### Train / Val Loss:
![results](https://github.com/user-attachments/assets/ccf05972-4e6d-47a0-9f2a-f216572f45b3)

#### 3. Confusion Matrix
![confusion_matrix](https://github.com/user-attachments/assets/d95d2dcc-b2b0-4f97-9a33-8dacc834cb2b)

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
This project entitled <b>"RoadScan"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.
