"""
IliaChan TechWell — CLIP Embedding Engine
Generates image and text embeddings using OpenAI CLIP model.
"""

import numpy as np
import streamlit as st
from PIL import Image
from config import CLIP_MODEL


@st.cache_resource(show_spinner="Loading CLIP model...")
def load_clip_model():
    """Load CLIP model and processor (cached)."""
    try:
        # pyrefly: ignore [missing-import]
        from transformers import CLIPModel, CLIPProcessor
        model = CLIPModel.from_pretrained(CLIP_MODEL)
        processor = CLIPProcessor.from_pretrained(CLIP_MODEL)
        return model, processor
    except Exception as e:
        st.warning(f"CLIP model not available: {e}. Image similarity search disabled.")
        return None, None


def encode_image(image: Image.Image) -> np.ndarray:
    """Generate CLIP embedding from a PIL Image."""
    model, processor = load_clip_model()
    if model is None:
        return np.zeros(512, dtype=np.float32)

    # pyrefly: ignore [missing-import]
    import torch
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        features = model.get_image_features(**inputs)
    embedding = features.cpu().numpy().flatten()
    # L2 normalize
    norm = np.linalg.norm(embedding)
    if norm > 0:
        embedding = embedding / norm
    return embedding.astype(np.float32)


def encode_text(text: str) -> np.ndarray:
    """Generate CLIP embedding from text."""
    model, processor = load_clip_model()
    if model is None:
        return np.zeros(512, dtype=np.float32)

    # pyrefly: ignore [missing-import]
    import torch
    inputs = processor(text=[text], return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        features = model.get_text_features(**inputs)
    embedding = features.cpu().numpy().flatten()
    norm = np.linalg.norm(embedding)
    if norm > 0:
        embedding = embedding / norm
    return embedding.astype(np.float32)


def compute_similarity(emb_a: np.ndarray, emb_b: np.ndarray) -> float:
    """Compute cosine similarity between two embeddings."""
    if emb_a is None or emb_b is None:
        return 0.0
    dot = np.dot(emb_a, emb_b)
    norm_a = np.linalg.norm(emb_a)
    norm_b = np.linalg.norm(emb_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot / (norm_a * norm_b))
