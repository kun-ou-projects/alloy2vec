import os
import requests
from tqdm import tqdm
from setuptools import find_packages, setup, Command

class downloadword2vecmodels(Command):
    user_options = [] 

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        base_dir = "training/models/"
        
        file_groups = {
            '': [ 
                "https://drive.google.com/file/d/1mhkHV-ZFYBIDWKZacbK8w_svtcnGAWwQ/view?usp=drive_link", 
                "https://drive.google.com/file/d/18BhdEVbZagC6IdPF-7mBB5_GKU-fypZ2/view?usp=drive_link", 
                "https://drive.google.com/file/d/1pFxPf0EY-qxSLPhPQyr3bfGG06CA4EYE/view?usp=drive_link", 
                "https://drive.google.com/file/d/1rO1dMoPhD21LfJUcTKWp9Nn7Mutu3vQy/view?usp=drive_link", 
                "https://drive.google.com/file/d/1WeHPNCousaSvQFHoDobVEDowBPEyHUGt/view?usp=drive_link"
                ],

            'aligned_time_series_embeddings/': [ 
                "https://drive.google.com/file/d/1UHpVBCnPR081VYVfEiWR7TaSivhYnUOl/view?usp=drive_link",
                "https://drive.google.com/file/d/1uMoyRWZXAsNCrKdynYHuT8Ng9p7jkRIz/view?usp=drive_link",
                "https://drive.google.com/file/d/1jqARBltTuoz1D52W6-xyN5wxVYkTcMIA/view?usp=drive_link",
                "https://drive.google.com/file/d/1qtgORcTwpQAH5M0vxmSYSkPxBnrqs4rQ/view?usp=drive_link",
                "https://drive.google.com/file/d/1Z3fkwdfxKTRgYeMEcGeMiChlkqcvPy0r/view?usp=drive_link",
                "https://drive.google.com/file/d/1FnQqActmOx6RTfpPrCA1N8RSs_QSQ4rQ/view?usp=drive_link",
                "https://drive.google.com/file/d/1sr2oL9CdjZ67fHBHuKJZszmPf0LDakqJ/view?usp=drive_link",
                "https://drive.google.com/file/d/1CkDscIM2yeHJaAO794I6Jn9Z0XX_8X9E/view?usp=drive_link",
                "https://drive.google.com/file/d/19vuFbOzPg3AVO3ATcVwGYuoCDavSRAxM/view?usp=drive_link",
                "https://drive.google.com/file/d/12Bos0AN0YWwEHWJojNEr0dmw_iHzeN5A/view?usp=drive_link",
                "https://drive.google.com/file/d/1iy0Vu1ndkZTusQp7QKqgibFkh3rcffBW/view?usp=drive_link",
                "https://drive.google.com/file/d/1KnOmOb2zaH6e33l4L_oyY4hJfkgjyqqI/view?usp=drive_link",
                "https://drive.google.com/file/d/1ZrAQ9vvo6ZPsfJjdpD3N3-X4vcTnDr6q/view?usp=drive_link",
                "https://drive.google.com/file/d/17JDRJpIkyJ86o_6pU8sLe7RV8nPU1UcQ/view?usp=drive_link",
                "https://drive.google.com/file/d/1DcH8skprsrfj3pLyWeZdfSKYPh3Y6VUT/view?usp=drive_link",
                "https://drive.google.com/file/d/1byIXYXltkRNSHASUXYKjcZ_96hOvEbBG/view?usp=drive_link",
                "https://drive.google.com/file/d/1nMsYE0j9NtNxLevPdb5RTDi7NpwWrrGU/view?usp=drive_link",
                "https://drive.google.com/file/d/1scUEt3HuPxVtpfAdnhM2Q8oJoe8JZXKh/view?usp=drive_link",
                "https://drive.google.com/file/d/1H67hcC5dBCzmIR971Upee9HfVhIga5wM/view?usp=drive_link",
                "https://drive.google.com/file/d/1U6EmbPQ14iHiDudKYyAYs9iGgYZTPfS-/view?usp=drive_link",
                "https://drive.google.com/file/d/1HEcVazrX16uYQuFHVijoFdwWUdHbuAC4/view?usp=drive_link",
                "https://drive.google.com/file/d/1A8TX8VSBFHac6nLqywi7JLIWfmvtMJW7/view?usp=drive_link",
                "https://drive.google.com/file/d/1_LpGTzzT79vXV94qcTTgfCpegnzN7yVM/view?usp=drive_link",
                "https://drive.google.com/file/d/10Tz1VxCbCPMi5m_hPzyvsxojZQKiUY3s/view?usp=drive_link"
            ],
            'processing/data/': [
                "https://drive.google.com/file/d/1Vju0c9royDRuoTHvYDm657fELTMwHaaG/view?usp=drive_link"
            ],
            'processing/models/': [
                "https://drive.google.com/file/d/1mK3eZYya3eBTbRDlg2kQ2wS262c0Bk5N/view?usp=drive_link"
            ],
        }

        secondary_dirs = {
            'processing/models/': 'training/alloy2vec/processing/models/',
        }

        for subdir, urls in file_groups.items():
            full_path = os.path.join(base_dir, subdir)
            if not os.path.exists(full_path):
                os.makedirs(full_path)
            for url in urls:
                response = requests.get(url, stream=True)
                total_size_in_bytes= int(response.headers.get('content-length', 0))
                block_size = 1024  # 1 Kibibyte
                progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                filename = url.split('/')[-1]
                with open(os.path.join(full_path, filename), 'wb') as file:
                    for data in response.iter_content(block_size):
                        progress_bar.update(len(data))
                        file.write(data)
                progress_bar.close()
                if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                    print("ERROR, something went wrong")
                print(f"Downloaded and saved {filename} to {full_path}")

def read_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]

setup(
    name="tracking_progress_metallic_materials",
    version="0.1",
    author="Xin Wang",
    author_email="xin.etica.wang@gmail.com",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=read_requirements(), 
    url='https://github.com/kun-ou-projects/tracking_progress_metallic_materials',
    cmdclass={
        'install': downloadword2vecmodels,
    }
)