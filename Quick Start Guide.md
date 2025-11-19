# ⚡ Quick Start Guide

Get your AES Encryption Tool up and running in 5 minutes!

## 🚀 Option 1: Deploy Directly (Fastest)

### For Streamlit Cloud:

```bash
# 1. Create new repo on GitHub
# 2. Clone this template
git clone https://github.com/YOUR_USERNAME/AES-Encryption-Tool.git
cd AES-Encryption-Tool

# 3. Push to your GitHub
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main

# 4. Go to share.streamlit.io and deploy!
```

**Done! Your app will be live in 2-3 minutes! 🎉**

---

## 💻 Option 2: Run Locally

### Prerequisites
- Python 3.8 or higher installed
- pip package manager

### Installation (3 commands)

```bash
# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/AES-Encryption-Tool.git
cd AES-Encryption-Tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run streamlit_app.py
```

**That's it!** Browser opens automatically at `http://localhost:8501`

---

## 📁 Project Structure

```
AES-Encryption-Tool/
├── streamlit_app.py          # Main application (run this!)
├── requirements.txt           # Dependencies
├── README.md                 # Full documentation
├── DEPLOYMENT_GUIDE.md       # Detailed deployment steps
├── QUICK_START.md           # This file
└── .gitignore               # Git ignore file
```

---

## 🎯 What You Need to Change

Before deploying, update these in **README.md**:

```markdown
# Line 7: Add your deployed URL
**[Launch App on Streamlit Cloud](YOUR_DEPLOYED_URL_HERE)**

# Line 245: Add your GitHub username
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

# Line 246: Update issue link
- Issues: [Report a bug](https://github.com/YOUR_USERNAME/AES-Encryption-Tool/issues)
```

---

## 🔑 First Time Usage

### Encrypting:
1. Open the app
2. Select "Encrypt" mode
3. Choose key size (256-bit recommended)
4. Enter a strong password
5. Type your message
6. Click "🚀 Encrypt Message"
7. Copy or download the result

### Decrypting:
1. Select "Decrypt" mode
2. Enter the **same password**
3. Paste encrypted text
4. Click "🚀 Decrypt Message"
5. View your original message

---

## 🐛 Common First-Time Issues

### Issue: "Module not found"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Port already in use"
**Solution:**
```bash
# Use a different port
streamlit run streamlit_app.py --server.port 8502
```

### Issue: App won't start
**Solution:**
```bash
# Check Python version (must be 3.8+)
python --version

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

---

## 📦 Dependencies Explained

```txt
streamlit==1.32.0          # Web framework for the UI
pycryptodome==3.20.0      # AES encryption library
```

That's all you need! Only 2 dependencies.

---

## 🎨 Customization Ideas

### Change Color Scheme
Edit CSS in `streamlit_app.py`:
```python
st.markdown("""
    <style>
    .stButton>button {
        background-color: #YOUR_COLOR;  # Change this!
    }
    </style>
""", unsafe_allow_html=True)
```

### Add Your Branding
```python
st.title("🔐 Your Company Name - AES Tool")
```

### Modify Key Sizes
```python
key_size = st.selectbox(
    "Key Size (bits)",
    [128, 192, 256, 512],  # Add more options
    index=2
)
```

---

## 📚 Next Steps

1. ✅ Get the app running
2. ✅ Test encryption/decryption
3. ✅ Deploy to Streamlit Cloud
4. ✅ Share with friends
5. ✅ Star the repo (if helpful!)
6. ✅ Customize for your needs

---

## 🎓 Learning Resources

- **AES Algorithm**: [Wikipedia](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- **Streamlit Tutorial**: [docs.streamlit.io](https://docs.streamlit.io)
- **PyCryptodome Docs**: [pycryptodome.readthedocs.io](https://pycryptodome.readthedocs.io)

---

## 💡 Pro Tips

1. **Use 256-bit keys** for maximum security
2. **Strong passwords** should be 16+ characters
3. **Never share** your encryption password
4. **Test locally** before deploying
5. **Keep dependencies updated**

---

## 🆘 Still Stuck?

1. Check the full [README.md](README.md)
2. Review [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
3. Open a GitHub issue
4. Ask on Streamlit Community Forum

---

## ✅ Success Checklist

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Dependencies installed
- [ ] App runs locally
- [ ] Tested encryption/decryption
- [ ] Code pushed to GitHub
- [ ] App deployed to cloud
- [ ] Updated README with live URL

**Congratulations! You're all set! 🎉**

---

**Time to Deploy**: ~5 minutes  
**Difficulty**: ⭐ Beginner Friendly  
**Cost**: $0 (Free!)

Happy Encrypting! 🔐✨