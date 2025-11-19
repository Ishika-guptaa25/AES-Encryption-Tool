import streamlit as st
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

st.set_page_config(
    page_title="AES Encryption Tool",
    page_icon="🔐",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem;
        border-radius: 5px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .success-box {
        padding: 1rem;
        border-radius: 5px;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .info-box {
        padding: 1rem;
        border-radius: 5px;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.title("🔐 AES Encryption & Decryption Tool")
st.markdown("### A secure implementation of Advanced Encryption Standard (AES)")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    mode = st.selectbox(
        "Select Mode",
        ["Encrypt", "Decrypt"],
        help="Choose whether to encrypt or decrypt your data"
    )

    key_size = st.selectbox(
        "Key Size (bits)",
        [128, 192, 256],
        index=2,
        help="AES supports 128, 192, or 256-bit keys. 256-bit is most secure."
    )

    st.markdown("---")
    st.markdown("### 📚 About AES")
    st.info("""
    **AES (Advanced Encryption Standard)** is a symmetric block cipher 
    that encrypts data in 128-bit blocks using keys of 128, 192, or 256 bits.

    **Features:**
    - Industry standard encryption
    - Used by governments & enterprises
    - Highly secure & efficient
    """)


# Helper Functions
def generate_key(password, key_size):
    """Generate AES key from password using SHA-256"""
    key = hashlib.sha256(password.encode()).digest()
    if key_size == 128:
        return key[:16]
    elif key_size == 192:
        return key[:24]
    else:  # 256
        return key[:32]


def encrypt_aes(plaintext, key):
    """Encrypt plaintext using AES in CBC mode"""
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    # Return IV + ciphertext as base64
    return base64.b64encode(iv + ciphertext).decode('utf-8')


def decrypt_aes(ciphertext_b64, key):
    """Decrypt ciphertext using AES in CBC mode"""
    try:
        data = base64.b64decode(ciphertext_b64)
        iv = data[:16]
        ciphertext = data[16:]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        return plaintext.decode('utf-8')
    except Exception as e:
        return f"Decryption failed: {str(e)}"


# Main Content
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔑 Key Configuration")
    password = st.text_input(
        "Enter Password/Key",
        type="password",
        help="Your password will be converted to a secure AES key",
        placeholder="Enter a strong password"
    )

    if password:
        st.success(f"✅ Key generated ({key_size}-bit)")
        key = generate_key(password, key_size)
    else:
        st.warning("⚠️ Please enter a password")

with col2:
    st.subheader("📝 Input Data")
    if mode == "Encrypt":
        input_text = st.text_area(
            "Enter text to encrypt",
            height=150,
            placeholder="Type your message here..."
        )
    else:
        input_text = st.text_area(
            "Enter encrypted text (Base64)",
            height=150,
            placeholder="Paste your encrypted text here..."
        )

st.markdown("---")

# Process Button
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    process_button = st.button(f"🚀 {mode} Message", use_container_width=True)

# Output Section
if process_button:
    if not password:
        st.error("❌ Please enter a password!")
    elif not input_text:
        st.error("❌ Please enter some text!")
    else:
        key = generate_key(password, key_size)

        if mode == "Encrypt":
            result = encrypt_aes(input_text, key)
            st.success("✅ Encryption Successful!")

            st.subheader("🔒 Encrypted Output")
            st.code(result, language=None)

            # Copy button simulation
            st.download_button(
                label="📥 Download Encrypted Text",
                data=result,
                file_name="encrypted_message.txt",
                mime="text/plain"
            )

            # Show info
            col_info1, col_info2 = st.columns(2)
            with col_info1:
                st.metric("Original Length", f"{len(input_text)} chars")
            with col_info2:
                st.metric("Encrypted Length", f"{len(result)} chars")

        else:  # Decrypt
            result = decrypt_aes(input_text, key)

            if result.startswith("Decryption failed"):
                st.error(f"❌ {result}")
            else:
                st.success("✅ Decryption Successful!")

                st.subheader("🔓 Decrypted Output")
                st.text_area("Decrypted Message", result, height=150)

                st.download_button(
                    label="📥 Download Decrypted Text",
                    data=result,
                    file_name="decrypted_message.txt",
                    mime="text/plain"
                )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🔐 <strong>AES Encryption Tool</strong> | Built with Python & Streamlit</p>
        <p>⚡ Secure • Fast • Easy to Use</p>
    </div>
""", unsafe_allow_html=True)

# Educational Section
with st.expander("📖 How AES Works"):
    st.markdown("""
    ### AES Encryption Process

    **Key Features:**
    - **Block Cipher**: Operates on 128-bit (16-byte) blocks
    - **Symmetric**: Same key for encryption and decryption
    - **Rounds**: Multiple rounds of substitution and permutation
        - 10 rounds for 128-bit keys
        - 12 rounds for 192-bit keys
        - 14 rounds for 256-bit keys

    **Main Operations:**
    1. **SubBytes**: Non-linear substitution
    2. **ShiftRows**: Row-wise permutation
    3. **MixColumns**: Column mixing
    4. **AddRoundKey**: XOR with round key

    **Modes of Operation:**
    - This tool uses **CBC (Cipher Block Chaining)** mode
    - Includes an Initialization Vector (IV) for added security
    - Each ciphertext block depends on all previous plaintext blocks
    """)

with st.expander("🛡️ Security Best Practices"):
    st.markdown("""
    ### Tips for Secure Encryption

    ✅ **Do:**
    - Use strong, random passwords (at least 16 characters)
    - Use 256-bit keys for maximum security
    - Store keys securely
    - Use unique passwords for different data

    ❌ **Don't:**
    - Reuse passwords across multiple encryptions
    - Share your encryption key
    - Use weak or common passwords
    - Store keys in plain text

    ⚠️ **Note:** This is an educational tool. For production use, consider additional security measures like key management systems and secure key storage.
    """)