# UIDAI Hackathon - Aadhaar Enrollment Analysis

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- 8GB RAM minimum
- 2GB free disk space

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ahmadjaved79/uidai-hackathon.git
cd uidai-hackathon
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download datasets:
```bash
python setup.py
```
**Alternative**: Manually download from [Google Drive](LINK) and place in `data/raw/`

4. Run analysis:
```bash
jupyter notebook notebooks/01_exploration.ipynb
```

## 📊 Data Sources

Due to GitHub's file size limitations, datasets are hosted externally:
- **Aadhaar Overall Data** (450 MB): [Download Link](https://drive.google.com/...)
- **Aadhaar State-wise Data** (280 MB): [Download Link](https://drive.google.com/...)

## 📁 Project Structure
```
├── notebooks/          # Jupyter notebooks with analysis
├── src/               # Python modules
├── outputs/           # Generated figures and results
├── final_report.pdf   # Hackathon submission
└── README.md
```

## 🔧 Troubleshooting

**Issue**: "Data files not found"
**Solution**: Run `python setup.py` or manually download datasets

**Issue**: "Out of memory"
**Solution**: Use data sampling in notebooks (set `SAMPLE_SIZE=10000`)