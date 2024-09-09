# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 09:16:11 2024

@author: BR0016447473
"""
import streamlit as st
import requests
from PIL import Image
import qrcode
from io import BytesIO
import pyshorteners
# Função para encurtar o link usando a API do TinyURL

def shorten_url(url_longa):
    # Inicialize o objeto de encurtador
    s = pyshorteners.Shortener()

    # Use o TinyURL para encurtar a URL
    url_encurtada = s.tinyurl.short(url_longa)
    
    return url_encurtada

# Função para gerar QR code
def generate_qr_code(link):
    qr = qrcode.make(link)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Interface do Streamlit
st.title("Encurtador de Links e Gerador de QR Code")

# Entrada do usuário
url = st.text_input("Digite o link que deseja encurtar:")

if st.button("Encurtar Link"):
    if url:
        short_url = shorten_url(url)
        if short_url:
            st.success(f"Link encurtado: {short_url}")
            
            # Gerar QR Code
            qr_image = generate_qr_code(short_url)
            st.image(qr_image, caption="QR Code do Link Encurtado", use_column_width=True)
    else:
        st.warning("Por favor, digite um link válido.")
